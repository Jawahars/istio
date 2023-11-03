import sh
import yaml

from utils import microk8s_enable, wait_for_pod_state, microk8s_disable


class TestAddons(object):
    def test_istio(self):
        pass

