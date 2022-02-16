# AIX

### It's not unix

Clear wtmp

```bash
# /usr/sbin/acct/nulladm /var/adm/wtmp
```

Allow LDAP/AD users to have local groups

```bash
# chsec -f /etc/secvars.cfg -s groups -a domainlessgroups=true
```