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

Update dns order
```bash
#  nmcli conn modify "System eth0" ipv4.dns  "10.10.12.100,10.12.12.100"
```

Restart Network Manager (for changes to take effect)
```bash
# systemctl restart NetworkManager
```
