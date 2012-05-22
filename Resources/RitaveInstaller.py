import time
import os
import sys
import subprocess
# Made by Olaf "Ritave" Tomalka (olaf.tomalka@gmail.com)
# Thanks to Rapacz
# Tested with python3

install_drive=""

class Color:
	Reset	= "\033[m"
	Red	= "\033[31m"
	Cyan	= "\033[36m"

def Bullet(string):
	print(Color.Cyan+"* "+Color.Reset+string)

def Exec(string):
	try:
		subprocess.check_call(string, shell=True)
	except subprocess.CalledProcessError:
		while 1:
			print(Color.Red+"Blad podczas wykonywania \""+Color.Reset+string+Color.Red+"\"!!!"+Color.Reset)
			time.sleep(60)

def Intro():
	# It just looks sexy ;)
	print(Color.Cyan+"Stowarzyszenie"+Color.Reset+"""
_________ _______  _        _______  _       _________
\__   __/(  ___  )( \      (  ____ \( (    /|\__   __/
   ) (   | (   ) || (      | (    \/|  \  ( |   ) (   
   | |   | (___) || |      | (__    |   \ | |   | |   
   | |   |  ___  || |      |  __)   | (\ \) |   | |   
   | |   | (   ) || |      | (      | | \   |   | |   
   | |   | )   ( || (____/\| (____/\| )  \  |   | |   
   )_(   |/     \|(_______/(_______/|/    )_)   )_(   
   Pendrive by: Olaf \"Rit"""+Color.Red+"a"+Color.Reset+"""ve\" Tomalka
""")

def GetInstallDisk():
	global install_drive
	partitions=open("/proc/partitions")
	lines = partitions.readlines()[2:]
	biggest_size=0
	biggest_index=""
	for line in lines:
		words = [x.strip() for x in line.split()]
		if not words[3][-1:].isdigit() and int(words[2]) > biggest_size:
			biggest_size = int(words[2])
			biggest_index = words[3]
	install_drive = '/dev/'+biggest_index
	Bullet("Automatycznie wybralem najwiekszy dysk: "+install_drive)

def Install():
	global install_drive
	Bullet("Zaczynam instalacje")
	Exec(r"rm -rf /SYSTEM")
	Exec(r"mkdir /SYSTEM")

	Bullet("[1/5] Tworze mape partycji")
	Exec(r"fdisk "+install_drive+r"< /Resources/fdiskScript > /dev/null 2> /dev/null")

	Bullet("[2/5] Generuje system plikow ext4")
	Exec(r"mkfs.ext4 "+install_drive+r"2 >/dev/null 2> /dev/null")

	Bullet("[3/5] Generuje swap")
	Exec(r"mkswap "+install_drive+r"1 >/dev/null")

	Bullet("[4/5] Kopiuje system...")
	Exec(r"mount "+install_drive+r"2 /SYSTEM")
	Exec(r"tar xf /Resources/System.tar -C /SYSTEM")

	Bullet("[5/5] Instaluje grub'a")
	Exec(r"mount -t proc none /SYSTEM/proc")
	Exec(r"mount --bind /dev /SYSTEM/dev")
	Exec(r"cp /Resources/grub.sh /SYSTEM/")
	Exec(r"chroot /SYSTEM /bin/bash grub.sh "+install_drive+" >/dev/null 2>/dev/null")
	Exec(r"rm /SYSTEM/grub.sh")
	Exec(r"umount /SYSTEM/proc")
	Exec(r"umount /SYSTEM/dev")

	Bullet("Restartuje")
	Bullet("Milego dnia :)")
	Exec(r"umount "+install_drive+r"2")
	Exec(r"rm -r /SYSTEM")
	Exec(r"reboot")

if __name__ == "__main__":
	Exec(r"clear")
	Intro()
	GetInstallDisk()
	Install()
