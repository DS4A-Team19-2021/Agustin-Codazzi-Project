# Agustin-Codazzi-Project

The following credentials are to be used to login to the [application](https://www.cats19.tech) 
-	ID: IGAC_user
-	Password: 123456

-------

## 1.	Description

This project was conceived out of the necessity from the _Instituto Geográfico Agustín Codazzi_ (IGAC) of having a tool capable of performing automatic soil taxonomy classification, using data collected in the field. 

This tool seeks to aid and make easier the process of taxonomic soil classification performed by the [edaphologists](https://en.wikipedia.org/wiki/Edaphology) from the _Instituto_, whose goal is to make an inventory and cartography of the soils in Colombia.  For this purpose, several models were fitted and tested using a database with more than 12,000 observations, which recorded 209 different variables, collected in the _Cundiboyacense_ Plateau.

This classification is based on the [USDA’s methodology](https://www.nrcs.usda.gov/wps/portal/nrcs/main/soils/survey/class/). The current application is capable of classifying the first category in said taxonomic hierarchy (_i.e._ Order).

In order to achieve this, the following steps were taken:
-	[USDA's Soil Taxonomy]() was studied
-	EDA
-	Data Cleaning
-	Statistical Classification Algorithms
-	Dashboard
-	Maps
-	Graphs
-	Databases management
-	Backend development

This Project seeks to become the foundations of a deeper automatic taxonomic classification (_i.e._ Suborder, Great Group, Sub Group, etc.) that may be achieved by fitting further models. Additionally,  data-entry standardization is highly recommended, in order to improve the databases quality and minimizing __Data Cleaning__ processes in the future.

The Project is called ___CATS___, which stands for __Clasificador Automático Taxonómico de Suelos__ in Spanish, or Automatic Taxonomic Soil Classifier. 


## 2.	Model
	
In order to perform the taxonomic classification, several models were fitted, such as:

-	Random Forests
-	Multinomial Regressions
-	Stacked Models

It was concluded that __Random Forests__ was the most appropriate algorithm in solving this classification problem. This was selecting, broadly, by balancing accuracy, speed and parsimony. 
 
The Random Forests were done using the [`scikit-learn` library]( https://scikit-learn.org/). These were optimized by testing more than 70 different forests with different parameters. The selection of the best was based on the [Out-of-Bag Error](https://en.wikipedia.org/wiki/Out-of-bag_error). 

The final model, obtained an __Accuracy__ of 94.2% using the __Test Dataset__. 


## 3.	App Use

By using the app, it’s possible to:
*	Obtain predictions of data uploaded by the user
*	Visualize and Interact with user-uploaded data and the original database
 
The usage process is as follows:
1.	Log in using authorized credentials
2.	Visualize and interact with the data from the original database using the __Map__, __Treemap__ and __Pivot Table__
3.	Filter the data using the filters located above the map
4.	Obtain detailed information by hovering over each entry point plotted in the map
5.	Upload valid files (`.csv`, `.xls` or `.xlsx`) (The maps and graphs will be automatically updated)
7.	Interact with the map and graphs
8.	Obtain and interpret the classifications performed by the model


## 4.	API

If the user wishes to by-pass the Dashboard, this can be done by interacting directly with the project's API.

Currently there are 3 API Endpoints:

1.	`/api/status/`
	Pings the API; the API responds with a boolean, whether the API is online and able to respond, or not.
	

2.	`/api/predict`
	With this, the user can request a __single__ prediction based on a set of 9 variables (__see Sample `JSON` Structure below__) that are passed in a `JSON`-like structure. The response, in again a `JSON` structure, the most likely prediction and the probability of being in each of the 5 possible taxonomic orders.

3.	`/api/predict_many`
	At this request, the API is able to perform several predictions in a single call.  A `JSON` format must be passed, containing the multiple observations to be predicted, based on the set of 9 variables (__see Sample `JSON` Structure below__). Once again, the response is ordered in a `JSON` format which contains the predictions, as well as the probabilities of each. This is a highly efficient method of communication with the application, considerably reducing the response time by __several orders of magnitude__. For example, this method is capable of performing up to 4000 classifications in less than a second. 

This is the only way in which the probability of each classification can be obtained. 

**NOTE** Numerical values __CAN'T__ contain _null_ values. 


### Sample `JSON` structure

The following is a sample of how a request would look like in the `JSON` structure:

```
{'ALTITUD': 291.0,
 'CONTENIDO_CENIZA_VOLCANICA': 'False',
 'DRENAJE_NATURAL': 'Pobre',
 'EPIPEDON': 'Ocrico',
 'FAMILIA_TEXTURAL: 'Fina',
 'H1_ESPESOR': 17.0,
 'H1_RESULTADO_ph': 4.5,
 'H2_ESPESOR: 38.0,
 'PROFUNDIDAD_MAXIMA': 110.0
}
```


### Request `JSON` structure detail

The following table details the characteristics of the valid structure. All fields __must__ be included. It is worth noting that the Random Forest algorithm can deal with `null` values, however, using non-null values is encouraged for a better prediction.

| Variable                   | Type   | Title                      |
|----------------------------|--------|----------------------------|
| ALTITUD                    | number | Altitud                    |
| CONTENIDO_CENIZA_VOLCANICA | string | Contenido Ceniza Volcanica |
| DRENAJE_NATURAL            | string | Drenaje Natural            |
| EPIPEDON                   | string | Epipedon                   |
| FAMILIA_TEXTURAL           | string | Familia Textural           |
| H1_ESPESOR                 | number | H1 Espesor                 |
| H1_RESULTADO_ph            | number | H1 Resultado pH            |
| H2_ESPESOR                 | number | H2 Espesor                 |
| PROFUNDIDAD_MAXIMA         | number | Profundidad Maxima         |


![imagen](https://raw.githubusercontent.com/DS4A-Team19-2021/Agustin-Codazzi-Project/main/Images/logo_igac_fondo_blanco.png)
