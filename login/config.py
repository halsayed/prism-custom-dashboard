import os

prism_ip = os.environ.get('PRISM_IP', '10.42.32.39')
prism_port = os.environ.get('PRISM_PORT', 9440)
page_title = os.environ.get('PAGE_TITLE', 'Prism Login')
login_title = os.environ.get('LOGIN_TITLE', 'Custom Prism Login')
verify_ssl = os.environ.get('VERIFY_SSL', False).lower() in ('true', '1', 't')
redirect_prism = os.environ.get('PRISM_REDIRECT', 'console/')

