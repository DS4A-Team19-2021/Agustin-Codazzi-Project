# Agustin-Codazzi-Project

## 1.	Description

This project was conceived out of the necessity from the _Instituto Geográfico Agustín Codazzi_ (IGAC) of having a tool capable of performing automatic soil taxonomy classification, using data obtained in the field. 

This tool seeks to aid and make easier the process of classification performed by the edaphologist from the Instituto, whose goal is performing an inventory and cartography of soils in Colombia.  For this purpose, several models where trained using a database with more than 12,000 observations, which recorded 209 different variables, collected in the _Cundiboyacense_ Plateau.

This classification is based on the [USDA’s methodology]( https://www.nrcs.usda.gov/wps/portal/nrcs/main/soils/survey/class/). The current project is capable of classifying the first category in said taxonomic hierarchy (_i.e._ Order).

In order to achieve this, among other things, the following processes were done:
-	Taxonomic Soil Classification research??
-	EDA
-	Data Cleaning
-	Statistical Classification Algorithms
-	Dashboard
-	Maps
-	Graphs
-	Databases management
-	Backend development

This Project seeks to become the foundations of a deeper taxonomic classification (_i.e._ Suborder, Great Group, Sub Group, etc.) by adding further models. Additionally, suggesting data entries standardization seeking to improve the databases quality and reducing the Data Cleaning processes in the future. 
The Project is called CATS, which stands for __Clasificador AuTomático de Suelos__ in Spanish, or Automatic Soil Classifier. 

## 2.	Model
	
In order to perform the taxonomic classification, several models were tested, such as:
-	Random Forests
-	Multinomial Regressions
-	Stacked Models

It was concluded that __Random Forests__ was the most appropriate algorithm in solving this classification problem. This was selecting, broadly, by balancing accuracy, speed and parsimony. 
 
The Random Forests were done using the [`scikit-learn` library]( https://scikit-learn.org/). These were optimized by testing more than 70 different forests with different parameters. The selection of the best was based on the [Out-of-Bag Error](https://en.wikipedia.org/wiki/Out-of-bag_error). 

The final model, obtained an __Accuracy__ of 94.2% using the __Test Dataset__. 


## 3.	App Use

Using the app, it’s possible to:
*	Obtain predictions of data uploaded by the user
*	Visualize and Interact with user-uploaded data and the original database
 
The usage process is as follows:
1.	Log in using the authorized credentials
2.	Visualize and interact with the data from the original database using the __Map__, __Treemap__ and __Pivot Table__
3.	Filter the data using the filters located above the map
4.	Obtain detailed information hovering over each entry point
5.	Upload valid files (`.csv`, `.xls` or `.xlsx`)
6.	The maps and graphs will be automatically refreshed 
7.	Interact with the graphs
8.	Obtain and interpret the classifications performed by the model


## 4.	API

If the user wishes to by-pass the Dashboard, this can be done by interacting directly with the API. This requires the use of `.json` files. With this method, up to 2000 predictions can be obtained in X seconds. 

By interacting directly with the API, the output is the taxonomic classification and the probability of each of the possible outcomes (only obtained via this method). 



![imagen](https://raw.githubusercontent.com/DS4A-Team19-2021/Agustin-Codazzi-Project/main/Images/logo_igac_fondo_blanco.png)



