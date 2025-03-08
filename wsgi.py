from flask import Flask, jsonify
from src.dice_roll_v1.dice import Dice

app = Flask(__name__)

@app.route('/')
def home():
    dice = Dice()
    roll = dice.roll()
    return jsonify({'roll': roll})
