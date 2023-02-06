from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def start():
    return "Миссия Колонизация Марса"

@app.route("/index")
def index():
    return "И на Марсе будут яблони цвести!"

@app.route("/promotion")
def promotion():
    return "</br>".join([
        "Человечество вырастает из детства.",
        "Мы сделаем обитаемыми безжизненные пока планеты.",
        "И начнем с Марса!",
        "Присоединяйся!"
    ])

@app.route("/image_mars")
def image_mars():
    return '''<h1>Жди нас, Марс!</h1><img src="/static/img/mars.jpg" alt="здесь должен быть Марс"><p>Вот она какая, красная планета.</p>'''




@app.route("/promotion_image")
def promotion_image():
    ending = "</br>".join([
        "Человечество вырастает из детства.",
        "Мы сделаем обитаемыми безжизненные пока планеты.",
        "И начнем с Марса!",
        "Присоединяйся!"
    ])
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/styles.css')}" />
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Колонизация Марса</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/mars.jpg" alt="здесь должен быть Марс">
                    <div class="alert alert-dark" role="alert">
                    Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                    Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                    Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                    И начнем с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                    Присоединяйся!
                    </div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')