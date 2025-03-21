# My smiple config for qtile

Hi:)
first of all I would like to say that I was inspired by the DistroTube channel,

and wanted to do something similar but in my own way.
## Preview

![](https://github.com/ProgrammerLinuxRus/dots/blob/main/screen09.jpg)

## Installation

1. Clone repo
2. Сreate the necessary directories and copy the files into them

## Dependencies 

+ **alsa-utils**        *for volume module on bar*
+ **python-psutil**     *for cpu module on bar*
+ **erd-fonts**    *for icons*
+ **conky**        *for system monitor*
+ **nitrogen**     *for wallpapers*
+ **picom**  *just a compositor*
+ **alacritty** *treminal*
+ **dmenu** *apps runner*
+ **pacman-contrib** *for pacman module on bar*
  
To install on arch linux run the following commands:

~~~
sudo pacman -S alsa-utils python-psutil conky nitrogen picom alacritty pacman-contrib
~~~
and
~~~bash
yay -S nerd-fonts #or use another AUR helper
~~~
### Installing Dmenu
To install follow the [link](https://tools.suckless.org/dmenu/) and download the dmenu archive. Unpack it.

After that run the following commands:

~~~bash
cd /path/to/unpacked/directory/
~~~
~~~bash
sudo make install
~~~

**PATCHING**
Now you need to add some patches, download [xyz](https://tools.suckless.org/dmenu/patches/xyw/) and [line height](https://tools.suckless.org/dmenu/patches/line-height/) patches into dmenu directory and install it.
