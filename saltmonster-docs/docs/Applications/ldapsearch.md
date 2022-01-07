# Ldapsearch

### Example search with paging

> ldapsearch  -E pr=10000/noprompt  -b "DC=ldap,DC=com" -h ldapquery.ldap.com -D ${USER} -w ${PASS} "(samaccountname=*)" samaccountname 
