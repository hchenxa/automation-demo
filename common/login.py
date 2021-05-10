import os

def login_with_token(url, token):
    '''
    Login the OCP cluster with token
    '''
    os.system('oc login --server ' + url + '--token ' + token)

def login_with_username(url, user, passwd):
    '''
    Login the OCP cluster with username and password
    '''
    os.system('oc login --server ' + url + '-u ' + user + '-p ' + passwd)