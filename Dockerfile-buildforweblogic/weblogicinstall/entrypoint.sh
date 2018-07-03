#!/bin/bash -x
# update config file for applictions 
 
sudo svn checkout ${SVN_URL} /home/weblogic/ --username ${SVN_USERNAME} --password   ${SVN_PASSWORD} --no-auth-cache

cp -f /home/weblogic/jdbc.properties  ${APP_PATH_1}/WEB-INF/classes/conf/sqlmap/jdbc.properties  \
   && cp -f /home/weblogic/eservice.js  ${APP_PATH_1}/front/js/eservice.js  \
   && cp -f /home/weblogic/common.properties  ${APP_PATH_1}/WEB-INF/classes/common.properties

##################################################################################################################
# Start Weblogic Server , Admin Server

if [ "$Server_Role" = 'Admin' ]; then
export USER_MEM_ARGS="-Xms1024m -Xmx1024m -Xmn768m -XX:MaxPermSize=512m -XX:+UseConcMarkSweepGC -XX:+HeapDumpOnOutOfMemoryError -verbose:gc -Xloggc:./logs/USSDappserver1_gc.out -XX:+PrintGCDetails -XX:+PrintGCTimeStamps -Dweblogic.threadpool.MinPoolSize=100 -Dweblogic.threadpool.MaxPoolSize=300"  
  /wxgl/weblogic/weblogicinstall/createapp.sh &
  /wxgl/weblogic/user_projects/domains/base_domain/startWebLogic.sh 
fi

