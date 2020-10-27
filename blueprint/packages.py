from calm.dsl.builtins import Package, CalmTask, action, ref

from services import Nginx


class NginxPackage(Package):
    """DemoApp package"""
    services = [ref(Nginx)]

    @action
    def __install__(self):
        CalmTask.Exec.ssh(name='update centos', filename='scripts/install_nginx.sh')



