import os

prism_ip = os.environ.get('PRISM_IP', '10.38.11.9')
prism_port = os.environ.get('PRISM_PORT', 9440)
page_title = os.environ.get('PAGE_TITLE', 'Prism Login')
login_title = os.environ.get('LOGIN_TITLE', 'Custom Prism Login')
verify_ssl = os.environ.get('VERIFY_SSL', False)
redirect_prism = os.environ.get('PRISM_REDIRECT', 'https://localhost/console/')

