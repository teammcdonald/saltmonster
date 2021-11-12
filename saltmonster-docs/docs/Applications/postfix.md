# Postfix

### Clear the postfix queue
 
``` bash
# postsuper -d ALL
 ```

### Restrict mail destinations

Edit /etc/postfix/transport with the allowed destinations
``` bash
johnsmith@company.com :
* discard:
```

Create the hash db
``` bash
# postmap /etc/postfix/transport
 ```

Edit /etc/postfix/main.cf to add the defaults
``` bash
# Company Specific
relayhost = mailrelay.company.com
mydomain = domain.company.com
transport_maps = hash:/etc/postfix/transport
```

Restart postfix
``` bash
# systemctl restart postfix
```
