import os
import yaml

def get_mco_operator():
    '''
    :return: Return true if the mco operator was installed
    '''
    mco_operator=os.popen('oc get mco --no-headers --ignore-not-found').read().strip('\n')
    if mco_operator == '':
        return True
    else:
        return False