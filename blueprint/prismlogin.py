# THIS FILE IS AUTOMATICALLY GENERATED.
# Disclaimer: Please test this file before using in production.
"""
Generated blueprint DSL (.py)
"""

import json  # no_qa
import os  # no_qa

from calm.dsl.builtins import *  # no_qa


# Secret Variables
BP_CRED_CRED_PASSWORD = read_local_file("BP_CRED_CRED_PASSWORD")

# Credentials
BP_CRED_CRED = basic_cred(
    "ubuntu",
    BP_CRED_CRED_PASSWORD,
    name="CRED",
    type="PASSWORD",
    default=True,
)


ubuntu_20_04_cloud = vm_disk_package(
    name="ubuntu_20_04_cloud",
    description="Standard ubuntu 20.04 cloud image",
    config={
        "name": "ubuntu_20_04_cloud",
        "image": {
            "name": "ubuntu_20_04_cloud",
            "type": "DISK_IMAGE",
            "source": "https://cloud-images.ubuntu.com/focal/current/focal-server-cloudimg-amd64.img",
            "architecture": "X86_64",
        },
        "product": {"name": "ubuntu", "version": "20.04"},
        "checksum": {},
    },
)


class nginx(Service):

    pass


class prismlogincalm_timeResources(AhvVmResources):

    memory = 4
    vCPUs = 1
    cores_per_vCPU = 1
    disks = [
        AhvVmDisk.Disk.Scsi.cloneFromVMDiskPackage(ubuntu_20_04_cloud, bootable=True)
    ]
    nics = [AhvVmNic.NormalNic.ingress("PUBLIC", cluster="DC-RUH")]

    guest_customization = AhvVmGC.CloudInit(
        filename=os.path.join("specs", "prismlogincalm_time_cloud_init_data.yaml")
    )


class prismlogincalm_time(AhvVm):

    name = "prism-login-@@{calm_time}@@"
    resources = prismlogincalm_timeResources


class AHVnginx(Substrate):

    os_type = "Linux"
    provider_type = "AHV_VM"
    provider_spec = prismlogincalm_time

    readiness_probe = readiness_probe(
        connection_type="SSH",
        disabled=False,
        retries="5",
        connection_port=22,
        address="@@{platform.status.resources.nic_list[0].ip_endpoint_list[0].ip}@@",
        delay_secs="60",
        credential=ref(BP_CRED_CRED),
    )


class Package1(Package):

    services = [ref(nginx)]

    @action
    def __install__():

        CalmTask.Exec.escript(
            name="01_resize_disk",
            filename=os.path.join(
                "scripts", "Package_Package1_Action___install___Task__01_resize_disk.py"
            ),
            target=ref(nginx),
        )
        CalmTask.Exec.ssh(
            name="02_restart",
            filename=os.path.join(
                "scripts", "Package_Package1_Action___install___Task__02_restart.sh"
            ),
            target=ref(nginx),
        )
        CalmTask.Delay(name="03_wait_for_reboot", delay_seconds=60, target=ref(nginx))
        CalmTask.Exec.ssh(
            name="04_update_os",
            filename=os.path.join(
                "scripts", "Package_Package1_Action___install___Task__04_update_os.sh"
            ),
            target=ref(nginx),
        )
        CalmTask.Exec.ssh(
            name="05_install_docker",
            filename=os.path.join(
                "scripts",
                "Package_Package1_Action___install___Task__05_install_docker.sh",
            ),
            target=ref(nginx),
        )
        CalmTask.Delay(name="06_restart", delay_seconds=60, target=ref(nginx))
        CalmTask.Exec.ssh(
            name="07_install_app",
            filename=os.path.join(
                "scripts", "Package_Package1_Action___install___Task__07_install_app.sh"
            ),
            target=ref(nginx),
        )


class _2d0ccc9f_deployment(Deployment):

    name = "2d0ccc9f_deployment"
    min_replicas = "1"
    max_replicas = "1"
    default_replicas = "1"

    packages = [ref(Package1)]
    substrate = ref(AHVnginx)


class Default(Profile):

    deployments = [_2d0ccc9f_deployment]

    PRISM_PORT = CalmVariable.Simple(
        "9440",
        label="Prism Central Port",
        is_mandatory=True,
        is_hidden=False,
        runtime=True,
        description="Default: 9440",
    )

    PRISM_HOST = CalmVariable.Simple(
        "10.38.12.9",
        label="Prism Central",
        is_mandatory=True,
        is_hidden=False,
        runtime=True,
        description="Hostname or IP address of Prism Central",
    )


class prismlogin(Blueprint):
    """Blueprint to deploy custom prism login page"""

    services = [nginx]
    packages = [Package1, ubuntu_20_04_cloud]
    substrates = [AHVnginx]
    profiles = [Default]
    credentials = [BP_CRED_CRED]
