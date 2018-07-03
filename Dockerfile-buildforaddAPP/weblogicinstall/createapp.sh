#!/bin/bash -x
while [ ! -f /wxgl/weblogic/weblogicinstall/.ssLenabled ]; do
  echo " managernode need time to runnning"
  sleep 15
done 
echo " now to deploy application use wlst script online mode"

sleep 50
if [ "$Server_Role" = 'Admin' ] && [ $DATASOURCE_NAME ] && [ ! -f /wxgl/weblogic/weblogicinstall/.datasourceset ]; then
 echo 'DATA SOURCE provided and not set. Start configuring Data Source ...'
 /wxgl/weblogic/wlserver_10.3/common/bin/wlst.sh -skipWLSModuleScanning /wxgl/weblogic/weblogicinstall/create-datasourceonline.py
 touch /wxgl/weblogic/weblogicinstall/.datasourceset
 sleep 20
 echo "weblogic Datasource 1 configuration test passed "
fi

if [ "$Server_Role" = 'Admin' ] && [ $DATASOURCE_NAME_2 ] && [ ! -f /wxgl/weblogic/weblogicinstall/.datasourceset2 ]; then
 echo 'DATA SOURCE provided and not set. Start configuring Data Source ...'
 /wxgl/weblogic/wlserver_10.3/common/bin/wlst.sh -skipWLSModuleScanning /wxgl/weblogic/weblogicinstall/create-datasourceonline2.py
 touch /wxgl/weblogic/weblogicinstall/.datasourceset2
sleep 20
echo "weblogic Datasource 2 configuration test passed "
fi


if [ "$Server_Role" = 'Admin' ] && [ ! -f /wxgl/weblogic/weblogicinstall/.deployed ]; then
/wxgl/weblogic/wlserver_10.3/common/bin/wlst.sh -skipWLSModuleScanning /wxgl/weblogic/weblogicinstall/deploy-application.py
touch /wxgl/weblogic/weblogicinstall/.deployed
sleep 20
echo "weblogic app configuration test passed "
fi


