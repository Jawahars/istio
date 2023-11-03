import sh
import yaml
from utils import microk8s_enable, wait_for_pod_state, microk8s_disable

class TestAddons(object):
    def test_istio(self):
        microk8s_enable("istio")
        wait_for_pod_state("", "default", "running", label="app=python-demo-nginx")
        status = yaml.safe_load(sh.microk8s.status(format="yaml").stdout)
        expected = {"istio": "enabled"}
        microk8s_disable("istio")