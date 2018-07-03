FROM  10.3.16.213/wechat/weblogicnoapptest1 

CMD ["/wxgl/weblogic/weblogicinstall/entrypoint.sh"] 
ADD  Application/*  /applications/
RUN  chown -R weblogic:weblogic /applications \
     && chmod -R 0777 /applications \
     && chown -R weblogic:weblogic /wxgl/weblogic 
USER weblogic
