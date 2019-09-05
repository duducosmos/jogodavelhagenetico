import pickle
from flask import Flask, url_for, render_template, jsonify, request, make_response
from flask import Response
from flask_socketio import SocketIO
from numpy import load, zeros

from jogodavelhagenetico.arvorejogodavelha import ArvoreJogoDaVelha
from jogodavelhagenetico.jogadorgenetico import JogadorGenetico
from jogodavelhagenetico.ferramentas import ferramentas as frt
from jogodavelhagenetico.modelos import ARVORE, POPULACAO_NUM_X, POPULACAO_NUM_O

app = Flask(__name__)


MAPA = None
with open(ARVORE, 'rb') as pickin:
    MAPA = pickle.load(pickin)

POPX = load(POPULACAO_NUM_X)
POPO = load(POPULACAO_NUM_O)
JOGADOR_X = JogadorGenetico(POPX[-1,:], 1, MAPA)
JOGADOR_O = JogadorGenetico(POPO[-1,:], -1, MAPA)

@app.route("/ia")
def ia():
    tabuleiro = zeros((3, 3))
    print(JOGADOR_X.jogar_em(tabuleiro))

@app.route("/")
def landing():
    """
    Render index.html. Initialization is performed asynchronously in initialize() function
    """
    tabuleiro = zeros((3, 3))
    print(JOGADOR_X.jogar_em(tabuleiro))
    # JOGADOR_X.reiniciar()
    #
    # tabuleiro = zeros((3, 3))
    # print(JOGADOR_X.jogar_em(tabuleiro))


    return render_template("index.html")

def startwebview():
    import webbrowser
    import time
    time.sleep(0.5)
    print("Abrindo Janela")
    webbrowser.open_new('http://0.0.0.0:8081/')

def main():
    print("Iniciando jogo")
    startwebview()
    app.run(host="0.0.0.0", port=8081, threaded=True, debug=False)
