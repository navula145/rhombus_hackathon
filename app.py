from flask import Flask

app = Flask(__name__)

@app.route('/')

ENTRYPOINT ['tail','-f','/dev/null']

def hello_world():
    return 'Hello from Virtual Machine'

if __name__=='__main__':
     app.run(host='0.0.0.0', port=5000)