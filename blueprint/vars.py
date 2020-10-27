from calm.dsl.builtins import read_local_file, basic_cred

# Change values based on your calm environment
IMAGE_NAME = 'centos-7'
NETWORK_NAME = 'DC-1-NET-1'
VM_USERNAME = 'centos'


# Secret variables (.local file store)
CENTOS_KEY = read_local_file('centos')

# Blueprint credentials
CENTOS_CRED = basic_cred(VM_USERNAME, CENTOS_KEY, name='CENTOS_CRED', type='KEY', default=True)

