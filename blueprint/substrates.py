from calm.dsl.builtins import Substrate, readiness_probe, read_provider_spec, ref, action, CalmTask

from base_vm import UbuntuAhvVM


class NginxSubstrace(Substrate):
    """CentOS substrate"""

    provider_spec = UbuntuAhvVM




