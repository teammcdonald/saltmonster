#SSH

###SSH Key Creation

Objective to provide secure seemless access to servers.

1. Log on to the client you wish to ssh from.
2. Create a key pair on the client (From)
>$ ssh-keygen -t rsa -b 4096
Generating public/private rsa key pair.
Enter file in which to save the key (/home/user/.ssh/id_rsa): ENTER
Enter passphrase (empty for no passphrase): ENTER
Enter same passphrase again: ENTER
Your identification has been saved in /home/user/.ssh/id_rsa.
Your public key has been saved in /home/user/.ssh/id_rsa.pub.
The key fingerprint is:
79:f5:a2:cf:72:40:bb:30:3c:e3:c1:9e:36:9c:19:71 user@hostname
3. Copy the key created in ~/.ssh/id_rsa.pub to ~/.ssh/authorized_keys
> $ cp ~/.ssh/id_rsa.pub ~/.ssh/authorized_keys
4. Test

###SSH Key Maintenance

Remove an old key from your known_hosts

```bash
# ssh-keygen -R _hostname_
```

Add a new key to your known_hosts

```bash
# ssh-keyscan _hostname_ >> ~/.ssh/known_hosts
```

### SSH - Check Crypto

'''nmap -Pn -n -p22 -vv --open --script=ssh2-enum-algos.nse hostname```
