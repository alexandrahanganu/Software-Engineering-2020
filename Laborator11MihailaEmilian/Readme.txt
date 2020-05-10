a) Ce ati reusit sa faceti in aceasta iteratie?
  Am resuit sa fac impreuna cu Teo si cu Iulian si Adrian sa facem parcurgerea pe toate cele 3 categorii(FrontBack....), incarcand toate pozele si antrenand modelul cu acestea. Vazand ca acesta nu da rezultate bune am eliminat din seturile de poze date de Denis acele poze in minoritate ce sunt foarte distinctive fata de celelalte(acele poze ce aveau predominant negru in poza si nu gri). 
  Am testat pe ambele seturi de date (atat cele gri si cele negre dar din pacate nu am ajuns la un rezultat favorabil. Astazi am schimbat si ne-am "jucat" cu variabilele de care ne-a atras atentiaGeorgiana Coca si am testat eu 14 dintre aceste posibile rulari, impreuna cu Teo acoperind amandoi toate posibilitatile. Am reusit cu totii sa facem ca programul sa ruleze.
	Am cautat pe internet anumiti algoritmi ce folosesc poze prelucrate cu masti si din pacate nu am gasit. Am facut initial cu totii label-uri pentru toate bolile dar dupa ce am vazut ca nu merge algoritmul am ramas doar cu label-uri pentru tuberculoza.
	Am facut media pentru toate pozele pentru un pacient(cu putin ajutor de la Alexandra).
	Am trecut de la codul cu tensorflow la keras. Am scris restructurat codul si am scris algoritmul cu keras.
	Am incarcat pe grupul nostru de discord  ss-uri cu toate csv-urile dupa ce am rulat.
	Am cautat despre optimizarea programului de CNN folosind keras.tuner, si multe alte metode de optimizare.
	Algoritmul este aproape terminat dar avem problemele expuse mai jos.
	Dupa toate rurarile de saptamana asta inca nu am descoperit unde este problema reala(seturi de date/antrenare) deoarece am reusit sa vedem
incetul cu incetul ca path-urile sunt ok label-urile sunt puse ok pe fiecare poza.
b) Ce probleme ati avut?
	Pozele au fost cu diferite nuante de gri pentru fiecare pacient. Unii pacienti avand poze doar cu nuante de negru. 
	Nu am reusit sa ajungem la un rezultat ok. Am testat pentru un anumit numar de poze si erau momente cand dadea apropiat de target dar
	numai pentru unele dintre ele. 
	Avem majoritatea rurarilor au peste 0.7 predictia si nu prea scad pentru cei sanatosi.
	La pacientul 17 la only right lung sunt masti pentru ambii plamani
c) Ce planuri aveti in continuare?
	Probabil sa luam un alt algoritm sa vedem deoarece pana acum am testat pe 3 algoritmi si toate dau rezultate la fel.
	Sau sa il perfectionam pe acesta dupa indicatiile de pe internet.
