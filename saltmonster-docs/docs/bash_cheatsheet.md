# Bash Cheatsheet

Get into the wonderful world of bash

```
# bash
```

* grep - Global Regular Expression Print
* awk - Aho, Weinberger, and Kernighan
* sed = Stream EDitor
* sort = sort
* uniq = unique
* wc = word count
* head = head
* tail = tail
* more = more
* find = find

### grep

<details>
<summary>grep <-- search a file</summary>

- test_file_space.txt
```
Cat 57 99
cat 23 89
dog 24 90
dog 89 80
horse 88 91
rabbit 87 78
rabbit 76 22
snake 33 99
snipe 44 98
turtle 88 76
fish 22 22
```

- Example
```
# grep dog test_file_space.txt
dog 24 90
dog 89 80
```
</details>

<details>
<summary>grep -i <-- ignore case</summary>

- test_file_space.txt
```
Cat 57 99
cat 23 89
dog 24 90
dog 89 80
horse 88 91
rabbit 87 78
rabbit 76 22
snake 33 99
snipe 44 98
turtle 88 76
fish 22 22
```

- Example
```
# grep -i cat test_file_space.txt
Cat 57 99
cat 23 89
```
</details>

<details>
<summary>grep -A <-- display rows after</summary>

- test_file_space.txt
```
Cat 57 99
cat 23 89
dog 24 90
dog 89 80
horse 88 91
rabbit 87 78
rabbit 76 22
snake 33 99
snipe 44 98
turtle 88 76
fish 22 22
```

- Example
```
# grep -A 2 dog test_file_space.txt
dog 24 90
dog 89 80
horse 88 91
rabbit 87 78
```

</details>

<details>
<summary>grep -B <-- display rows before</summary>

- test_file_space.txt
```
Cat 57 99
cat 23 89
dog 24 90
dog 89 80
horse 88 91
rabbit 87 78
rabbit 76 22
snake 33 99
snipe 44 98
turtle 88 76
fish 22 22
```

- Example
```
# grep -B 2 dog test_file_space.txt
Cat 57 99
cat 23 89
dog 24 90
dog 89 80
```

</details>

<details>
<summary>grep -C <-- display rows in context</summary>

- test_file_space.txt
```
Cat 57 99
cat 23 89
dog 24 90
dog 89 80
horse 88 91
rabbit 87 78
rabbit 76 22
snake 33 99
snipe 44 98
turtle 88 76
fish 22 22
```

- Example
```
# grep -C 2 dog test_file_space.txt
Cat 57 99
cat 23 89
dog 24 90
dog 89 80
horse 88 91
rabbit 87 78
```

</details>

<details>
<summary>grep -v <-- exclude rows</summary>

- test_file_space.txt
```
# Animals
Cat 57 99

cat 23 89

dog 24 90

dog 89 80

horse 88 91

rabbit 87 78

rabbit 76 22

snake 33 99

snipe 44 98

turtle 88 76

fish 22 22
```

- Example
```
# grep -v dog test_file_comment.txt
# Animals
Cat 57 99

cat 23 89



horse 88 91

rabbit 87 78

rabbit 76 22

snake 33 99

snipe 44 98

turtle 88 76

fish 22 22
```

```
# grep -v ^$ test_file_comment.txt
# Animals
Cat 57 99
cat 23 89
dog 24 90
dog 89 80
horse 88 91
rabbit 87 78
rabbit 76 22
snake 33 99
snipe 44 98
turtle 88 76
fish 22 22
```

</details>

<details>
<summary>grep -R <-- recursive search</summary>

