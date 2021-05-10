import pytest
import allure

from common.resources import get_acm_version

@allure.severity(allure.severity_level.CRITICAL)
@allure.epic("Observability")
@allure.feature("Observability Granafa")
@pytest.mark.skipif(get_acm_version() < '2.2', reason='The feature was GAed in 2.2+ version')
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
        version = get_acm_version()
        print(version)
        assert version=='2.2'

if __name__ == '__main__':
    pytest.main()