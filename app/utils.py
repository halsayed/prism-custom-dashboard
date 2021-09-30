import requests
from flask import make_response, redirect, request
from flask import current_app as app
from urllib.parse import urljoin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


def successful_redirect(cookies, destination='/'):
    response = make_response(redirect(urljoin(request.base_url, destination)))
    for cookie in cookies:
        response.set_cookie(cookie.name, cookie.value, secure=cookie.secure, expires=cookie.expires)

    return response


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


def prism_login(username, password, user_agent=None):
    base_url = app.config['BASE_URL']
    api_url = urljoin(app.config['API_URL'], 'users/me')
    app.logger.debug(api_url)
    spring_security_url = f'{base_url}/PrismGateway/j_spring_security_check'

    # attach domain if provided in config
    if app.config['ATTACH_DOMAIN'] and '@' not in username:
        username = username + '@' + app.config['ATTACH_DOMAIN']

    headers = {
        'X-Nutanix-Client-Type': 'ui',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    if user_agent:
        headers['User-Agent'] = user_agent

    client = requests.Session()
    resp = client.get(api_url, verify=app.config['SSL_VERIFY'], auth=(username, password), headers=headers)
    app.logger.debug(f'Auth API call status: {resp.status_code}, msg: {resp.content}')

    # API login passed, move to spring_security
    if resp.status_code == 200:
        app.logger.info(f'api login pass for user: {username}')

        # the user is domain based, no need to perform spring security check
        # if '@' in username:
        #     log.info(f'User {username} is a LDAP user')
        #     return True, client.cookies

        # local admin continue with spring security check
        data = f'j_username={username}&j_password={password}'
        resp = client.post(spring_security_url, verify=app.config['SSL_VERIFY'], data=data, headers=headers)
        if resp.status_code == 200:
            app.logger.info(f'spring check pass for user: {username}')
        return True, client.cookies

    # one of the stages failed
    app.logger.info(f'error in login for user: {username}')
    return False, None
