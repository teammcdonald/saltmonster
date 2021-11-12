# Ldap

### AD Attributes Required for Posix compliance (Linux/Solaris/AIX)
The following attributes are required in Active Directory by unix/linux systems for users to be recognized as valid to the OS.  Where applicable, I added the default value for new accounts.


AD Attribute | Default Value
-------------|--------------
sn | Last Name
uid | This should be login name
uidNumber | This should be unique
gidNumber | Default value of uidNumber
loginShell | Default value of /bin/bash
unixHomeDirectory | Default value of /home/{uid}
gecos | Usually fullname or email


The following attributes required in Active Directory by unix/linux systems for groups to be recognized as valid to the OS.

AD Attribute | Note 
-------------|-------------
gidNumber | The value must be unique

