FROM  centos6.8svnbase  
MAINTAINER jicheng <guojc@wise2c.com>
# 编码设置
ENV LANG=en_US.UTF-8  \
    LANGUAGE=en_US:en  \
    LC_ALL=en_US.UTF-8
#查看语言支持列表
RUN localedef --list-archive    #精简locale  \
  && cd /usr/lib/locale/  && mv locale-archive locale-archive.old  && localedef -i en_US -f UTF-8 en_US.UTF-8  # 添加中文支持（可选） \   
  && localedef -i zh_CN -f UTF-8 zh_CN.UTF-8  && localedef -i zh_CN -f GB2312 zh_CN  && localedef -i zh_CN -f GB2312 zh_CN.GB2312 && localedef -i zh_CN -f GBK zh_CN.GBK \#下面这些也是可选的，可以>丰富中文支持（香港/台湾/新加坡）\
  && localedef -f UTF-8 -i zh_HK zh_HK.UTF-8 && localedef -f UTF-8 -i zh_TW zh_TW.UTF-8  && localedef -f UTF-8 -i zh_SG zh_SG.UTF-8  && localedef -i zh_CN -f GB18030 zh_CN.GB18030  \
  && mkdir -p /wxgl/weblogic  
RUN  groupadd weblogic && useradd -g weblogic weblogic && echo "weblogic:weblogic" | chpasswd \
  && curl -o sudo-1.8.6p3-27.el6.x86_64.rpm  http://192.168.2.141:81/weblogic/sudo-1.8.6p3-27.el6.x86_64.rpm  \
  && rpm -ivh sudo-1.8.6p3-27.el6.x86_64.rpm \
  && rm -rf sudo-1.8.6p3-27.el6.x86_64.rpm \
  && echo "weblogic ALL=(ALL) NOPASSWD:ALL" >>/etc/sudoers 
COPY weblogicinstall/* /wxgl/weblogic/weblogicinstall/  
WORKDIR /home/weblogic/
COPY keydir/*  /home/weblogic/
RUN  mkdir -p /wxgl/weblogic/beainstall  \
 &&  chmod -R 755 /wxgl/weblogic/  \
 &&  curl -o jdk-6u45-linux-x64.bin http://192.168.2.141:81/weblogic/jdk-6u45-linux-x64.bin  \
 &&  chmod a+x  jdk-6u45-linux-x64.bin  \
 &&  /bin/bash ./jdk-6u45-linux-x64.bin  \
 &&  mv jdk1.6.0_45 /wxgl/weblogic/jdk1.6.0_45 \
 &&  rm -rf jdk-6u45-linux-x64.bin \ 
 &&  chown -R weblogic:weblogic /home/weblogic 

ENV JAVA_HOME /wxgl/weblogic/jdk1.6.0_45/  \
    CLASSPATH ".:/wxgl/weblogic/jdk1.6.0_45/lib/dt.jar:$JAVA_HOME/lib/tools.jar" \
    PATH   $PATH:/wxgl/weblogic/jdk1.6.0_45/bin  

# install weblogic for slient mode , and create domain

RUN curl -o wls1036_generic.jar http://192.168.2.141:81/weblogic/wls1036_generic.jar  &&  chmod -R 755 /wxgl/weblogic && /wxgl/weblogic/jdk1.6.0_45/bin/java  -jar wls1036_generic.jar -mode=silent -silent_xml=/wxgl/weblogic/weblogicinstall/silent.xml -log=/wxgl/weblogic/weblogicinstall/silent.log   &&  rm wls1036_generic.jar /wxgl/weblogic/weblogicinstall/silent.xml && rm -rf wls1036_generic.jar && chown -R weblogic:weblogic /wxgl/  &&  chmod -R 0777 /wxgl/

##  变量设置 （快速登录界面）
ENV JAVA_OPTIONS="-Dweblogic.security.SSL.ignoreHostnameVerification=true -Djava.security.egd=file:///dev/urandom" \
    CONFIG_JVM_ARGS='-Djava.security.egd=file:/dev/./urandom'  \
    Server_Role=Admin \
    ADMIN_USERNAME=weblogic \
    AdminPort=7001 \
    sslport=7002 \
    base_domain_default_password=999999999 \
    APP_NAME_1='Gllic_wx' \
    APP_PATH_1='/applications/Gllic_wx' \
    SVN_URL='svn://10.4.12.48/davesvn/code/config/uat' \
    SVN_USERNAME=yanglu \
    SVN_PASSWORD=yanglu

## 创建domain
RUN /wxgl/weblogic/wlserver_10.3/common/bin/wlst.sh -skipWLSModuleScanning /wxgl/weblogic/weblogicinstall/create-wls-domain.py 


## 登录不输入密码

RUN mkdir -p /wxgl/weblogic/user_projects/domains/base_domain/servers/AdminServer/security/  &&  sudo echo "username=weblogic" >> /wxgl/weblogic/user_projects/domains/base_domain/servers/AdminServer/security/boot.properties  && sudo echo "password=999999999" >> /wxgl/weblogic/user_projects/domains/base_domain/servers/AdminServer/security/boot.properties && touch /wxgl/weblogic/weblogicinstall/.passwordseted  && chown -R weblogic:weblogic /wxgl/weblogic/user_projects/domains/base_domain/servers/AdminServer/security/ 

## 启动参数

RUN export USER_MEM_ARGS="-Xms1024m -Xmx1024m -Xmn768m -XX:MaxPermSize=512m -XX:+UseConcMarkSweepGC -XX:+HeapDumpOnOutOfMemoryError -verbose:gc -Xloggc:./logs/USSDappserver1_gc.out -XX:+PrintGCDetails -XX:+PrintGCTimeStamps -Dweblogic.threadpool.MinPoolSize=100 -Dweblogic.threadpool.MaxPoolSize=300"  

## 启动修改ssl 

RUN   /wxgl/weblogic/weblogicinstall/createssl.sh  && sleep 12

#CMD ["/wxgl/weblogic/weblogicinstall/entrypoint.sh"] 
#COPY Application  /applications/
#RUN  chown -R weblogic:weblogic /applications \
#     && chmod -R 0777 /applications 
#USER weblogic
