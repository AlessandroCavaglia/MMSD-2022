/*********************************************
 * OPL 12.8.0.0 Model
 * Author: Alessandro
 * Creation Date: 21/giu/2022 at 17:26:14
 *********************************************/
 int M =...;	//Numero giorni
 int N =...;	//Numero esami
 int L=...;		//Numero laboratori
 int A=...;		//Numero aule
 int S=...;		//Numero della sessione
 int MI=...;	//Valore di maxIncrease
 int DMA=...;	//Distanza minima tra appelli dello stesso esame
 int DMAS=...;	//Distanza minima appelli dello stesso semestre
 int LNAE[1..N]=...;	//Lista associazione numero appelli - esami
 int LAE[1..N][1..3] =...;	//Lista associazione anni - esami (Falso booleano)
 int LSE[1..N][1..2] =...;	//Lista associazione semestri - esami (Falso booleano)
 int LRLE[1..N][1..L]=...;	//Lista associazione risorse di laboratorio - esami
 int LRAE[1..N][1..A]=...;	//Lista associazione risorse aule - esami
 float PGE[1..N][1..M]=...;	//Lista preferenze giorno - esame
 
 
 
 
 range giorni= 1..M;
 range esami = 1..N;
 range aule = 1..A;
 range laboratori = 1..L;
 
 dvar boolean x [esami][giorni];
 dvar int dummy;
 
 minimize dummy;
 
 subject to {
	
	//Dummy deve essere sempre almeno positiva se no minimizzando andiamo in negativo
	MinimoDummy: dummy >= 0;
	//Per ogni esame lo assegno pari al suo numero di appelli
  	NumeroEsattoAppelli: forall(esame in esami)sum(giorno in giorni) x[esame][giorno] == LNAE[esame];
  	//Verificare che non siano superati i limiti delle aule
  	LimiteSlotAule : forall(aula in aule)forall(giorno in giorni)sum(esame in esami) x[esame][giorno]*LRAE[esame][aula]<=2;
  	//Verificare che non siano superati i limiti dei laboratori
  	LimiteSlotLaboratori : forall(laboratorio in laboratori)forall(giorno in giorni)sum(esame in esami) x[esame][giorno]*LRLE[esame][laboratorio]<=3;
  	
}