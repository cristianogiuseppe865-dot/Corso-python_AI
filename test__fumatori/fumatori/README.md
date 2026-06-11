# fumatori
Analisi dataset dei fumatori 14enni dal 1980 al 2015
Analisi dei fumatori in Italia
Questo repository contiene un progetto di analisi dati sulla percentuale di fumatori in Italia, con focus su andamento temporale, differenze di genere, confronto tra aree geografiche e un primo esperimento di modellazione predittiva basato su machine learning. I file principali del progetto sono un dataset in formato CSV e un notebook Jupyter con pulizia, visualizzazioni, analisi statistiche e modello di regressione.

Contenuto del repository
fumatori_italia-2.csv: dataset con osservazioni per anno, sesso, macro-area geografica e totale Italia.
test_fumatori.ipynb: notebook Jupyter con l'intero flusso di lavoro, dalle analisi esplorative alle visualizzazioni fino alla fase di training del modello.

Obiettivo del progetto
L'obiettivo è studiare come è cambiata nel tempo la percentuale di fumatori in Italia, evidenziando le differenze tra uomini e donne e tra le diverse aree del Paese. Nel notebook vengono inoltre calcolate statistiche descrittive, percentili, deviazioni standard e viene costruito un modello di regressione per stimare la percentuale nazionale dei fumatori a partire dalle altre variabili disponibili.

Struttura del dataset
Il dataset include le seguenti colonne:
Anno: anno di rilevazione.
Sesso: categoria del campione (Maschi, Femmine)
​Nordovest, Nordest, Centro, Sud, Isole: percentuale di fumatori nelle macro-aree italiane.
Italia: percentuale complessiva nazionale.


L'intervallo temporale copre osservazioni dal 1980 al 2015 per entrambi i sessi, con più rilevazioni intermedie. Questo permette sia analisi longitudinali sia confronti territoriali e di genere.

Cosa è stato fatto nel notebook
1. Esplorazione iniziale dei dati
Nel notebook viene caricato il dataset e vengono ispezionate struttura, colonne e valori numerici per impostare correttamente le successive analisi. La base dati viene poi usata per confrontare l'evoluzione del fenomeno nel tempo e tra gruppi diversi.
​

2. Analisi descrittiva e statistica
Sono state calcolate misure come media e deviazione standard per le macro-aree geografiche, così da valutare il livello medio di fumatori e la variabilità nel tempo. Nel notebook compare anche una sezione dedicata ai percentili e alla distribuzione dei dati italiani per sesso.
​

3. Visualizzazioni
Nel notebook sono presenti diversi grafici, tra cui:
​

grafici a barre con media e deviazione standard per area geografica;
​

boxplot per osservare la distribuzione dei fumatori in Italia per sesso;
​

line plot temporali per mostrare l'andamento storico dal 1980 al 2015;
​

grafici comparativi tra macro-aree per individuare differenze territoriali.
​

Dalle note presenti nel notebook emerge una diminuzione progressiva dei fumatori maschi nel tempo, mentre per le femmine l'andamento appare più stabile. Viene inoltre osservato che Sud e Isole mostrano una variabilità più alta rispetto ad altre aree in alcune analisi.
​

4. Preparazione dei dati per il modello
Per la parte di machine learning la variabile Sesso viene trasformata in formato numerico, con mappatura Maschi = 1 e Femmine = 0. Successivamente vengono definite le feature Anno, Sesso, Nordovest, Nordest, Centro, Sud, Isole, mentre la variabile target è Italia.
​

Il dataset viene poi suddiviso in training set e test set con train_test_split, ottenendo 41 righe per il training e 11 per il test. Le feature vengono standardizzate con StandardScaler, applicando fit_transform solo sul training e transform sul test per evitare leakage.
​

5. Modellazione
Nel notebook è presente una sezione di creazione del modello di regressione per prevedere la percentuale di fumatori in Italia. È incluso anche un grafico finale che confronta valori reali e predizioni del modello sul test set.
​

Principali osservazioni emerse
In base alle annotazioni inserite nel notebook, il progetto mette in evidenza alcuni pattern interpretativi:
​

forte calo della percentuale di fumatori maschi tra 1980 e 2015;
​

andamento femminile più stabile e concentrato;
​

riduzione del divario tra uomini e donne nel corso del tempo;
​

maggiore variabilità di alcune aree, in particolare Sud e Isole, in certe analisi descrittive.
​

Librerie utilizzate
Dal notebook risultano utilizzate librerie Python tipiche per data analysis e machine learning, tra cui pandas, matplotlib, seaborn e componenti di scikit-learn come train_test_split e StandardScaler. La parte di modellazione e visualizzazione è quindi coerente con un workflow classico di analisi dati in ambiente Jupyter.
​

Come eseguire il progetto
Requisiti
È consigliato usare Python 3.10+ o 3.11+ in un ambiente virtuale. Servono almeno queste librerie:
pip install pandas matplotlib seaborn scikit-learn notebook

Avvio del notebook
Clonare il repository.

Aprire la cartella del progetto.

Avviare Jupyter Notebook o JupyterLab.

Aprire test_fumatori.ipynb.

Eseguire le celle in ordine per riprodurre analisi, grafici e modello.

Possibili miglioramenti
Il progetto può essere esteso in diversi modi:
confrontare più algoritmi di regressione;
migliorare la pulizia e la documentazione del notebook separando meglio analisi descrittiva e parte predittiva;
esportare grafici e risultati in report finali o dashboard.

Conclusione
In Italia i fumatori sono diminuiti molto tra il 1980 e il 2015. Il calo è stato forte soprattutto tra gli uomini, mentre tra le donne è stato più graduale.
