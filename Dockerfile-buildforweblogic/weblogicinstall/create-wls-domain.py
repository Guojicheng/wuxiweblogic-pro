# Default domain 'base_domain' to be created inside the Docker image for WLS
# ==============================================

# Open default domain template
# ======================
readTemplate("/wxgl/weblogic/wlserver_10.3/common/templates/domains/wls.jar")
# Configure the Administration Server and SSL port.
# =========================================================
cd('Servers/AdminServer')
set('ListenAddress','')
set('ListenPort',7001)
# Define the user password for weblogic
# =====================================
cd('/')
cd('Security/base_domain/User/weblogic')
cmo.setPassword('999999999')
# Write the domain and close the domain templat
# ==============================================
setOption('OverwriteDomain', 'true')
setOption('ServerStartMode', 'prod')
writeDomain('/wxgl/weblogic/user_projects/domains/base_domain')
closeTemplate()
# Exit WLST
# =========
exit()
