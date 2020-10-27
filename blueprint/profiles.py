from calm.dsl.builtins import Profile, CalmVariable

from deployments import NginxDeployment


class AHV(Profile):

    deployments = [NginxDeployment]

    PRISM_IP = CalmVariable.Simple('10.38.11.9', name='PRISM_IP', label='Prism IP Address',
                                   is_mandatory=True, runtime=True)
    PRISM_PORT = CalmVariable.Simple('9440', name='PRISM_PORT', label='Prism Port',
                                     is_mandatory=True, runtime=True)



