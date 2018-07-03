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
admin_port     = os.environ.get('AdminPort', '8001')

# Datasource Information
# =======================
dsName=os.environ.get('DATASOURCE_NAME')
dsJNDIName=os.environ.get('JNDI_NAME')
dbhost1 = os.environ.get('DATABASE_HOST')
if (dbhost1 is not None):
  dsURL =  'jdbc:oracle:thin:@' + dbhost1
dsDriver = 'oracle.jdbc.xa.client.OracleXADataSource'
dsUsername = os.environ.get('DATABASE_USERNAME')
dsPassword = os.environ.get('DATABASE_PASSWORD')
dsTargetType = 'Cluster'
dsTargetName = os.environ.get("CLUSTER_NAME", "WebLogicCluster")

# Display the variable values.
print 'dsName=', dsName
print 'dsJNDIName=', dsJNDIName
print 'dsURL=', dsURL
print 'dsDriver=', dsDriver
print 'dsUsername=', dsUsername
print 'dsPassword=', dsPassword
print 'dsTargetType=', dsTargetType
print 'dsTargetName=', dsTargetName


#execfile('/wxgl/weblogic/weblogicinstall/ManagedServer.properties')
# Function
def editMode():
    edit()
    startEdit(waitTimeInMillis=-1, exclusive="true")

def saveActivate():
    save()
    activate(block="true")

def connectToAdmin():
     connect(admin_username,admin_password,url='t3://' + 'AdminServer1' + ':' + admin_port)


# Connect to the AdminServer
# ==========================
connectToAdmin()
print 'Connected to Admin Server' + '\n'

# Change to Edit Mode
# ======================
edit()
startEdit()

# Get the Server Target
# ======================
cd('/')
cmo.createJDBCSystemResource(dsName)

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName)
cmo.setName(dsName)

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDataSourceParams/' + dsName)
set('JNDINames',jarray.array([String(dsJNDIName)], String))

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName)
cmo.setUrl(dsURL)
cmo.setDriverName(dsDriver)
set('Password', dsPassword)
cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCConnectionPoolParams/' + dsName)
cmo.setTestTableName('SQL SELECT 1 FROM DUAL\r\n\r\n')

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName)
cmo.createProperty('user')

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName + '/Properties/user')
cmo.setValue(dsUsername)

cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDataSourceParams/' + dsName)
cmo.setGlobalTransactionsProtocol('TwoPhaseCommit')

cd('/SystemResources/' + dsName)
set('Targets',jarray.array([ObjectName('com.bea:Name=' + dsTargetName + ',Type=' + dsTargetType)], ObjectName))

save()
activate()

disconnect()
exit()

print 'Completed JNDI created.' + '\n'

