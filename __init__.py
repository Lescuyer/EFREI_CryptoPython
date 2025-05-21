from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html') #Comment3

key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

# ➕ Exercice 1 : Décryptage avec la clé de session
@app.route('/decrypt/<token>')
def decryptage(token):
    try:
        decrypted = f.decrypt(token.encode())
        return f"Valeur décryptée : {decrypted.decode()}"
    except InvalidToken:
        return "Erreur : Le token est invalide ou la clé ne correspond pas."

@app.route('/encrypt_custom/<key>/<valeur>')
def encrypt_custom(key, valeur):
    try:
        f_custom = Fernet(key.encode())
        token = f_custom.encrypt(valeur.encode())
        return f"Valeur encryptée avec votre clé : {token.decode()}"
    except Exception as e:
        return f"Erreur lors du chiffrement : {str(e)}"

@app.route('/decrypt_custom/<key>/<token>')
def decrypt_custom(key, token):
    try:
        f_custom = Fernet(key.encode())
        decrypted = f_custom.decrypt(token.encode())
        return f"Valeur décryptée avec votre clé : {decrypted.decode()}"
    except InvalidToken:
        return "Erreur : Token invalide ou clé incorrecte."
    except Exception as e:
        return f"Erreur lors du déchiffrement : {str(e)}"
                                                                                                                                                     
if __name__ == "__main__":
  app.run(debug=True)
