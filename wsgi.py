from flask import Flask, jsonify
from src.dice_roll_v1.dice import Dice

app = Flask(__name__)

@app.route('/')
def home():
    dice = Dice()
    return jsonify({'roll': dice.roll()})
