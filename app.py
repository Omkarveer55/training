from flask import Flask,request

app = Flask(__name__)

@app.route('/main',methods = ['GET'])
def main():
    return "hello"

if __name__ == '__main__':
    app.run(debug=True)