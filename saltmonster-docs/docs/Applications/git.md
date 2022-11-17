# Git

### Configuring git locally

To start using Git from your computer, you must enter your credentials (user name and email) to identify you as the author of your work. The user name and email should match the ones you’re using in GitHub.

```bash
# git config --global user.name "John Smith"
# git config --global user.email "johnsmith@company.com"
```

### Clone a repo locally

via https

```bash
# git clone https://git/Documentation.git
```

via ssh (Key must be in place)

```bash
# git clone git@git/Documentation.git
```

### Create a deploy key

Generate a unique ssh key for git

```bash
# ssh-keygen -y ed25519 -C "Comment"
```
File name is id_ed25519_git

Create a ssh config file to direct git requests to that key

```bash
# touch ~/.ssh/config
# chmod 600 ~/.ssh/config
```

Add the following to the config file
```bash
Host github-repo
	HostName github.com 
    AddKeysToAgent yes 
    PreferredAuthentications publickey 
    IdentityFile ~/.ssh/id_ed25519_git
```

Add the pub key (id_ed25519_git.pub) to the Deploy keys in settings of your repo

Test by cloning repository
```bash
# git clone git@github-repo:saltmonster/test.git
```
