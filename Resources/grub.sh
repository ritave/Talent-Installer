#!/bin/bash
grub-install --no-floppy --recheck ${1} &&
update-grub2 &&
exit
