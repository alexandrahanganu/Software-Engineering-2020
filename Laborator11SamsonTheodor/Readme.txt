a) Ce ati reusit sa faceti in aceasta iteratie?

Am terminat de implementat label-urile.
Am reparat impreuna cu restul colegilor bug-urile pentru terminarea algoritmului final.
Aproape terminasem partea noastra de la CNN, dar am dat de o mare problema, o gasiti la subpunctul b).
Am trecut de la a folosi tensorflow la a folosi keras. Am scris codul integral pentru implementarea cu keras.
Am mutat pozele preponderent negre intr-un alt folder (o mica restructurare).
Am rulat ambii algoritmi atat pe pozele doar negre cat si pe cele cu gri, pe path-uri diferite si cu parametri schimbati, pentru a vedea pe care dintre ele sunt rezultate mai bune.
Am incercat diferite rulari cu diferiti parametri pentru poze pentru identificarea problemei sau pentru a obtine o imbunatatire. 
Din pacate n-am avut succes.
Am folosit toti parametrii disponibili atat pe layere cat si pe model pentru a vedea daca exista vreo modificare. 
Diferentele au fost nesemnificative.
In urma debugging-urilor efectuate am dovedit ca label-urile functioneaza, path-urile sunt corecte, pozele sunt preluate 
una cate una, modelul are accuracy bun.

b) Ce probleme ati avut?

Din pacate, rezultatele pentru pacientii sanatosi sunt eronate. Rezultatele tind sa fie aproape de 1 (pe majoritatea cazurilor 
rezultatele sunt intre 0.8% pana la 0.95%), adica bolnavi. Tind sa cred ca aceasta problema rasare din faptul ca plamanii pacientilor 
sanatosi sunt extrem de similari cu cei ai celor bolnavi (diferenta o reprezinta cateva puncte albe, reprezentand, in mare, o diferenta
destul de mica fata de plamanii celor bolnavi). Aceasta este singura problema plauzibila la care ma pot gandi.

c) Ce planuri aveti in continuare?

Cred ca vom incerca, ca echipa, sa luam drept model INCA un algoritm nou (pana acum am avut ca model 4 sau 5 algoritmi diferiti pentru 
a reusi sa avem rezultatele pe placul nostru). Acest nou algoritm foloseste deja masti, daca nici asta nu merge, nu stiu 
ce am mai putea face. O alta posibilitate pe care o am in vedere este restructurarea folderelor si a pozelor de care dispunem, 
pentru a vedea daca rezolvam problema descrisa la b).
