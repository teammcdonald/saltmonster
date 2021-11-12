# Sudoers

### /etc/sudoers

The /etc/sudoers file is standard across environments and OS's.

```bash
#
# Config for sudoers files
#
#

Defaults   !visiblepw
Defaults    env_reset
Defaults    requiretty
Defaults    use_pty
Defaults    env_keep = "COLORS DISPLAY HOSTNAME HISTSIZE INPUTRC KDEDIR \
                        LS_COLORS MAIL PS1 PS2 QTDIR USERNAME \
                        LANG LC_ADDRESS LC_CTYPE LC_COLLATE LC_IDENTIFICATION \
                        LC_MEASUREMENT LC_MESSAGES LC_MONETARY LC_NAME LC_NUMERIC \
                        LC_PAPER LC_TELEPHONE LC_TIME LC_ALL LANGUAGE LINGUAS \
                        _XKB_CHARSET XAUTHORITY"
Defaults    secure_path = /sbin:/bin:/usr/sbin:/usr/bin
Defaults    logfile=/var/log/sudo.log
Defaults    lecture="once"

root	ALL=(ALL) 	ALL

#includedir /etc/sudoers.d/
```

It is git managed.

The sudoers.d contains the files that our specific to environment/application.


