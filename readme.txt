MusicWorld

Autor - Robert Bogacz

Program został stworzony w środowiku PyCharm 2020.2.2 (Professional Edition) z wykorzystaniem interpretera Python 3.8 rozszerzonego o moduły wyszczególnione w pliku requirements.txt


Do poprawnego działania projektu konieczne jest uruchomienie lokalnego serwera bazodanowego SQL Server. Następnie należy na nim utworzyć bazę MusicWorld, przechowującą bazę danych projektu. Można to zrobić na dwa sposoby:
1) Poprzez uruchomienie na serwerze skryptu SQL o nazwie createMusicWorld znajdującego się w folderze Baza danych. (UWAGA: W skrypcie należy zmienić lokalizację pliku bazy danych oraz pliku logów bazy danych. W tym celu konieczne jest zmienienie ścieżek, które znajdują się w linijkach 7 i 9, przekazywanych jako parametr FILENAME. Ścieżki powinny prowadzić do lokalizacji, pod którymi te pliki mają być przechowywane na komputerze lokalnym.)
2) Możliwe jest również stworzenie bazy danych z backupu MusicWorld_backup zamieszczonego w folderze Baza danych.


Instrukcja uruchamiania programu:
1) W programie PyCharm należy otworzyć projekt zamieszczony w folderze o nazwie Projekt Inżynierski. 
2) Po otwarciu projektu należy przejść do ustawień i przypisać do niego interpreter Python 3.8. 
3) Następnie należy zainstalować biblioteki używane w projekcie. Znaleźć je można w pliku requirements.txt. 
4) W pliku db_handling.py należy zmienić nazwę serwera i bazy danych. W tym celu należy wyedytować linijkę 10 i w miejsce tekstu 'LAPTOP-OLVBJSU6' podać nazwę serwera lokalnego.
5) Po poprawnym wykonaniu wszystkich poprzednich kroków można uruchomić wykonywanie pliku startowego: index.py.
6) Po jego uruchomieniu powinien zostać zwrócony adres http://127.0.0.1:8050/ przez który możliwe jest połączenie się z aplikacją z poziomu przeglądarki internetowej.


W razie problemów z uruchomieniem aplikacji autor prosi o kontakt:
email: robert.bogacz@edu.wsti.pl 
telefon: +48 668 939 176