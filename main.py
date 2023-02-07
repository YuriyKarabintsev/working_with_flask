from flask import Flask, url_for, request

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


@app.route('/astronaut_selection')
def form_sample():
    print(request.method, "Method")
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                          </head>
                          <body>
                            <h1 align="center">Анкета претендента</h1>
                            <h2 align="center">на участие в миссии</h2>
                            <div bgcolor="$orange-200">
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите фамилию" name="email">
                                    <input type="password" class="form-control" id="password" placeholder="Введите имя" name="password">
                                    <br /><input type="password" class="form-control" id="password" placeholder="Введите адрес почты" name="password">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее общее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                       <p>Какие у Вас есть профессии?</p>
                                       <p><input type="checkbox" name="a" value="1">Инженер-исследователь</p>
                                       <p><input type="checkbox" name="a" value="2">Инженер-строитель</p>
                                       <p><input type="checkbox" name="a" value="3">Пилот</p>
                                       <p><input type="checkbox" name="a" value="4">Метеоролог</p>
                                       <p><input type="checkbox" name="a" value="5">Инженер по жизнеобеспечению</p>
                                       <p><input type="checkbox" name="a" value="6">Инженер по радиационной защите</p>
                                    <p><input type="checkbox" name="a" value="7">Врач</p>
                                    <p><input type="checkbox" name="a" value="8">Экзобиолог</p>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в экспедиции?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['education'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


@app.route("/choice/<planet_name>")
def variants_of_choice(planet_name):
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8" />
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Колонизация Марса</title>
                      </head>
                      <body>
                        <h1>Моё предложение: {planet_name}</h1>
                        <div>
                        Много нефти и газа
                        </div>
                        <div class="alert alert-success" role="alert">
                        Здесь есть целых 3 солнца
                        </div>
                        <div class="alert alert-dark" role="alert">
                        На планете можно разместить сервера суперкомпьютеров для хранения датасетов под нейронки
                        </div>
                        <div class="alert alert-warning" role="alert">
                        На этой планете безопасно, ведь там никто не умер.
                        </div>
                        <div class="alert alert-danger" role="alert">
                        На данной планете нету языка Kotlin, что делает её прекрасной
                        </div>
                      </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')