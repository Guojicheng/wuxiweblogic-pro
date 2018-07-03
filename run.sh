docker run -itd \
 -p 7001:7001 \
 -p 7002:7002 \
 -e Server_Role=Admin \
 -e ADMIN_USERNAME=weblogic \
 -e AdminPort=7001  \
 -e sslport=7002 \
 -e base_domain_default_password=999999999 \
 -e APP_NAME_1='Gllic_wx'  \
 -e APP_PATH_1='/applications/Gllic_wx' \
 -e SVN_URL='svn://10.4.12.48/davesvn/code/config/uat ' \
 -e SVN_USERNAME=yanglu \
 -e SVN_PASSWORD=yanglu \
10.3.16.213/wechat/weblogicaddapptest1 /bin/bash
