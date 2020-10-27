from calm.dsl.builtins import read_local_file, basic_cred

# Change values based on your calm environment
IMAGE_NAME = 'centos7'
IMAGE_URL = 'http://download.nutanix.com/calm/CentOS-7-x86_64-1810.qcow2'
NETWORK_NAME = 'DC-1-NET-1'
VM_USERNAME = 'centos'


# Secret variables (.local file store)
CENTOS_KEY = read_local_file('centos')

# Blueprint credentials
CENTOS_CRED = basic_cred(VM_USERNAME, CENTOS_KEY, name='UBUNTU_CRED', type='KEY', default=True)

