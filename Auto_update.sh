#!/bin/bash
dpkg -s picoscenes-platform | grep Version | sed 's/Version: //g' > my_version.txt
version=$(cat version.txt)
my_version=$(cat my_version.txt)
if [ "$version" == "$my_version" ]; then
    echo "You don not need to update"
else
read -n1 -p "PicoScenes only supports the following Ubuntu versions and their variants, choose the correct one for your system: 
1: Ubuntu 16.04; 
2: Ubuntu 17.10; 
3: Ubuntu 18.04;

Your choice is: " answer
case $answer in
1) wget -O release.zip https://gitlab.com/wifisensing/release/PicoScenes-Release/-/jobs/artifacts/master/download?job=PicoScenes_platform%2Bplugins_for_Ubuntu16.04;;
2) wget -O release.zip https://gitlab.com/wifisensing/release/PicoScenes-Release/-/jobs/artifacts/master/download?job=PicoScenes_platform%2Bplugins_for_Ubuntu17.10;;
3) wget -O release.zip https://gitlab.com/wifisensing/release/PicoScenes-Release/-/jobs/artifacts/master/download?job=PicoScenes_platform%2Bplugins_for_Ubuntu18.04;;
esac

unzip -o release.zip
sudo dpkg -r picoscenes-plugins-demo-rxsbroadcaster-chronos
sudo dpkg -r picoscenes-platform
sudo dpkg -i picoscenes-platform*.deb
sudo dpkg -i picoscenes-plugins*.deb
fi
