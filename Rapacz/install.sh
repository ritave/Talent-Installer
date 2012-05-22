#!/bin/bash
cd /
echo -e "d\n1\nd\n2\nd\n3\nd\n4\nn\np\n1\n\n+1G\nn\np\n2\n\n+10G\nt\n1\n82\nt\n2\n83\na\n2\nw" | fdisk /dev/sda;
mkfs.ext3 /dev/sda2 &&
mkswap /dev/sda1 &&
mkdir /SYSTEM &&
mount /dev/sda2 /SYSTEM &&
cp /mnt/cdrom/Resources/wchroocie.sh /SYSTEM &&
tar xzf /mnt/cdrom/Resources/ubuntu2.tgz -C /SYSTEM &&
rm /SYSTEM/etc/fstab &&
cp /mnt/cdrom/Resources/fstab /SYSTEM/etc &&
mount -t proc none /SYSTEM/proc &&
mount -o bind /dev /SYSTEM/dev &&
chroot /SYSTEM /bin/bash wchroocie.sh &&
rm /SYSTEM/wchroocie.sh &&
umount /dev/sda2;
umount /dev/sdb1;
reboot
