function Test_And_Install_Package() {
	if [[ $(Test_Package_Installed $1) == 0 ]]; then
	    echo "Install $1"
	    sudo apt-get install $1 -y
    fi

	if [[ $(Test_Package_Installed $1) == 1 ]]; then
		coloredEcho "$1 installed." green
	else
		coloredEcho "$1 installation failed." red
		exit 1;
	fi
}


Test_And_Install_Package curl
Test_And_Install_Package git
Test_And_Install_Package cmake
Test_And_Install_Package vim
Test_And_Install_Package python-pip
Test_And_Install_Package guake

mkdir /tmp/vscode
cd /tmp/vscode/
wget https://vscode.cdn.azure.cn/stable/950b8b0d37a9b7061b6f0d291837ccc4015f5ecd/code_1.22.1-1522974421_amd64.deb
sudo dpkg -i *.deb