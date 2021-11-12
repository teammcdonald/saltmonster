# Sed

### Strip html code

``` bash
# curl  https://server:2182/ | sed 's/<\/tr>/\n/g' | sed -e 's/<[^>]*>/,/g' | awk '{FS=","}{printf "%-30s %-10s \n", $4, $8}'
```
