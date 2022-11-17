from flask import Flask

app = Flask(__name__)


@app.route("/") # ini mksdnya ada suatu fungsi lain yang harus dijalankan sebelum jalan helo world, hello world dijalankan didalam fungsi app
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run()
    # pake ini supaya pas running python hello.py langsung bisa,
    # ga perlu  flask --app .\hello.py run

#> set FLASK_APP=hello.py
#> flask run