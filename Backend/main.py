from flask import Flask

app = Flask(__name__)

@app.route ('/prueba')
def canche():
    print("aaaaaaaaaaa2backend")
    return "Probando el flask"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
