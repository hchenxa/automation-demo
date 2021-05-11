import os

def create_with_clusterscope(name):

def create(filepath, namespace):
    '''
    Create the resources from filepath
    '''
    os.system('oc create -f ' + filepath + '-n ' + namespace)

def update(filepath, namespace):
    '''
    Apply the resources from filepath
    '''
    os.system('oc apply -f ' + filepath + '-n ' + namespace)

def delete(filepath, namespace):
    '''
    Delete the resources from filepath
    '''
    os.system('oc delete -f ' + filepath + '-n ' + namespace)

def view(name, namespace):

def query_with_selector(namespace, selector):