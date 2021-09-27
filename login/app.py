from flask import Flask, request, make_response, redirect, render_template
import requests
from logger import log
from config import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    error_message = None
    log.info(f'DEBUG={redirect_prism}')
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        log.info(f'Log request from user: {username}')

        # if no username or password return error message on login page
        if not (username and password):
            error_message = 'Username and password are required'
            return render_template('index.html',
                                   page_title=page_title,
                                   login_title=login_title,
                                   error_message=error_message)

        is_authenticated, cookies = prism_login(username, password, request.headers.get('User-Agent'))

        # user is authenticated successfully, redirect to Prism dashboard
        if is_authenticated:
            log.info(f'User {username} logged successfully')
            authenticated_resp = make_response(redirect(redirect_prism))
            for cookie in cookies:
                authenticated_resp.set_cookie(cookie.name, cookie.value, secure=cookie.secure,
                                              httponly=True, expires=cookie.expires)
            return authenticated_resp
        else:
            log.info(f'User {username} login failed')
            error_message = 'Wrong username or password, try again please.'
            return render_template('index.html',
                                   page_title=page_title,
                                   login_title=login_title,
                                   error_message=error_message)

    return render_template('index.html',
                           page_title=page_title,
                           login_title=login_title)


def prism_login(username, password, user_agent=None):

    base_url = f'https://{prism_ip}:{prism_port}'
    api_url = f'{base_url}/api/nutanix/v3/users/me'
    spring_security_url = f'{base_url}/PrismGateway/j_spring_security_check'

    headers = {
        'X-Nutanix-Client-Type': 'ui',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    if user_agent:
        headers['User-Agent'] = user_agent

    client = requests.Session()
    resp = client.get(api_url, verify=verify_ssl, auth=(username, password), headers=headers)

    # API login passed, move to spring_security
    if resp.status_code == 200:
        log.info(f'api login pass for user: {username}')

        # the user is domain based, no need to perform spring security check
        # if '@' in username:
        #     log.info(f'User {username} is a LDAP user')
        #     return True, client.cookies

        # local admin continue with spring security check
        data = f'j_username={username}&j_password={password}'
        resp = client.post(spring_security_url, verify=verify_ssl, data=data, headers=headers)
        if resp.status_code == 200:
            log.info(f'spring check pass for user: {username}')
        return True, client.cookies

    # one of the stages failed
    log.info(f'error in login for user: {username}')
    return False, None


if __name__ == '__main__':
    app.run()
