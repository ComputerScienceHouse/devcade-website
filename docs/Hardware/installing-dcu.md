# Setting Up a New Cabinet

## Table of Contents
- [Summary](#summary)
- [Booting Up](#booting-up)
  - [BIOS](#bios)
  - [UEFI](#uefi)
- [The Preseed File](#the-preseed-file)
- [Installation Components](#installation-components)
- [Booting the Installer](#booting-the-installer)
- [Configuration and Setup](#configuration-and-setup)

## Summary

The Devcade project should theoretically run on just about any linux distro if set up properly. Our distro of choice is Debian 11.

We now take advantage of Debian's preseed functionality to install the OS, and set up our launcher, [devcade-onboard](https://github.com/computersciencehouse/devcade-onboard). Our preseed file is located at https://devcade.csh.rit.edu/preseed.txt and is based off of the file given as an example in the [Debian Wiki](https://wiki.debian.org/DebianInstaller/Preseed).

Devcade and its games ought to run on nearly any x86 hardware released in the last 10 years, but we recommend:

**CPU:** Intel Core i5 (5th gen or better)
**RAM:** 8GB
**GPU:** ¯\\_(ツ)_/¯

## Booting Up

To begin, download a copy of [Debian Bullseye](https://mirrors.rit.edu/debian/debian-cd/11.6.0/amd64/iso-cd/debian-11.6.0-amd64-netinst.iso). Flash it onto a USB drive and boot from it. **Make sure to have the machine connected to the internet.** If you can, add a DHCP entry.

When you see the GRUB screen, you will need to supply the URL of our preseed file.

### BIOS

If booting with BIOS, simply press `esc` and type `auto url=https://devcade.csh.rit.edu/preseed.txt`. 

### UEFI

If using UEFI, enter `Advanced Options`, select `Automated Install`, press `e`, and move down to the line that starts with `linux`, and at the end of the line, add `auto url=https://devcade.csh.rit.edu/preseed.txt`. Press `^X` to boot.

## The Preseed File

The preseed file is simply a list of pre-selections for the debian installer. It is used to set up networking, configure disk partitions, and set up the account. It will also handle automatically selecting yes/no on prompts, but can stop to let you control things like the password and the disk to install the OS to.

## Installation Components

The preseed file installs the ssh-server, along with the following individual packages: `xinit xterm git build-essential wget openbox compton pulseaudio x11-xserver-utils`. 

[devcade-onboard](https://github.com/computersciencehouse/devcade-onboard) runs as an X11 application in Openbox, and runs Compton and pulseaudio. There are also some useful build utilities.

Apart from that, there are a number of auxiliary files:

- `bashrc-check.sh`: Used to append configuration to `.bashrc`
- `.env`: Environment variables used for the onboard
- `rc.xml`: Openbox configuration
- `update.sh`: Script used to update the onboard
- `tty1_service_override.conf`: getty systemd service
- `.xinitrc`: Starts X11 server, loads environment vars, configures display, and launches the onboard!
- `configure.sh`: Script that installs the Dotnet SDK and all of the above!

## Booting the installer

The installer will grab the preseed file from our website, which will pre-fill many options for you, such as packages to install. You can navigate to the preseed url in your browser and read the options used.

It will also set up the devcade user, and prompt you for a password. If using it, the machine will set up its hostname using DHCP.

The installation takes around 10 minutes. When finished, it will reboot.

## Configuration and setup

When the machine comes back up, you will be presented with a login prompt. Log in with username `devcade` and the provided password, and then run the `configure.sh` script in the home directory. Reboot again, and you should have a shiny new Devcade!
