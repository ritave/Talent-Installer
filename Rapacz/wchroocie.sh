#!/bin/bash
grub-install --no-floppy --recheck /dev/sda &&
update-grub2 &&
exit
