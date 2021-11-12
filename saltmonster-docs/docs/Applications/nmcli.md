# Nmcli

### DNS Search

Check dns search 
``` bash
# nmcli con show 'System eth0' | grep ipv4.dns-search
```

Update dns search
``` bash
# nmcli con mod "System eth0" ipv4.dns-search "mi.company.com company.com"
```
