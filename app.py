from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

# @app.route('/board')
# def register():
#     return render_template('board.html')

# @app.route('/mypage')
# def register():
#     return render_template('mypage.html')

# @app.route('/input')
# def register():
#     return render_template('input.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)