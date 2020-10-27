from calm.dsl.builtins import Deployment, ref

from packages import NginxPackage
from substrates import NginxSubstrace


class NginxDeployment(Deployment):

    min_replicas = '1'
    max_replicas = '1'

    packages = [ref(NginxPackage)]
    substrate = ref(NginxSubstrace)