- Directoy Structure
```
# ls -laR
.:
total 28
drwxr-xr-x. 3 root root 4096 Jun 16 14:28 .
drwxr-xr-x. 3 root root 4096 Jun 16 11:33 ..
drwxr-xr-x. 2 root root 4096 Jun 16 14:30 subdir
-rwxr-xr-x. 1 root root   81 Jun 16 11:35 test_exit.sh
-rw-r--r--. 1 root root  126 Jun 16 14:05 test_file_comma.txt
-rw-r--r--. 1 root root  146 Jun 16 14:23 test_file_comment.txt
-rw-r--r--. 1 root root   64 Jun 16 13:58 test_file_name.txt
-rw-r--r--. 1 root root  126 Jun 16 13:33 test_file_space.txt

./subdir:
total 8
drwxr-xr-x. 2 root root 4096 Jun 16 14:30 .
drwxr-xr-x. 3 root root 4096 Jun 16 14:28 ..
-rw-r--r--. 1 root root   24 Jun 16 14:30 test_file_recursiv.txt
```

- Example
```
# grep -R cat *
subdir/test_file_recursiv.txt:cat
test_file_comma.txt:cat,23,89
test_file_comment.txt:cat 23 89
test_file_name.txt:cat
test_file_space.txt:cat 23 89
```

</details>

### awk
<details>
<summary>awk <-- pattern scanning</summary>

- test_file_space.txt
```
Cat 57 99
cat 23 89
dog 24 90
dog 89 80
horse 88 91
rabbit 87 78
rabbit 76 22
snake 33 99
snipe 44 98
turtle 88 76
fish 22 22
```

- Example
```
# awk '{print "I love",$1"s"}' test_file_space.txt
I love Cats
I love cats
I love dogs
I love dogs
I love horses
I love rabbits
I love rabbits
I love snakes
I love snipes
I love turtles
I love fishs
```

</details>

<details>
<summary>awk -F <-- change the field separator</summary>

- test_file_comma.txt
```
Cat,57,99
cat,23,89
dog,24,90
dog,89,80
horse,88,91
rabbit,87,78
rabbit,76,22
snake,33,99
snipe,44,98
turtle,88,76
fish,22,22
```

- Example
```
# awk -F, '/dog/ {print "I love",$1"s"}' test_file_comma.txt
I love dogs
I love dogs
```

```
# awk -F, '$3>90 {print $0}' test_file_comma.txt
Cat,57,99
horse,88,91
snake,33,99
snipe,44,98
```

```
# awk -F, '$NF>90 {print $0}' test_file_comma.txt
Cat,57,99
horse,88,91
snake,33,99
snipe,44,98
```

</details>

### sed
<details>
<summary>sed <-- stream editor for text manipulation </summary>

- test_file_name.txt
```
Cat
cat
dog
dog
horse
rabbit
rabbit
snake
snipe
turtle
fish
dog
```

- Example
```
# sed 's/Cat/cat/g' test_file_name.txt
cat
cat
dog
dog
horse
rabbit
rabbit
snake
snipe
turtle
fish
dog
# cat test_file_name.txt
Cat
cat
dog
dog
horse
rabbit
rabbit
snake
snipe
turtle
fish
dog
```

</details>

<details>
<summary>sed -i <-- inline</summary>

- test_file_name.txt
```
Cat
cat
dog
dog
horse
rabbit
rabbit
snake
snipe
turtle
fish
dog
```

- Example
```
# sed -i 's/Cat/cat/g' test_file_name.txt
# cat test_file_name.txt
cat
cat
dog
dog
horse
rabbit
rabbit
snake
snipe
turtle
fish
dog
```

</details>

<details>
<summary>sed -e </summary>

- test_file_name.txt
```
Cat
cat
dog
dog
horse
rabbit
rabbit
snake
snipe
turtle
fish
dog
```

- Example
```
# sed -e 's/C/c/g' -e 's/h/H/g' test_file_name.txt
cat
cat
dog
dog
Horse
rabbit
rabbit
snake
snipe
turtle
fisH
dog
```

</details>

### sort
<details>
<summary>sort <-- sorting text</summary>

- test_file_space.txt
```
Cat 57 99
cat 23 89
dog 24 90
dog 89 80
horse 88 91
rabbit 87 78
rabbit 76 22
snake 33 99
snipe 44 98
turtle 88 76
fish 22 22
```

