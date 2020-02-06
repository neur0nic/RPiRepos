# Fensterscheiss
Weil bei uns immer vergessen wird das Badfester zu schließen und ich 
noch einen RPi Zero rumliegen hab, der nicht benutzt wird, hab ich
heute schnell eine __Eieruhr__ gebaut.

## Funktionsweise
Beim Betätigen des Buttons beginnt ein 10 Minuten Countdown, an dessen
Ende ein Ton an das Schließen des Fensters erinnert. Ein weiterer Button
quttiert das Schließen des Fensters und schaltest das __Fensterscheiss__
Gerät ab.

## Einrichtung
*run.py* in *home* Folder speichern und folgende Zeilen zur `.bashrc`
bzw. `.zshrc` hinzufügen.
```
echo Running at boot 
sudo python /home/alarm/run.py
```

## Schaltplan
![](https://github.com/neur0nic/RPiRepos/blob/master/Fensterscheiss/w_scheme.png)

## Lizens
"THE BEER-WARE LICENSE" (Revision 42):
<stephan.mertens1@gmx.net> wrote this file. 
As long as you retain this notice you can do whatever you want with this
stuff. If we meet some day, and you think this stuff is worth it, you
can buy me a beer in return. Stephan Mertens

