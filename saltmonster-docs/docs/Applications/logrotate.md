# Logrotate

### Important Files
> /etc/logrotate.conf - main configuration file 

> /etc/logrotate.d/ - individual configuration files 

> /var/lib/logrotate/logrotate.status - logrotate state file



### Commands

> logrotate -d /etc/logrotate.conf - debug (what would happen but don't do it)

> logrotate -df /etc/logrotate.d/nginx - what would happen if you forced a logrotate on the nginx configuration file

