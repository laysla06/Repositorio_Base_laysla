from flask import Flask
app = Flask(__name__)


@app.route('/')
def homem():
        
    ...
@app.route('/calculadora/soma/<int:n1>/<int:n2>')
def calculadora():
    n1=500
    n2=4
    resultado =n1 + n2 
    return f'resultado é:{resultado}'

@app.route('/bemvindo/<name>')
def bemvindo(name):
    ...



if __name__ == "__main__":
    app.run(debug=True)