#! /bin/bash

SYS_TOOL=(
    gcc g++ make preload libncurses5 cmake
    libncurses5-dev build-essential  
    python python3 python-dev python3-dev
    exuberant-ctags
)

DEV_TOOL=(
    git tree curl wget zsh tmux nc locate stardict
    python-pip python3-pip p7zip-full screenfetch
    python-virtualenv python3-virtualenv virtualenvwrapper
)

apt-get -y update; apt-get -y upgrade; apt-get -y autoremove

updatedb

for tool in ${SYS_TOOL[*]};
do
    apt-get -y install $tool
    if [[ $? -ne 0 ]]; then
        continue
    fi
done

for tool in ${DEV_TOOL[*]};
do
    apt-get -y install $tool
    if [[ $? -ne 0 ]]; then
        continue
    fi
done

zpath=$(which zsh)
if [[ $? -eq 0 ]]; then
    chsh -s ${zpath}
    sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
fi

if [[ ! -d "$HOME/worktmp" ]]; then
    mkdir $HOME/worktmp
fi
cd $HOME/worktmp
vimstatus=$(git clone https://github.com/vim/vim.git)
cd vim
./configure --enable-python3interp=yes --enable-pythoninterp=yes
make && make install

git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
