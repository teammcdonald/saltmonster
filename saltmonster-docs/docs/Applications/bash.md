# Bash

### Useful one liners

##### du of only local file systems in root

AIX
```bash
# mount > mounts.txt
# for d in /*; do egrep " ${d} " mounts.txt > /dev/null || du -sg ${d}; done
```

Linux
```bash
# for d in /*; do egrep " ${d} " /proc/mounts > /dev/null || du -sh ${d}; done
```

