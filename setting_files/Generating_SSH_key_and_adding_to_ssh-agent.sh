#Generating_SSH_key_and_adding_to_ssh-agent
your_email="klgentle@sina.com"

ssh-keygen -t rsa -b 4096 -C $your_email
#start the ssh-agent in the background
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa

cat $HOME/.ssh/id_rsa.pub
# TODO Add the SSH key to your GitHub account.
