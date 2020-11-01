from calm.dsl.builtins import Package, CalmTask, action, ref

from services import Nginx


class NginxPackage(Package):
    """DemoApp package"""
    services = [ref(Nginx)]

    @action
    def __install__(self):
        CalmTask.Exec.ssh(name='Prepare Centos', filename='scripts/prepare_centos.sh')
        CalmTask.Exec.ssh(name='Install docker', filename='scripts/install_docker.sh')
        CalmTask.Exec.ssh(name='Install custom login app', filename='scripts/install_custom_login_app.sh')





