
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def upload():

    file = request.files['file']
    print(file.stream.read())
    print(file.filename)
    print(request.form['job_id'])
    print(request.form['client_id'])
    return {}, 200


if __name__ == '__main__':
    app.run()