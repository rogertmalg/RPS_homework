from flask import render_template, request, redirect 
from app import app
from models.game import *
from models.player import *
import random

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<player_1_hand>/<player_2_hand>')
def result(player_1_hand, player_2_hand):
    player_1 = Player("Player 1", player_1_hand)
    player_2 = Player("Player 2", player_2_hand)
    game_object = Game()
    result = game_object.play_game(player_1, player_2)
    
    return render_template('result.html', player_1 = player_1, player_2 = player_2, winner = result)

@app.route('/play')
def play():
    return render_template('play.html')
    

    # player_name = request.form['name']
    # player_hand = request.form['hand']
    # player_1 = Player(player_name, player_hand)
