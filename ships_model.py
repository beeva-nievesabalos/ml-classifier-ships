# -*- coding: utf-8 -*-
import numpy as np
from scipy import sparse as sp
from sklearn import multiclass
from sklearn.cross_validation import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import os
from sklearn.externals import joblib

model = joblib.load('models/ships_model.txt')
words = joblib.load('models/ships_words.txt')


def predictionShips(email):
    print("\nFichero DATA: " + email)
    # Abro el fichero a voy a leer
    f = open(email, 'r')
    # Matriz X
    files=[]
    files.append(f.read())
    filess=[f.split() for f in files]
    print("\nNúmero de ficheros:")    
    print len(filess) 

    # PARTE 2: procesamiento de datos, conteo de palabras 
    print("\nNúmero de palabras (total):")    
    print len(words) 
    
    indices=[]
    indptr=[0]
    c=0
    for index,ff in enumerate(filess):
        d=[words[w] for w in ff if w in words]
        c+=len(d)
        indptr.append(c)
        indices.extend(d)

    # Vector X: matriz con las palabras   
    X=sp.csr_matrix((np.ones(len(indices)),indices,indptr),shape=(len(files),len(words)))
    #Prediccion
    ypred = model.predict(X)
    yprob = model.predict_proba(X)
    print("\nProbabilidad prediccion:")
    print(yprob)
    print("\nClass predicted:") 
    print(ypred[0])
    return [ypred[0],yprob]
    
#fichero = "../Output/Posiciones Coasters/msg_9.txt"
#prediccion = predictionShips(fichero)
#print("\n[Class predicted, [p0  p1  p2]]:") 
#print(prediccion)