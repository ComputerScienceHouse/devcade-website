# Troubleshooting

## Table of contents

- [Buttons swapping places](#Buttons-swapping-places)

## Buttons swapping places

### Issue:

Buttons will swap places on reboot. In the case we have observed the following buttons will be swapped as seen: A1<->A2 and B1<->B2 on each controller

### Causes:

The cause for this issue is currently presumed to be that the control boards were somehow at some point set to nintendo switch mode which switches the "x" and "y" buttons as well as the "triggers". When this is interpreted by the system this results in the wrong buttons being assigned to the devcade buttons.

### Fixes:

Simply unplugging and plugging back in the controller boards will fix it temporarily untill the system is rebooted. The permanant fix is to hold down the A1 button while rebooting the system. This sets it into PS3 mode and it should remember this through future reboots. 
