from calm.dsl.builtins import Package, CalmTask, action, ref

from services import Nginx


class NginxPackage(Package):
    """DemoApp package"""
    services = [ref(Nginx)]

    @action
    def __install__(self):
        CalmTask.Exec.ssh(name='update ubuntu', filename='scripts/update_ubuntu.sh')
        CalmTask.Exec.ssh(name='install docker compose', filename='scripts/install_docker_compose.sh')




