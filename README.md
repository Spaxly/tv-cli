<h1 align=center>
tv-cli
</h1>
</p>

<h3 align="center">
A cli to browse and watch live TV. This tool scrapes the site <a href="https://ustvgo.tv">ustvgo.</a>
</h3>
<h3 align="center">
This will only work in the US or with a US IP!
</h3>
	
## Table of Contents

- [Install](#Install)
  - [Linux](#Linux)
  - [MacOS](#MacOS)
- [Uninstall](#Uninstall)
- [Issues](#Issues)
- [Dependencies](#Dependencies)
- [Disclaimer](./DISCLAIMER.md)

## Install

### Python Version
**The python version fixes issues of some channels not showing.**
```pip install git+https://www.github.com/justfoolingaround/fzf.py && pip install bs4 && pip install httpx```
<br>
```git clone https://github.com/Spaxly/tv-cli && cd ./tv-cli && sudo cp ./tv-cli.py /usr/local/bin```

### Linux

Install dependencies [(See below)](#Dependencies)

```sh
git clone "https://github.com/Spaxly/tv-cli.git" && cd ./tv-cli
chmod +x ./tv-cli
sudo cp ./tv-cli /usr/local/bin
cd .. && rm -rf "./tv-cli"
```
*Also note that mpv installed through flatpak is not compatible*

### MacOS

Install dependencies [(See below)](#Dependencies)

Install [HomeBrew](https://docs.brew.sh/Installation) if not installed.

```sh
git clone "https://github.com/Spaxly/tv-cli" && cd ./tv-cli
cp ./tv-cli "$(brew --prefix)"/bin 
cd .. && rm -rf ./tv-cli
```

*To install (with Homebrew) the dependencies required on Mac OS, you can run:* 

```sh
brew install ffmpeg mpv curl sed git
``` 
## Uninstall

* Linux:  
```sh
sudo rm "/usr/local/bin/tv-cli"
```
* Mac:  
```sh
rm "$(brew --prefix)/bin/tv-cli"
```
## Issues
- Some channels like ESPN won't work if you are outside the U.S. Only way to fix this temporarily is to use a VPN. 

## Dependencies

- git
- fzf
- sed
- curl
- mpv