- Example
```
# sort test_file_space.txt
cat 23 89
Cat 57 99
dog 24 90
dog 89 80
fish 22 22
horse 88 91
rabbit 76 22
rabbit 87 78
snake 33 99
snipe 44 98
turtle 88 76
```

</details>

<details>
<summary>sort -n <-- numeric sort</summary>

- test_file_space.txt
```
Cat 57 99
cat 23 89
dog 24 90
dog 89 80
horse 88 91
rabbit 87 78
rabbit 76 22
snake 33 99
snipe 44 98
turtle 88 76
fish 22 22
```

- Example
```
# sort -n -k 2 test_file_space.txt
fish 22 22
cat 23 89
dog 24 90
snake 33 99
snipe 44 98
Cat 57 99
rabbit 76 22
rabbit 87 78
horse 88 91
turtle 88 76
dog 89 80
```

</details>

### uniq
<details>
<summary>uniq <-- simple omit of repeated lines</summary>

- test_file_name.txt
```
Cat
cat
dog
dog
horse
rabbit
rabbit
snake
snipe
turtle
fish
dog
```

- Example
```
# uniq test_file_name.txt
Cat
cat
dog
horse
rabbit
snake
snipe
turtle
fish
dog
```

</details>

<details>
<summary>uniq -c <-- count</summary>

- test_file_name.txt
```
Cat
cat
dog
dog
horse
rabbit
rabbit
snake
snipe
turtle
fish
dog
```

- Example
```
# uniq -c test_file_name.txt
      1 Cat
      1 cat
      2 dog
      1 horse
      2 rabbit
      1 snake
      1 snipe
      1 turtle
      1 fish
      1 dog
```

</details>

### wc
<details>
<summary>wc <-- word count</summary>

- test_file_space.txt
```
Cat 57 99
cat 23 89
dog 24 90
dog 89 80
horse 88 91
rabbit 87 78
rabbit 76 22
snake 33 99
snipe 44 98
turtle 88 76
fish 22 22
```

- Example
```
# wc test_file_space.txt
 11  33 126 test_file_space.txt
```

```
# wc -l test_file_space.txt
11 test_file_space.txt
```

</details>

### head
<details>
<summary>head <-- report the beginning of a file</summary>

- test_file_space.txt
```
Cat 57 99
cat 23 89
dog 24 90
dog 89 80
horse 88 91
rabbit 87 78
rabbit 76 22
snake 33 99
snipe 44 98
turtle 88 76
fish 22 22
```

- Example
```
# head test_file_space.txt
Cat 57 99
cat 23 89
dog 24 90
dog 89 80
horse 88 91
rabbit 87 78
rabbit 76 22
snake 33 99
snipe 44 98
turtle 88 76
```

```
# head -2 test_file_space.txt
Cat 57 99
cat 23 89
```

</details>

### tail 
<details>
<summary>tail <-- report the end of a file</summary>

- test_file_space.txt
```
Cat 57 99
cat 23 89
dog 24 90
dog 89 80
horse 88 91
rabbit 87 78
rabbit 76 22
snake 33 99
snipe 44 98
turtle 88 76
fish 22 22
```

- Example
``` 
# tail test_file_space.txt
cat 23 89
dog 24 90
dog 89 80
horse 88 91
rabbit 87 78
rabbit 76 22
snake 33 99
snipe 44 98
turtle 88 76
```

```
# tail -2 test_file_space.txt
snipe 44 98
turtle 88 76
```

</details>

<details>
<summary>tail -f <-- follow</summary>

- test_file_space.txt
```
Cat 57 99
cat 23 89
dog 24 90
dog 89 80
horse 88 91
rabbit 87 78
rabbit 76 22
snake 33 99
snipe 44 98
turtle 88 76
fish 22 22
```

