import pytest
import allure

from common import resources, observability

@allure.severity(allure.severity_level.CRITICAL)
@allure.epic("Observability Core")
@pytest.mark.skipif(resources.get_acm_version() < '2.2', reason='The feature was GAed in 2.2+ version')
class TestObservabilityMetrics():
    '''
    Used to test the grafana function created by OCM observability.
    '''
    # @author huichen@redhat.com
    # @case_id: RHACM4K-1658
    # @pytest.mark.parametrize('cr', GetData().get('../testdata/observability/observability_cr.yaml'))
    @allure.feature("RHACM4K-1658")
    @allure.story("Customized metrics data to be collected")
    @allure.description("Customized metrics data to be collected")
    def test_observability_customized_metrics(self):
        '''
        Used to test customized metrics for observability.
        '''
        # Step1: verify the MCO
        mco_operator=observability.get_mco_operator()
        assert mco_operator == True
        # Step2: Create the customized configmap
        
        # Step3: Verify the new metrics of node_memory_Active_bytes
        # Step4: Add another metrics in configmap
        # Step5: Verify the new metrics
        # Step6: Delete the configmap  

if __name__ == '__main__':
    pytest.main()