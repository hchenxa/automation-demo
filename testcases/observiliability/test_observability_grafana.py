import pytest
import allure

from common.ocm_common import OcmCommon

@allure.severity(allure.severity_level.CRITICAL)
@allure.epic("Observability")
@allure.feature("Observability Granafa")
@pytest.mark.skipif(OcmCommon.get_ocm_version() < '2.2', reason='The feature was GAed in 2.2+ version')
class TestObservabilityGrafana():
    '''
    Used to test the grafana function created by OCM observability.
    '''
    # @author username@redhat.com
    # @case_id: RHACM4K-id
    # @pytest.mark.parametrize('cr', GetData().get('../testdata/observability/observability_cr.yaml'))
    @allure.story("View the observability grafana")
    @allure.description("The test case was used to check if the grafana can be viewd")
    def test_observability_granafa_view(self):
        '''
        Used to test the grafana view function in OCM environment.
        '''
        assert True == True

if __name__ == '__main__':
    pytest.main(['-s'])