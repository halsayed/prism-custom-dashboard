import urllib3

from flask import Flask, request, render_template
from urllib.parse import urljoin
from app.utils import successful_redirect, LoginForm, prism_login


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    # disable ssl warning if SSL_VERIFY is disabled
    if not app.config['SSL_VERIFY']:
        urllib3.disable_warnings()

    @app.route('/', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        error_message = None

        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            app.logger.debug(f'Authenticating user: {username}')
            is_authenticated, cookies = prism_login(username, password, request.headers.get('User-Agent'))

            if is_authenticated:
                app.logger.info(f'User {username} logged successfully')
                # redirect user to Prism with authentication cookies
                dest_url = urljoin(request.base_url, app.config['REDIRECT_DEST'])
                app.logger.debug(dest_url)
                return successful_redirect(cookies, dest_url)
            else:
                error_message = 'Wrong username or password, try again please.'
                app.logger.info(f'User: {username} login failed')

        return render_template('index.html', form=form, page_title=app.config['HTML_TITLE'],
                               login_title=app.config['LOGIN_HEADER'], error_message=error_message)

    return app

