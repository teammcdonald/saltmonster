# Miscellaneous Linux Stuff

###  Getting uuid

```bash
# blkid
```

### Set old kernel count 

```bash
# package-cleanup --oldkernels --count=2
```

To permantly set, change yum.conf and modify the line below

```bash
installonly_limit=2
```