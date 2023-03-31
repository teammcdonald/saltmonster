# Grub

### Booting to single user

1. Replace ro with rw init=/sysroot/bin/sh
2. chroot /sysroot

### Changing root password

1. Do the above 
2. passwd root
3. touch /.autorelabel
4. exit
5. reboot