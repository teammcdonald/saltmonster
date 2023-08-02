#AWK

###Examples :

Print if the second to last column is greater than 1

```bash
# grep 11:23 filename  | awk ' $(NF-1) >1{print $(NF-1),$7}'
```

Print the second to last column 

```bash
# awk '{for (i=2; i<NF; i++) printf $i " "; print $NF}' filename
```
```bash
# awk `{$1=""; print $0}' filename
```
