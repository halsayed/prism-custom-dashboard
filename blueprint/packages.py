from calm.dsl.builtins import Package, CalmTask, action, ref

from services import Nginx


class NginxPackage(Package):
    """DemoApp package"""
    services = [ref(Nginx)]

    @action
    def __install__(self):
        CalmTask.Exec.ssh(name='update ubuntu', filename='scripts/install_docker.sh')




