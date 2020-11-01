from calm.dsl.builtins import Substrate, readiness_probe, read_provider_spec, ref, action, CalmTask

from base_vm import CentosAhvVM


class NginxSubstrace(Substrate):
    """CentOS substrate"""

    os_type = "Linux"
    provider_type = "AHV_VM"
    provider_spec = CentosAhvVM

    readiness_probe = readiness_probe(
        connection_type="SSH",
        disabled=True,
        retries="5",
        connection_port=22,
        address="@@{platform.status.resources.nic_list[0].ip_endpoint_list[0].ip}@@",
        delay_secs="60",
    )




