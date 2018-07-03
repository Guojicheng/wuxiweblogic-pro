#!/bin/bash -x

/usr/bin/nohup /wxgl/weblogic/user_projects/domains/base_domain/startWebLogic.sh & 
sleep 50 
/wxgl/weblogic/wlserver_10.3/common/bin/wlst.sh -skipWLSModuleScanning /wxgl/weblogic/weblogicinstall/enable_ssl_server.py  
echo "ssl configed , please have a little time "
sleep 10
/wxgl/weblogic/user_projects/domains/base_domain/bin/stopWebLogic.sh
