from calm.dsl.builtins import Substrate, readiness_probe, read_provider_spec, ref, action, CalmTask

from base_vm import CentOSAhvVM
from vars import CENTOS_CRED


class NginxSubstrace(Substrate):
    """CentOS substrate"""

    provider_spec = CentOSAhvVM




