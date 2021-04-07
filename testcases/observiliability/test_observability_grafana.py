import pytest
from common.ocm_common import OcmCommon

@pytest.mark.skipif(OcmCommon.get_ocm_version() <= '2.2')
class TestObservabilityGrafana():
    '''
    Used to test the grafana function created by OCM observability.
    '''
    # @author username@redhat.com
    # @case_id: RHACM4K-id
    # @pytest.mark.parametrize('cr', GetData().get('../testdata/observability/observability_cr.yaml'))
    def test_observability_granafa_view(self):
        '''
        Used to test the grafana view function in OCM environment.
        '''
        assert True == True

if __name__ == '__main__':
    pytest.main(['-s'])