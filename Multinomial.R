library(rcompanion)
library(car)
library(pROC)
library(ResourceSelection)
library(LogisticDx)
library(generalhoslem)
library(robustbase)

library(readxl)

library(foreign)
library(nnet)
library(ggplot2)
library(reshape2)

library(RVAideMemoire)
library(DescTools)
library(readr)
library(generalhoslem)
library(dplyr)
library(data.table)

setwd("C:/Users/Pacho Lara/Documents/UN/MLG_2019_II")
source("macros.txt")
        
Datos_Limpios_modelo <- read_excel("ADS4A/Modelo/Datos_Limpios_modelo.xlsx")

colnames(Datos_Limpios_modelo)


model<-glm(ORDEN~FAMILIA_TEXTURAL, data=Datos_Limpios_modelo, family = binomial)

ORDEN  <-  relevel(Datos_Limpios_modelo$ORDEN) 

?relevel

model<-multinom(ORDEN~FAMILIA_TEXTURAL, data=Datos_Limpios_modelo)

summary(model)


Datos_Limpios_modelo_2 <- read_csv("C:/Users/Pacho Lara/Documents/ADS4A/Modelo/Datos_Limpios_modelo_2.csv")

colnames(Datos_Limpios_modelo_2)

Datos_Limpios_modelo_2$TIPO_OBSERVACION<-as.factor(Datos_Limpios_modelo_2$TIPO_OBSERVACION)
Datos_Limpios_modelo_2$CLIMA_AMBIENTAL<-as.factor(Datos_Limpios_modelo_2$CLIMA_AMBIENTAL)
Datos_Limpios_modelo_2$CLASE_PENDIENTE<-as.factor(Datos_Limpios_modelo_2$CLASE_PENDIENTE)
Datos_Limpios_modelo_2$REGIMEN_TEMPERATURA<-as.factor(Datos_Limpios_modelo_2$REGIMEN_TEMPERATURA)
Datos_Limpios_modelo_2$REGIMEN_HUMEDAD<-as.factor(Datos_Limpios_modelo_2$REGIMEN_HUMEDAD)
Datos_Limpios_modelo_2$DRENAJE_NATURAL<-as.factor(Datos_Limpios_modelo_2$DRENAJE_NATURAL)
Datos_Limpios_modelo_2$H1_NOMENCLATURA<-as.factor(Datos_Limpios_modelo_2$H1_NOMENCLATURA)
Datos_Limpios_modelo_2$H1_COLOR_MATRIZ_HUMEDO1<-as.factor(Datos_Limpios_modelo_2$H1_COLOR_MATRIZ_HUMEDO1)
Datos_Limpios_modelo_2$H2_NOMENCLATURA<-as.factor(Datos_Limpios_modelo_2$H2_NOMENCLATURA)
Datos_Limpios_modelo_2$EPIPEDON<-as.factor(Datos_Limpios_modelo_2$EPIPEDON)
Datos_Limpios_modelo_2$FAMILIA_TEXTURAL<-as.factor(Datos_Limpios_modelo_2$FAMILIA_TEXTURAL)
Datos_Limpios_modelo_2$ORDEN<-as.factor(Datos_Limpios_modelo_2$ORDEN)
Datos_Limpios_modelo_2$CONTENIDO_CENIZA_VOLCANICA<-as.factor(Datos_Limpios_modelo_2$CONTENIDO_CENIZA_VOLCANICA)


#y_test <- read_csv("ADS4A/Modelo/y_test.csv", col_names = FALSE)
#y_train <- read_csv("ADS4A/Modelo/y_train.csv",col_names = FALSE)
X_test <- read_csv("C:/Users/Pacho Lara/Documents/ADS4A/Modelo/X_test.csv", col_names = FALSE)
X_train <- read_csv("C:/Users/Pacho Lara/Documents/ADS4A/Modelo/X_train.csv",col_names = FALSE)

#y_test<-na.omit(t(as.data.frame(list(c(y_test)))+1))
#y_train<-na.omit(t(as.data.frame(list(c(y_train)))+1))
X_test<-na.omit(t(as.data.frame(list(c(X_test)))+1))
X_train<-na.omit(t(as.data.frame(list(c(X_train)))+1))

#y_test<-Datos_Limpios_modelo_2[y_test,]%>%select(ORDEN)
#y_train<-Datos_Limpios_modelo_2[y_train,]%>%select(ORDEN)

X_test<-Datos_Limpios_modelo_2[X_test,]
X_train<-Datos_Limpios_modelo_2[X_train,]

y_test<-as.data.frame( X_test%>%select(ORDEN))
y_train<-as.data.frame(X_train%>%select(ORDEN))

#ORDEN  <-  relevel(X_train$ORDEN) 


