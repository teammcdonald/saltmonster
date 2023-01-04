# Duo

### Duo Installation

1. Install Duo software
    ```bash
    # yum install duo_unix
    ```
2. Update  /etc/duo/login_duo.conf with the following :
    ```bash
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
    ```
3. Update /etc/ssh/sshd_config with the following  :
    ``` bash
    #require tfa auth
    ForceCommand /usr/sbin/login_duo
    PermitTunnel no
    AllowTcpForwarding no
    ```
4. Restart sshd
    ``` bash
    # systemctl restart sshd
    ```
5. Test
