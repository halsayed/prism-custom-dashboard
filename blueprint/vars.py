from calm.dsl.builtins import read_local_file, basic_cred

# Change values based on your calm environment
IMAGE_NAME = 'centos7'
IMAGE_URL = 'https://cloud.centos.org/centos/7/images/CentOS-7-x86_64-GenericCloud.qcow2'
NETWORK_NAME = 'Network-01'
VM_USERNAME = 'centos'


# Secret variables (.local file store)
CENTOS_KEY = read_local_file('centos')

# Blueprint credentials
CENTOS_CRED = basic_cred(VM_USERNAME, CENTOS_KEY, name='CENTOS_CRED', type='KEY', default=True)

