from calm.dsl.builtins import read_local_file, basic_cred

# Change values based on your calm environment
IMAGE_NAME = 'ubuntu_focal'
IMAGE_URL = 'https://cloud-images.ubuntu.com/focal/current/focal-server-cloudimg-amd64.img'
NETWORK_NAME = 'DC-1-NET-1'
VM_USERNAME = 'ubuntu'


# Secret variables (.local file store)
UBUNTU_KEY = read_local_file('centos')

# Blueprint credentials
UBUNTU_CRED = basic_cred(VM_USERNAME, UBUNTU_KEY, name='UBUNTU_CRED', type='KEY', default=True)

