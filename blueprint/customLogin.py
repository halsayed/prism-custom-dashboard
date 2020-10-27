from calm.dsl.builtins import SimpleDeployment, SimpleBlueprint
from calm.dsl.builtins import read_local_file, basic_cred
from calm.dsl.builtins import AhvVmResources, AhvVmDisk, AhvVmNic, AhvVmGC, AhvVm
from calm.dsl.builtins import action, CalmTask, CalmVariable


# Change values based on your calm environment
IMAGE_NAME = 'centos-7'
NETWORK_NAME = 'DC-1-NET-1'

# Password file located under './.local'
CENTOS_PASSWD = read_local_file('centos')
CENTOS_CRED = basic_cred('centos', 'nutanix/4u', name='CENTOS_CRED', default=True)


class CentosVmResources(AhvVmResources):

    memory = 4
    vCPUs = 2
    cores_per_vCPU = 1
    disks = [AhvVmDisk.Disk.Scsi.cloneFromImageService(IMAGE_NAME, bootable=True)]
    nics = [AhvVmNic.DirectNic.ingress(NETWORK_NAME)]
    guest_customization = AhvVmGC.CloudInit(
        config={
            'password': CENTOS_PASSWD,
            'ssh_pwauth': True,
            'chpasswd': { 'expire': False }
        }
    )


class CentosVm(AhvVm):
    resources = CentosVmResources


class Nginx(SimpleDeployment):
    provider_spec = CentosVm
    os_type = 'Linux'

    @action
    def __install__(self):
        CalmTask.Exec.ssh(name='install_nginx', filename='scripts/install_nginx.sh')



class customLogin(SimpleBlueprint):
    credentials = [CENTOS_CRED]
    deployments = [Nginx]

    COUNT = CalmVariable.WithOptions.Predefined.string(['1', '2', '3'], default='1', name='COUNT',
                                                        label='Apache Count', runtime=True)

def main():
    print(customLogin.json_dumps(pprint=True))

if __name__ == '__main__':
    main()