#table(Datos_Limpios_modelo_2$IGUALDAD)
#summary(Datos_Limpios_modelo_2)
t <- proc.time() # Inicia el cronómetro
model<-multinom(ORDEN~ TIPO_OBSERVACION+CLIMA_AMBIENTAL+CLASE_PENDIENTE+           
                       REGIMEN_TEMPERATURA+REGIMEN_HUMEDAD+DRENAJE_NATURAL+           
                       H1_NOMENCLATURA+H1_ESPESOR+H1_COLOR_MATRIZ_HUMEDO1+
                       H1_RESULTADO_ph+H2_NOMENCLATURA+H2_ESPESOR+                
                       EPIPEDON+ FAMILIA_TEXTURAL+LATITUD +LONGITUD+ALTITUD+                 
                       `PROFUNDIDAD MAXIMA`+CONTENIDO_CENIZA_VOLCANICA, data=X_train)


proc.time()-t    # Detiene el cronómetro
# Calculate z-values
t <- proc.time() 

zvalues <- summary(model)$coefficients / summary(model)$standard.errors
# Show z-values
#zvalues

pnorm(abs(zvalues), lower.tail=FALSE)*2 > 0.05
proc.time()-t  


PseudoR2(model, which = "Nagelkerke")

TEST<-X_test%>%select(-c("IGUALDAD","ORDEN"))

#Y_predic_train<-as.data.frame(predict(model, newdata=TEST))
Y_predic<-as.data.frame(predict(model, newdata=TEST))
  

table(y_test==Y_predic)[2]/2264
table(y_test==Y_predic)[1]/2264

matrix<-cbind(Y_predic,y_test)
colnames(matrix)<-c("Pre","test")
dcast(matrix, Pre ~ test)


#1  Evaluacion de Puntos influyentes 

X_train_1<-X_train%>%filter(ORDEN %in% c("Andisol","Entisol"))

logit1 <- glm(ORDEN~ TIPO_OBSERVACION+CLIMA_AMBIENTAL+CLASE_PENDIENTE+REGIMEN_TEMPERATURA+REGIMEN_HUMEDAD+DRENAJE_NATURAL+           
                    H1_NOMENCLATURA+H1_ESPESOR+H1_COLOR_MATRIZ_HUMEDO1+H1_RESULTADO_ph+H2_NOMENCLATURA+H2_ESPESOR+                
                    EPIPEDON+ FAMILIA_TEXTURAL+LATITUD +LONGITUD+ALTITUD+`PROFUNDIDAD MAXIMA`+CONTENIDO_CENIZA_VOLCANICA, 
                    data=X_train, family = binomial(link='logit'))

X_train_2<-X_train%>%filter(ORDEN %in% c("Andisol","Histosol"))

logit2 <- glm(ORDEN~ TIPO_OBSERVACION+CLIMA_AMBIENTAL+CLASE_PENDIENTE+REGIMEN_TEMPERATURA+REGIMEN_HUMEDAD+DRENAJE_NATURAL+           
                H1_NOMENCLATURA+H1_ESPESOR+H1_COLOR_MATRIZ_HUMEDO1+H1_RESULTADO_ph+H2_NOMENCLATURA+H2_ESPESOR+                
                EPIPEDON+ FAMILIA_TEXTURAL+LATITUD +LONGITUD+ALTITUD+`PROFUNDIDAD MAXIMA`+CONTENIDO_CENIZA_VOLCANICA, 
              data=X_train_2, family = binomial(link='logit'))

X_train_3<-X_train%>%filter(ORDEN %in% c("Andisol","Inceptisol"))

logit3 <- glm(ORDEN~ TIPO_OBSERVACION+CLIMA_AMBIENTAL+CLASE_PENDIENTE+REGIMEN_TEMPERATURA+REGIMEN_HUMEDAD+DRENAJE_NATURAL+           
                H1_NOMENCLATURA+H1_ESPESOR+H1_COLOR_MATRIZ_HUMEDO1+H1_RESULTADO_ph+H2_NOMENCLATURA+H2_ESPESOR+                
                EPIPEDON+ FAMILIA_TEXTURAL+LATITUD +LONGITUD+ALTITUD+`PROFUNDIDAD MAXIMA`+CONTENIDO_CENIZA_VOLCANICA, 
              data=X_train_3, family = binomial(link='logit'))

X_train_4<-X_train%>%filter(ORDEN %in% c("Andisol","Molisol"))

logit4 <- glm(ORDEN~ TIPO_OBSERVACION+CLIMA_AMBIENTAL+CLASE_PENDIENTE+REGIMEN_TEMPERATURA+REGIMEN_HUMEDAD+DRENAJE_NATURAL+           
                H1_NOMENCLATURA+H1_ESPESOR+H1_COLOR_MATRIZ_HUMEDO1+H1_RESULTADO_ph+H2_NOMENCLATURA+H2_ESPESOR+                
                EPIPEDON+ FAMILIA_TEXTURAL+LATITUD +LONGITUD+ALTITUD+`PROFUNDIDAD MAXIMA`+CONTENIDO_CENIZA_VOLCANICA, 
              data=X_train_4, family = binomial(link='logit'))

par(mfrow = c(2, 2), oma = c(0, 0, 4, 0))
Cookdis_glm(logit1,identify=2)
Cookdis_glm(logit2,identify=3)
Cookdis_glm(logit3,identify=2)
Cookdis_glm(logit4,identify=2)

