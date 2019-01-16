from flask import Flask, render_template
from flask import abort
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
    if name == "":
        abort(404)
    else:
        return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)

# 通过flask script启动
# from flask_script import Manager
#
# manager = Manager(app)
#
# if __name__ == '__main__':
#     manager.run()
