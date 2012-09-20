# Samoinstalujący się pendrive do Płytek OIG 2012 Uranos
*Olaf "Ritave" Tomalka - [olaf.tomalka@gmail.com](olaf.tomalka@gmail.com)*
## Struktura pendriva
* Pendrive ma zainstalowany jakiś system bootstrapujący (ja użyłem Arch Linux) który w ```/``` posiada folder **Resources** z tego samego folderu co ten README
    * System ten musi posiadać python3 (testowana wersja to 3.2)
        * Nie powinno być dla kogoś znającego python2 zportowanie tego skryptu w dół, jeśli wolisz to możesz to zrobić
    * Musi umieć tworzyć partycję ext4
        * Możesz to zamienić na jakiś starszy edytując odpowiednią linijke w głównym skrypcie
* Installator odpala się komendą ```python3 Resources/RitaveInstaller.py```
* Najlepiej dodać powyższą komendę do ```/etc/inittab``` zamiast tty0, w ten sposób uruchomi się automatycznie po włączeniu pendriva
    * Ew. możesz na tty0 włączyć autologin a skrypt wrzucić do ```/etc/rc.local``` ale nie jest to moim zdaniem najlepsze wyjśćie

## Potrzebne pliki
* Zainstaluj sobie twoje iso na jakimś kompie i po przeczytaniu całego readme zbootuj z jakiegoś pendriva i skompresuj partycje twojego zainstalowanego systemu do tara
* System wsadzic do /Resources/System.tar jako nie skompresowany tar
    * Pamiętaj aby sprawdzić czy nie jest w żadnym podfolderze - ```tar xf System.tar ./``` powinien rozpakować cały system do obecnego katalogu **a nie do jakiegoś podkatalogu np. ```./System/```**
* W instalowanym systemie przed kompresowaniem musisz podmienić ```/etc/fstab```
    * Jako że system będzie na wielu kompach to nie może używać UUID dysku
    * Musisz kazać mu mountować systemy plików poprzez ```/dev/sdaX``` gdzie X to jakaś cyfra
        * O ile dobrze pamiętam ```/dev/sda1``` to swap a ```/dev/sda2``` to główny system

## Notatki
* W folderze Rapacz znajdują się stare pliki ze starego systemu instalującego Marcina Rapackiego, mogą okazać ci się przydatne
* Możliwe, że skrypt rożni się od tego co był na OIGu detalami bo dodawałem last-minute poprawki, a nie mam obecnie dostępu do tamtych pendrivów
