alias ll="ls -al"
export PS1='\n\[\e[33m\]\w\[\e[0m\] \[\e[34m\]\t\[\e[0m\]\[\e[36m\]`__git_ps1`\[\e[0m\]\n\$ '

if [ `pwd` == "/c/Windows/System32" ] 
then
    cd ~/Desktop
fi
