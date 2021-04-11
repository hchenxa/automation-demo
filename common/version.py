import commands
import yaml

def get_openshift_version():
    """
    :return: Returns the current openshift server version
    """
    version_output = commands.getoutput('oc version -o yaml')
    data = yaml.load(version_output, Loader=yaml.FullLoader)
    client_version = data.get('clientVersion').get('gitVersion')
    openshift_version = data.get('openshiftVersion')
    kube_version = data.get('serverVersion').get('gitVersion')

    return client_version, openshift_version, kube_version

def get_acm_version(namespace):
    '''
    :return: 
    '''
    # Hard code 2.2 here and will return the real ocm version later
    acm_version = commands.getoutput('oc get csv -n ' + namespace + ' --no-headers | awk \'{print $7}\' ')
    return acm_version