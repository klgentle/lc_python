eval `ssh-agent -s`
ssh-add ~/.ssh/lc_python_key
git pull origin master
