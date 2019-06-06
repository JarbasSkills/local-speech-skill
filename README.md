# <img src='https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/microphone-alt.svg' card_color='#40DBB0' width='50' height='50' style='vertical-align:bottom'/> Local Speech
Listens offline for wake words and pre-defined speech commands

## About
Using kaldi it will perform offline speech recognition 24/7

pre approved commands will be broadcast to messagebus

also works as a wake word spotter, multiple wake words supported at the same time

wake words will trigger mycroft's speech client

edit your configuration at "~/.kaldi_spotter/kaldi_spotter.conf" or add/remove hotwords at home.mycroft.ai, see [kaldi_spotter](https://github.com/JarbasAl/kaldi_spotter) for configuration details

## Examples

## Credits
JarbasAI (@jarbasal)

## Category
**Configuration**

## Tags
#offline
#STT
#mic


## Manual install

this skill will not install by msm

- cython and numpy need to be installed before requirements.txt will complete

- pre-trained model needs manual download

NOTE: on a mark1 to use pip you can do ```sudo mycroft-pip install numpy ```

### System Requirements

```bash
sudo apt-get install libatlas-dev pulseaudio-utils pulseaudio cython
```

### Pre-trained models

You can install English model ```kaldi-chain-zamia-speech-en``` or german model ```kaldi-chain-zamia-speech-de```

Refered as ```kaldi-chain-zamia-speech-XX``` bellow

#### Raspbian 9 (stretch) on a Raspberry Pi 2/3
```bash
echo "deb http://goofy.zamia.org/repo-ai/raspbian/stretch/armhf/ ./" >/etc/apt/sources.list.d/zamia-ai.list
wget -qO - http://goofy.zamia.org/repo-ai/raspbian/stretch/armhf/bofh.asc | sudo apt-key add -
apt-get update
apt-get install kaldi-chain-zamia-speech-XX
```

#### Debian 9 (stretch, amd64)
```bash
apt-get install apt-transport-https
echo "deb http://goofy.zamia.org/repo-ai/debian/stretch/amd64/ ./" >/etc/apt/sources.list.d/zamia-ai.list
wget -qO - http://goofy.zamia.org/repo-ai/debian/stretch/amd64/bofh.asc | sudo apt-key add -
apt-get update
apt-get install kaldi-chain-zamia-speech-XX
```

#### CentOS 7 (amd64)
```bash
cd /etc/yum.repos.d
wget http://goofy.zamia.org/zamia-speech/misc/zamia-ai-centos.repo
yum install kaldi-chain-zamia-speech-XX
```
