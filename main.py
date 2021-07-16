from flask import Flask, request
from utils import read_requirements_txt, making_users

# 1

app = Flask(__name__)

@app.route('/requirements/')
def requirements():
    result = read_requirements_txt()
    return result


# 2

@app.route('/generate-users/')
def generate_users():
    users_numb = int(request.args.get('numb-of-users'))
    result = making_users(users_numb)
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0')