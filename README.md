ml-classifier-ships
===================

Machine Learning - Email classifier - Ships


---------------------------------------------------------------------

1) **CLASIFICADOR:** ships_classifier.py
- Multiclass One Vs Rest Classifier
- Logistic Regression


Correos que entran en Posiciones (Barcos). Clasificación:

- coasters       c   0
- handies        h   1
- panamax/capes  p   2

Ejemplo de ejecución:

	Número de correos TOTAL:
	16362

	Número de palabras (total):
	137144

	Número de indices:
	4747106

	============ EVALUATION ================

	Accuracy Score:
	0.93680479159

	=======================================

	Confusion matrix:
	[[5083  368   18]
	 [ 289 7345  148]
	 [  36  175 2900]]


INPUT: 
- Necesita la carpeta 'output' donde están los correos en formato .txt

OUTPUT: 
- Tras crear el modelo, lo guarda en 'models/ships_model.txt'.
- El conjunto de palabras se guarda en 'models/ships_words.txt'.
- Accuracy y matriz de confusión.


---------------------------------------------------------------------


2) **PREDICCIÓN:** ships_model.py

Función que recibe un correo y utilizando el modelo creado en (1) previamente, devuelve la clasificación + probabilidad.

Ejemplo de ejecución:

	Fichero DATA: ../Output/Posiciones Coasters/msg_9.txt

	Número de ficheros:
	1

	Número de palabras (total):
	137144

	Probabilidad prediccion:
	[[  9.99837601e-01   2.80208724e-05   1.34377989e-04]]

	Class predicted:
	0

INPUT:
- Fichero recibido a clasificar.
- Carga el modelo de 'models/ships_model.txt' y el conjunto de palabras de 'models/ships_words.txt'.

OUTPUT:
- Clase predicha + probabilidades de las tres clases

	[Class predicted, [p0  p1  p2]]:
	[0, array([[  9.99837601e-01,   2.80208724e-05,   1.34377989e-04]])]


---------------------------------------------------------------------


3) **API REST PREDICCIÓN:** servicio_ships.py
Servicio REST que devuelve JSON o string. 
Recibe un correo desde POST/GET:
* POST si viene de un formulario
* GET permite CORS usando JSNOP

INPUT: 
- Función de predicción creada en (2)
	from ships_classifier import predictionShips

OUTPUT:
- Clase predicha + probabilidades de las tres clases

	[Class predicted, [p0  p1  p2]]:
	[0, array([[  9.99837601e-01,   2.80208724e-05,   1.34377989e-04]])]