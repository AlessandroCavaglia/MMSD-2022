/*********************************************
 * OPL 12.8.0.0 Model
 * Author: Alessandro
 * Creation Date: 21/giu/2022 at 17:26:14
 *********************************************/
 int numero_giorni =...;
 int numero_esami =...;
 
 range giorni= 1..numero_giorni;
 range esami = 1..numero_esami;
 
 int distanza_minima_stesso_semestre=...;
 
 dvar boolean x [esami][giorni];
 dvar int dummy;
 
 minimize dummy;
 
 subject to {
  
 	//Per ogni esame lo assegno una sola volta
  	forall(esame in esami)sum(giorno in giorni) x[esame][giorno] == 1;
  	//Per ogni coppia di esami devono essere almeno distanti dummy+distanza_minima_stesso_semestre
 	forall(esame1 in esami, giorno1 in giorni) forall(esame2 in esami, giorno2 in giorni) 
 		 if(esame1!=esame2)	//If � sostituibile moltiplicando entrambe le parti per abs(esame1-esame2)
 		 	((abs(giorno1-giorno2)-1) *(x[esame2][giorno2]* x[esame1][giorno1])) //Distanza tra i due giorni se sono entrambi a 1
 		 			 + (numero_giorni * (1 - (x[esame2][giorno2]* x[esame1][giorno1])))//Numero dei giorni totale se almeno uno � a 0
 		 			  >= distanza_minima_stesso_semestre-dummy;	//Distanza minima
	
	//Dummy deve essere sempre almeno positiva se no minimizzando andiamo in negativo
	MinimoDummy: dummy >= 0;
}