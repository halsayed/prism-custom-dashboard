from calm.dsl.builtins import AhvVmResources, AhvVm
from calm.dsl.builtins import AhvVmDisk, AhvVmNic, AhvVmGC, vm_disk_package

from vars import VM_USERNAME, IMAGE_NAME, NETWORK_NAME, IMAGE_URL

ubuntuDisk = vm_disk_package(name=IMAGE_NAME, config={"image": {"source": IMAGE_URL}})


class UbuntuVmResource(AhvVmResources):
    """Base CentOS VM Resource """

    memory = 4
    vCPUs = 2
    cores_per_vCPU = 1
    disks = [AhvVmDisk.Disk.Scsi.cloneFromVMDiskPackage(ubuntuDisk, bootable=True)]
    nics = [AhvVmNic.DirectNic.ingress(NETWORK_NAME)]
    guest_customization = AhvVmGC.CloudInit(
        config={
            'users': 
            [{
                'name': VM_USERNAME,
                'ssh-authorized-keys': ["@@{UBUNTU_CRED.public_key}@@"],
                'sudo': ['ALL=(ALL) NOPASSWD:ALL']
            }]
        }
    )


class UbuntuAhvVM(AhvVm):
    resources = UbuntuVmResource
