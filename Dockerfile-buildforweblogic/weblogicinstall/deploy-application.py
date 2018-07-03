# Copyright (c) 2015 Oracle and/or its affiliates. All rights reserved.
#
# WLST Offline for deploying an application under APP_NAME packaged in APP_PKG_FILE located in APP_PKG_LOCATION
# It will read the domain under DOMAIN_HOME by default
#
# author: Bruno Borges <bruno.borges@oracle.com>
# since: December, 2015
#
import os
import random
import string
import socket
# Deployment Information 
domainhome = os.environ.get('DOMAIN_HOME', '/wxgl/weblogic/user_projects/domains/base_domain')
cluster_name = os.environ.get("CLUSTER_NAME", "WebLogicCluster")
admin_username = os.environ.get('ADMIN_USERNAME', 'weblogic')
admin_password = os.environ.get('base_domain_default_password') 
admin_port     = os.environ.get('AdminPort', '7001')

# Application Information
# =======================
appname1 = os.environ.get('APP_NAME_1')
apppath1 = os.environ.get('APP_PATH_1')
appname2 = os.environ.get('APP_NAME_2')
apppath2 = os.environ.get('APP_PATH_2')


#execfile('/wxgl/weblogic/weblogicinstall/ManagedServer.properties')
# Function
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

# Change to Edit Mode
# ======================
#edit()
#startEdit()

# Get the Server Target
# ======================
#cd('/')
#cd('/Servers/' + msname)
#self=cmo

# AppDeployments
# ======================
if (appname1 is not None) and (apppath1 is not None) and os.path.exists(str(apppath1)):
  print 'Start deploying the first application ' + appname1  +  '\n' 
  deploy(appname1, apppath1, stageMode='nostage')
  startApplication(appname1)

#save()

if (appname2 is not None) and (apppath2 is not None) and os.path.exists(str(apppath2)):
  print 'Start deploying the first application ' + appname1  +  '\n'
  deploy(appname2, apppath2, stageMode='nostage')
  startApplication(appname2)

#save()

#activate()

print 'Completed JNDI and Application modification.' + '\n'

disconnect()
exit()
