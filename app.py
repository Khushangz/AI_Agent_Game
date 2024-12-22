from flask import Flask, render_template
from tic_tac_toe import TicTacToeGame  # Adjust based on your file structure

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Tic Tac Toe!"

if __name__ == "__main__":
    app.run(debug=True)
