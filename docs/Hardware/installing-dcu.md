
# Setting up a Devcade cabinet

## Table of Contents
- [Installing an OS](#installing-debian-11)
- [Network Configuration](#configuring-network)
- [APT Configuration](#fixing-apt)
	- [Sources](#sources-list)
	- [Packages](#package-setup)
	- [Dotnet](#dotnet-sdk)
- [Misc Setup](#other-misc-setup)
- [Devcade Onboard Setup](#installing-onboard)
	- [Clone](#clone-the-repo)
	- [Environment](#environment-vars)
	- [Daemons](#summoning-daemons)
- [X setup](#x-setup)
	- [.xinitrc](#xinitrc)
	- [Xinput](#xinput)
- [Pulseaudio](#pulseaudio-setup)
- [Daemons](#arcane-daemonology)


## Installing Debian 11

The Devcade project should theoretically run on just about any linux distro if set up properly. Our distro of choice for this guide will be Debian 11. Boot to the installer and proceed installing normally except for the following settings:

- User: `devcade`
- Force UEFI Mode
- Use Entire Disk
- Everything on 1 partition

## Configuring Network

Get MAC address and other info with `ip a`

Other network configurations will depend on your specific network setup. For example, we create a record in our network management system and reboot the computer to obtain DHCP.

## Fixing Apt

### Sources list

Edit `/etc/apt/source.list` and change (as needed):

* Remove the local cdrom:// source 
* Uncomment the official Debian repositories
* Add bullseye main repository
* `apt update` 
* `apt upgrade`


### Package Setup

Install optional but useful packages:

* `apt install openssh-server`
* `apt install neofetch`
* `apt install vim`
* `apt install datadog-agent`

Install required packages:

	apt install git xorg xterm compton openbox pulseaudio

### Dotnet SDK

[Add Microsoft repositories](https://learn.microsoft.com/en-us/dotnet/core/install/linux-debian#debian-11) and install the 6.0 version of the SDK. This is the version that most everything Devcade is written in and is guaranteed* to work with the source code. Future versions of the SDK might introduce breaking changes.

`apt install dotnet-sdk-6.0`


## Other Misc Setup

Add devcade to sudoers file (optional, highly recommended)

	usermod -aG sudo devcade
	echo "devcade ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers


## Installing onboard


### Clone the repo

Find a nice home for the onboard somewhere in your filesystem (like $HOME/git)

	cd ~
	mkdir git
	cd git
	git clone https://Github.com/ComputerScienceHouse/devcade-onboard
	cd devcade-onboard

### Environment vars
<!-- TODO -->
Setup a .env file according to the .env template in the repo (coming soon). Then run the following:

	cp .env ~/.env
	echo "source /home/devcade/.env" >> ~/.bashrc

This will source the environment variables used by Devcade every time you login.

### Summoning Daemons

From the onboard directory, initialize the xlogin submodule by running:

    git submodule update --init --recursive

To build the onboard program and put it in the correct place, run
<!-- TODO Update idiot naming →
./idiot/update_onboard.sh
cp idiot/.xinitrc /home/devcade
mkdir -p /home/devcade/.config/openbox && cp idiot/rc.xml /home/devcade/.config/openbox

To install xlogin do the following:
 
    cd idiot/xlogin
    sudo make install
    sudo systemctl enable --now xlogin@devcade

You may also need to do:

    cd /home/devcade/publish
    chmod +x onboard

## X Setup

### .xinitrc

The .xinitrc file is by default setup to use HDMI-2. If your monitor is not plugged into the second HDMI port (HINT: it probably won't be) you’ll encounter errors and need to edit the .xinitrc file with the correct output type. The file onboard.log should have the output of xrandr, which will include the correct display adapter (HINT: it’s the only one that has resolutions listed)

With a correctly configured display adapter in the .xinitrc it should _Just Work™_

### Xinput

// TODO


## PulseAudio Setup

PulseAudio is another thing that should Just Work™.

If it doesn’t, use the following commands to fix which audio sink is selected.

* `pacmd list-cards` or `pactl list cards`
* `pacmd list-sinks` or `pactl list sinks`
* `pactl set-default-sink [NAME]`

The `[NAME]` option will be the name of the audio source, which is the ENTIRE string after the ‘Monitor Source’ line in the sink information. For example the soundbar currently used in the first cabinet is:

	alsa_output.usb-Lenovo_Lenovo_USB_Soundbar-00.analog-stereo

If you have driver issues or encounter issues other than the sink not being set correctly: cry, pray, and despair, in that order.


## Arcane Daemonology

Once the computer is fully configured, the final step in the process is to set up a systemd service to automatically login and launch the onboard on boot. The only two things this requires are creating a service and editing the .bashrc

Create a service file at `/etc/systemd/system/getty@tty1.service.d/override.conf`. This may require creating a directory.
```
[Service]
Type=Simple
ExecStart=
ExecStart=-/sbin/agetty --autologin devcade --noclear %I 38400 linux
```

Then, add the following to the .bashrc of the devcade user:

```sh
if [[-z “$DISPLAY” ]] && [[ $(tty) = /dev/tty1 ]]; then
    . startx
    logout 
fi 
```

The machine will now login to the devcade user on boot and launch the onboard program. The onboard program will also relaunch every time it closes. To use a shell again, switch to a different tty or ssh into the machine.