- Example
```
# tail -f test_file_space.txt
cat 23 89
dog 24 90
dog 89 80
horse 88 91
rabbit 87 78
rabbit 76 22
snake 33 99
snipe 44 98
turtle 88 76
fish 22 22

```

</details>

### more
<details>
<summary>more <-- report a file a page at a time</summary>

- test_file_space.txt
```
Cat 57 99
cat 23 89
dog 24 90
dog 89 80
horse 88 91
rabbit 87 78
rabbit 76 22
snake 33 99
snipe 44 98
turtle 88 76
fish 22 22
```

- Example
```
# more test_file_space.txt
Cat 57 99
cat 23 89
dog 24 90
dog 89 80
horse 88 91
--More--(41%)
```

</details>

### find
<details>
<summary>find <-- search for files</summary>

- Directoy Structure
```
# ls -laR
.:
total 28
drwxr-xr-x. 3 root root 4096 Jun 16 14:28 .
drwxr-xr-x. 3 root root 4096 Jun 16 11:33 ..
drwxr-xr-x. 2 root root 4096 Jun 16 14:30 subdir
-rwxr-xr-x. 1 root root   81 Jun 16 11:35 test_exit.sh
-rw-r--r--. 1 root root  126 Jun 16 14:05 test_file_comma.txt
-rw-r--r--. 1 root root  146 Jun 16 14:23 test_file_comment.txt
-rw-r--r--. 1 root root   64 Jun 16 13:58 test_file_name.txt
-rw-r--r--. 1 root root  126 Jun 16 13:33 test_file_space.txt

./subdir:
total 8
drwxr-xr-x. 2 root root 4096 Jun 16 14:30 .
drwxr-xr-x. 3 root root 4096 Jun 16 14:28 ..
-rw-r--r--. 1 root root   24 Jun 16 14:30 test_file_recursiv.txt
```

- Example
```
# find /home/jmcdonald/bash/examples -name "*.txt"
/home/jmcdonald/bash/examples/test_file_comma.txt
/home/jmcdonald/bash/examples/test_file_space.txt
/home/jmcdonald/bash/examples/test_file_name.txt
/home/jmcdonald/bash/examples/test_file_comment.txt
/home/jmcdonald/bash/examples/subdir/test_file_recursiv.txt
```

</details>

### redirection
<details>
<summary>Redirection <-- basic</summary>

- test_file_space.txt
```
Cat 57 99
cat 23 89
dog 24 90
dog 89 80
horse 88 91
rabbit 87 78
rabbit 76 22
snake 33 99
snipe 44 98
turtle 88 76
fish 22 22
```

- Example
```
# grep dog test_file_space.txt > temp.txt
# cat temp.txt
dog 24 90
dog 89 80
# grep dog test_file_space.txt > temp.txt
# cat temp.txt
dog 24 90
dog 89 80
```

```
grep dog test_file_space.txt >> temp.txt
# cat temp.txt
dog 24 90
dog 89 80
# grep dog test_file_space.txt >> temp.txt
# cat temp.txt
dog 24 90
dog 89 80
dog 24 90
dog 89 80
```

```
# awk '{print $1}' test_file_space.txt | sed 's/[A-Z]/\L&/g' | sort | uniq -c | sort -rn
      2 rabbit
      2 dog
      2 cat
      1 turtle
      1 snipe
      1 snake
      1 horse
      1 fish
```

</details>

### exit codes
<details>
<summary>Exit Codes <-- basic</summary>

- test_exit.sh
```
#!/bin/bash
if [[ $1 -eq 0 ]];then
   echo "Good"
else
   echo "Bad"
fi
exit $1
```

- Example
```
# ./test_exit.sh 0
Good
# echo $?
0
# ./test_exit.sh 1
Bad
# echo $?
1
```

</details>

### bonus

[VIM - Disabling Colors](https://git.rockfin.com/pages/Kernel/Documentation/Applications/vim/)


[SSH Keys](https://git.rockfin.com/pages/Kernel/Documentation/Applications/ssh/)
