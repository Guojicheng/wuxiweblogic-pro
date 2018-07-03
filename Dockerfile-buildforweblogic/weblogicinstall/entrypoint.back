#!/bin/bash -x
# update config file for applictions 
 
#sudo svn checkout ${SVN_URL} /home/weblogic/ --username ${SVN_USERNAME} --password   ${SVN_PASSWORD} --no-auth-cache

#cp -f /home/weblogic/jdbc.properties  ${APP_PATH_1}/WEB-INF/classes/conf/sqlmap/jdbc.properties  \
#   && cp -f /home/weblogic/eservice.js  ${APP_PATH_1}/front/js/eservice.js  \
#   && cp -f /home/weblogic/common.properties  ${APP_PATH_1}/WEB-INF/classes/common.properties

# Update the create-wls-domain.py file
/bin/sed -i "s/^.*cmo.setPassword.*$/cmo.setPassword('${base_domain_default_password}')/" /wxgl/weblogic/weblogicinstall/create-wls-domain.py
#/bin/sed -i "s/^.*ListenAddress.*$/set('ListenAddress','${SELF_IP}')/" /wxgl/weblogic/weblogicinstall/create-wls-domain.py
/bin/sed -i "s/^.*ListenPort.*$/set('ListenPort',${AdminPort})/" /wxgl/weblogic/weblogicinstall/create-wls-domain.py

# Init the base domain
startfile="/wxgl/weblogic/user_projects/domains/base_domain/startWebLogic.sh"
if [ ! -f "$startfile" ] 
then
    /wxgl/weblogic/wlserver_10.3/common/bin/wlst.sh -skipWLSModuleScanning /wxgl/weblogic/weblogicinstall/create-wls-domain.py
fi
##################################################################################################################
# Start Weblogic Server , Admin Server

if [ "$Server_Role" = 'Admin' ] &&  [ ! -f /wxgl/weblogic/weblogicinstall/.passwordseted ]; then
  mkdir -p /wxgl/weblogic/user_projects/domains/base_domain/servers/AdminServer/security/
  echo "username=weblogic" >> /wxgl/weblogic/user_projects/domains/base_domain/servers/AdminServer/security/boot.properties
  echo "password=${base_domain_default_password}" >> /wxgl/weblogic/user_projects/domains/base_domain/servers/AdminServer/security/boot.properties
  touch /wxgl/weblogic/weblogicinstall/.passwordseted
fi
if [ "$Server_Role" = 'Admin' ]; then
export USER_MEM_ARGS="-Xms1024m -Xmx1024m -Xmn768m -XX:MaxPermSize=512m -XX:+UseConcMarkSweepGC -XX:+HeapDumpOnOutOfMemoryError -verbose:gc -Xloggc:./logs/USSDappserver1_gc.out -XX:+PrintGCDetails -XX:+PrintGCTimeStamps -Dweblogic.threadpool.MinPoolSize=100 -Dweblogic.threadpool.MaxPoolSize=300"  
  /wxgl/weblogic/weblogicinstall/createapp.sh &
  /wxgl/weblogic/user_projects/domains/base_domain/startWebLogic.sh &
fi
sleep 30
if [ "$Server_Role" = 'Admin' ] && [ ! -f /wxgl/weblogic/weblogicinstall/.ssLenabled ]; then
 /wxgl/weblogic/wlserver_10.3/common/bin/wlst.sh -skipWLSModuleScanning /wxgl/weblogic/weblogicinstall/enable_ssl_server.py
 touch /wxgl/weblogic/weblogicinstall/.ssLenabled
 sleep 15
 /wxgl/weblogic/user_projects/domains/base_domain/bin/stopWebLogic.sh
 /wxgl/weblogic/user_projects/domains/base_domain/startWebLogic.sh
fi

