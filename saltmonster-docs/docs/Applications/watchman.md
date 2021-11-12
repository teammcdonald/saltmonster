# Watchman

### Overview

Watchman is a file/directory watching service.  It is open source from [Watchman URL](https://facebook.github.io/watchman/)

Watchman uses json format for it's configuration files.

**Steps**

1. Define a directory or file to watch
2. Create a trigger to log infotmation
   * Create a monitor in zabbix to monitor changes to the log file
3. Create a trigger to perform an action (fix)


### Basic Commands

Command | Notes
--------|------
watchman -j < watchman-watch.json | Starts a watch of a file or directory
watchman shutdown-server | Ends all watches on the server
watchman watch-list | View what watchman is watching
watchman trigger-list *watch-directory* | View trigeers on a watched directory 

### Example json files

**Watching a directory**
``` json
["watch", "/home/directory"]
```

**Trigger on a watched directory**
``` json
["trigger", "/home/directory", {
"name": "Trigger Log Write",
"append_files": true,
"command": ["/bin/watchman_command.sh"]
}]
```
