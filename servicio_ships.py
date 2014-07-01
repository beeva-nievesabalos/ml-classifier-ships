# -*- coding: utf-8 -*-
"""
Created on Thu May 29 15:33:24 2014

@author: nieves
"""

from ships_model import predictionShips
from flask import Flask, request, url_for, render_template, jsonify, Response
app = Flask(__name__)

#flag_json = 1 (json) = 0 (string)
def predictShips(email, flag_json):
  print("\npredictShips!!")
  shipsClass = predictionShips(email)
  #phonesstring = "[" + ''.join(phones[:-1]) + "]"
  #phonesarrayjson = ast.literal_eval(phonesstring)  

  if flag_json:  #json
    resultado = jsonify({'ships_prediction': shipsClass[0], 'prob_c0': shipsClass[1][0], 'prob_c1': shipsClass[1][1], 'prob_c2': shipsClass[1][2]})
  else: #string
    resultado = json.dumps({'ships_prediction': shipsClass[0], 'prob_c0': shipsClass[1][0], 'prob_c1': shipsClass[1][1], 'prob_c2': shipsClass[1][2]})
  
  return resultado


#---------------------- ROUTES --------------------------
@app.route('/ships', methods=['GET', 'POST'])
def ships():
  #'POST' ya que viene de un formulario
  if request.method == 'POST':
    if request.headers['Content-Type'] == 'application/x-www-form-urlencoded':
      print("\n-------- request POST form['email'] -------")
      print(request.form['email'])
      email = str(request.form['email'])
      response = predictShips(email, 1) # devuelve json

      #### para evitar CORS ######
      response.headers.add_header('Access-Control-Allow-Origin', '*')
      response.headers['Content-Type'] = 'application/json'
      response.status_code = 200
      print("\n-------- JSON response -------")
      print(response)
      print("\n")

      return response
  #'GET' permite CORS usando JSONP
  if request.method == 'GET':
      print("\n-------- request GET request.args.get('....') -------")
      print("CALLBACK =" + request.args.get('callback'))
      print("email =" + request.args.get('email'))
      idcallback = str(request.args.get('callback'))
      email = str(request.args.get('email'))
      json_string = predictShips(email, 0) #devuelve string

      respuesta = Response(idcallback + "("+ json_string + ");")
      print("\n-------- JSON response -------")
      print(respuesta)
      print("\n")
      
      return respuesta
 
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8021)