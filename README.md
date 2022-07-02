# ori_projekat_2022
ORI projekat 2022 - Reversi strateska igra - Nikola Sovilj, SW75/2019


Članovi tima: Nikola Sovilj, SW75/2019, grupa 5

Asistent: Milica Škipina

Problem koji se rešava: Implementacija bota koji u ovoj igri pronalazi niz najpovoljnijih poteza u skladu sa datom situacijom na tabli, koji ga dovode do pobede. Cilj je realizovati režim gde će čovek igrati protiv bota, unosom odgovarajućih koordinata za izabarani sledeći potez. Postoje crne i bele figure, koje se međusobno uklanjaju sa table, a pobednik je igrač koji ukloni sve protivničke figure.

Algoritam: Minimax algoritam uz korišćenje stabla kao strukture podataka prilikom odabira narednih poteza.

Metrika za merenje performansi: Meriće se vreme trajanja igre, odnosno koliko brzo bot može da pobedi saigrača. Pored toga, vreme odabira poteza od strane bota ne bi trebalo da bude predugačko (max 5s).

Validacija rešenja: Rešenje će biti prikazano u vidu konzolne aplikacije u režimu čovek VS bot. Jasno će biti predstavljene crne, bele figure i dozvoljene pozicije za potez na tabli.


===========INFORMACIJE O POKRETANJU PROJEKTA==================


-Za pokretanje projekta, nephodno je posedovati PyCharm IDE
-Source kod i poster se nalaze na master grani
-Igra se pokreće run-ovanjem main.py modula
-Igra je kreirana u režimu čovek VS bot, gde čovek poseduje crne a bot bele figure


