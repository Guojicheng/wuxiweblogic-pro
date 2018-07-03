#!/usr/bin/python
# Save Script as : enable_ssh_server.py 

import time
import getopt
import sys
import re
import os
import random
import string
import socket
# Deployment Information 
domainhome = os.environ.get('DOMAIN_HOME', '/wxgl/weblogic/user_projects/domains/base_domain')
admin_username = os.environ.get('ADMIN_USERNAME', 'weblogic')
admin_password = os.environ.get('base_domain_default_password') 
admin_port     = os.environ.get('AdminPort', '7001')
msSSLPort = os.environ.get('sslport', '7002')

def editMode():
    edit()
    startEdit(waitTimeInMillis=-1, exclusive="true")

def saveActivate():
    save()
    activate(block="true")

def connectToAdmin():
     connect(admin_username,admin_password,url='t3://' + 'localhost' + ':' + admin_port)


# Connect to the AdminServer
# ==========================
connectToAdmin()
print 'Connected to Admin Server' + '\n'


edit()
startEdit()

# set keystore infomation.
cd('/Servers/AdminServer')
cmo.setKeyStores('CustomIdentityAndCustomTrust')

activate()

startEdit()

cmo.setKeyStores('CustomIdentityAndCustomTrust')
cmo.setCustomIdentityKeyStoreFileName('/home/weblogic/server.jks')
cmo.setCustomIdentityKeyStoreType('jks')
set('CustomIdentityKeyStorePassPhrase','111111')
cmo.setCustomTrustKeyStoreFileName('/home/weblogic/serverjks')
cmo.setCustomTrustKeyStoreType('jks')
set('CustomTrustKeyStorePassPhrase','111111')

activate()

startEdit()
# Enable SSL. Attach the keystore later.
cd('/Servers/AdminServer/SSL/AdminServer')
cmo.setEnabled(true)
cmo.setListenPort(int(msSSLPort))
cmo.setServerPrivateKeyAlias('serverkey')
set('ServerPrivateKeyPassPhrase','changeit')
cmo.setHostnameVerificationIgnored(true)
cmo.setHostnameVerifier(None)
cmo.setTwoWaySSLEnabled(false)
cmo.setClientCertificateEnforced(false)
cmo.setJSSEEnabled(true)




save()
activate()

disconnect()
exit()
