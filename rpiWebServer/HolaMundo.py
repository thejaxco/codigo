from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hola Javi'
if __name__ == '__main__':
    app.run(debug=True, port=80, host='10.199.160.229')
