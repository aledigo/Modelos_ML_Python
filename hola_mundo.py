
from flask import Flask
app = Flask('__name__')

@app.route('/')
def index():
   return 'Hola Mundo! Soy Alejandra \N{winking face}'


if __name__ == "__main__":
    app.run(debug=False, port=5003)

