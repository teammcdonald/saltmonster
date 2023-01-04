# Duo

### Duo Installation

1. Install Duo software

        # dnf install duo_unix

2. Update  /etc/duo/login_duo.conf with the following :

        [duo]
        ; Duo integration key
        ikey = {integration key}
        ; Duo secret key
        skey ={secret key}
        ; Duo API host
        host = api-{api-host}.duosecurity.com
        ; Send command for Duo Push authentication
        ;pushinfo = yes
        accept_env_factor = yes
        failmode = safe
        groups = *,!root
        autopush = yes

3. Update /etc/ssh/sshd_config with the following  :

        #require tfa auth
        ForceCommand /usr/sbin/login_duo
        PermitTunnel no
        AllowTcpForwarding no

4. Restart sshd

        # systemctl restart sshd

5. Test



* Account must created at duo.com
* {integration key},{secret key} and {api-host} will come from the applications tab on your dashboard 