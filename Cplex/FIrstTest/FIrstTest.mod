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
 
 dvar int x [esami];
 dvar int dummy;
 
 minimize dummy;
 
 subject to {
	forall (esame in esami) GiornoAssegnatoMinoreGiorno : x[esame] <= numero_giorni;
	forall (esame in esami) GiornoAssegnatoMaggiore0 : x[esame] >= 1;

	forall (esame1 in esami, esame2 in esami) DistanzaMinima : abs(x[esame1]-x[esame2]) * abs(esame1-esame2) >= (distanza_minima_stesso_semestre-dummy)* abs(esame1-esame2);
	MinimoDummy: dummy >= 0;
	
}