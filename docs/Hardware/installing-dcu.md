# Setting up a new cabinet

The Devcade project should theoretically run on just about any linux distro if set up properly. Our distro of choice is Debian 11.

We now take advantage of Debian's preseed functionality. Our preseed file is located at https://devcade.csh.rit.edu/preseed.txt and is based off of the file given as an example in the [Debian Wiki](https://wiki.debian.org/DebianInstaller/Preseed).

Devcade and its games ought to run on nearly any x86 hardware released in the last 10 years, but we recommend:

**CPU:** Intel Core i5 (5th gen or better)
**RAM:** 8GB
**GPU:** ¯\\_(ツ)_/¯

To begin, download a copy of [Debian Bullseye](https://mirrors.rit.edu/debian/debian-cd/11.6.0/amd64/iso-cd/debian-11.6.0-amd64-netinst.iso). Flash it onto a USB drive and boot from it. **Make sure to have the machine connected to the internet.** If you can, add a DHCP entry.

When you see the GRUB screen, you will need to supply the URL of our preseed file.

### BIOS

If booting with BIOS, simply press `esc` and type `auto url=https://devcade.csh.rit.edu/preseed.txt`. 

## UEFI

If using UEFI, enter `Advanced Options`, select `Automated Install`, press `e`, and move down to the line that starts with `linux`, and at the end of the line, add `auto url=https://devcade.csh.rit.edu/preseed.txt`. Press `^X` to boot.

## Booting the installer

The installer will grab the preseed file from our website, which will pre-fill many options for you, such as packages to install. You can navigate to the preseed url in your browser and read the options used.

It will also set up the devcade user, and prompt you for a password. If using it, the machine will set up its hostname using DHCP.

The installation takes around 10 minutes. When finished, it will reboot.

## Configuration and setup

When the machine comes back up, you will be presented with a login prompt. Log in with username `devcade` and the provided password, and then run the `configure.sh` script in the home directory. Reboot again, and you should have a shiny new Devcade!
