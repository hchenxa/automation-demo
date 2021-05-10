import os
import yaml

def get_openshift_version():
    '''
    :return: Returns the current openshift server version
    '''
    version_output = os.popen('oc version -o yaml').read()
    data = yaml.load(version_output, Loader=yaml.FullLoader)
    client_version = data.get('clientVersion').get('gitVersion')
    openshift_version = data.get('openshiftVersion')
    kube_version = data.get('serverVersion').get('gitVersion')

    return client_version, openshift_version, kube_version

def get_acm_version():
    '''
    :return: Returns the acm version
    '''
    namespace = get_installed_namespace()
    acm_version = os.popen('oc get csv -n ' + namespace + ' --no-headers | awk \'{print $7}\' ').read().strip('\n')
    return acm_version

def get_installed_namespace():
    '''
    :return: Returns the acm installed namespace
    '''
    installed_ns = os.popen('oc get csv --all-namespaces --no-headers | grep advanced-cluster-management  | awk \'{print $1}\'').read().strip('\n')
    return installed_ns

def get_cloud_provider():
    '''
    :return: Returns the hub cluster cloud provider type
    '''
    inf_output = os.popen('oc get infrastructures.config.openshift.io cluster -o yaml').read()
    data = yaml.load(inf_output, Loader=yaml.FullLoader)
    cloud_provider_type = data.get('status').get('platform')
    return cloud_provider_type