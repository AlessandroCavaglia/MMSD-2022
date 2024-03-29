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
 int LNG[1..N]=...;			//Lista associazione numeroGiorni - esame			
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
	//Per ogni esame lo assegno pari al suo numero di appelli * le giornate richieste
  	NumeroEsattoAppelli: forall(esame in esami)sum(giorno in giorni) x[esame][giorno] == LNAE[esame]*LNG[esame];
  	//Verificare che non siano superati i limiti delle aule
  	LimiteSlotAule : forall(aula in aule)forall(giorno in giorni)sum(esame in esami) x[esame][giorno]*LRAE[esame][aula]<=2;
  	//Verificare che non siano superati i limiti dei laboratori
  	LimiteSlotLaboratori : forall(laboratorio in laboratori)forall(giorno in giorni)sum(esame in esami) x[esame][giorno]*LRLE[esame][laboratorio]<=3;
  	//Distanza minima tra il primo e il secondo appello della stessa materia
  	DistanzaPrimoSecondoAppello: forall(esame in esami, giorno1 in giorni,giorno2 in giorni)
 		 if(giorno1!=giorno2 && abs(giorno1-giorno2) >= LNG[esame])		//Se i giorni sono diversi
 		 	((abs(giorno1-giorno2)-1) *(x[esame][giorno2]* x[esame][giorno1])) //Se entrambi gli esami sono in quelle date -> Distanza tra i due giorni
 		 			 + (M * (1 - (x[esame][giorno2]* x[esame][giorno1]))) //Se almeno uno degli esami non � in quelle date -> Numero dei giorni totale
 		 			  >= DMA;	//Distanza minima tra due appelli dello stesso esame
 	//Distanza minima tra esami della stessa sessione di esame
  	DistanzaEsamiStessaSessione: forall(esame1 in esami, esame2 in esami, giorno1 in giorni,giorno2 in giorni)
 		 if(esame1!=esame2 &&	//Se non sono lo stesso esame
 		 	 (LAE[esame1][1]==LAE[esame2][1] && LAE[esame1][2]==LAE[esame2][2] && LAE[esame1][3]==LAE[esame2][3]) &&	//Se sono lo stesso anno
 		 	 (LSE[esame1][1]==LSE[esame2][1] && LSE[esame1][2]==LSE[esame2][2])	//Se sono lo stesso semestre
 		 ) 
 		 	((abs(giorno1-giorno2)-1) *(x[esame1][giorno1]* x[esame2][giorno2]))  //Se entrambi gli esami sono in quelle date -> Distanza tra i due giorni
 		 			 + (M * (1 - (x[esame2][giorno2]* x[esame1][giorno1])))  //Se almeno uno degli esami non � in quelle date -> Numero dei giorni totale
 		 			  >= DMAS-dummy;	//Distanza minima tra due appelli dello stesso esame
 	//Verifica giorni indisponibilit�
 	GiorniIndisponibilita: forall(esame in esami, giorno in giorni) x[esame][giorno] <= PGE[esame][giorno];
 	
 	//Verifica assegnamento giornate multiple		
  	forall(esame in esami, giorno in 2..(M-LNG[esame]-1)) if(LNG[esame]>1) ((1-x[esame][giorno-1])*x[esame][giorno]* LNG[esame]) <= sum(index in giorno..giorno+LNG[esame]-1)x[esame][index];
}