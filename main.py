from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def main():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    promo = '''Человечество вырастает из детства.
             Человечеству мала одна планета.
             Мы сделаем обитаемыми безжизненные пока планеты.
             И начнем с Марса!
             Присоединяйся!'''
    return promo.replace('\n', '<br>')


@app.route('/image_mars')
def image():
    return '''<title>Привет, Марс!</title>
              <h1>Жди нас, Марс!</h1>
              <img src="https://upload.wikimedia.org/wikipedia/commons/0/02/OSIRIS_Mars_true_color.jpg" 
              alt="здесь должна была быть картинка марса">
              <p>Вот она какая красная планета</p>'''


@app.route('/promotion_image')
def promotion_image():
    return '''<!doctype html>
              <html lang="en">
              <head>
              <meta charset="utf-8">
              <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
              <link rel="stylesheet" 
              href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
               integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
               crossorigin="anonymous">
              <link rel="stylesheet" href="static\\css\\style.css">
              <title>Колонизация</title>
              </head>
              <body>
              <h1>Жди нас, Марс!</h1>
              <img src="static\\img\\Mars.png" alt="здесь должна была быть картинка марса" width="400px" height="400px">
               <div class="alert alert-primary" role="alert">
               Человечество вырастает из детства.
               </div>
               <div class="alert alert-secondary" role="alert">
                Человечеству мала одна планета.
               </div>
               <div class="alert alert-success" role="alert">
                Мы сделаем обитаемыми безжизненные пока планеты.!
               </div>
               <div class="alert alert-danger" role="alert">
                И начнем с Марса!
               </div>
               <div class="alert alert-warning" role="alert">
                Присоединяйся!
               </div>
               </body>
               </html>'''


@app.route('/astronauts_selection', methods=['POST', 'GET'])
def astronauts_selection():
    if request.method == 'GET':
        return '''<!doctype html>
                    <html lang="en">
                    <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="static/css/style2.css" />
                    <title>Отбор астронавтов</title>
                    </head>
                    <body>
                    <h1>Анкета претендента</h1>
                    <h3>на участие в миссии</h3>
                    <div>
                    <form class="login_form" method="post">
                    <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                    <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" 
                    placeholder="Введите адрес почты" name="email">
                    <div class="form-group">
                    </div>
                    <div class="form-group">
                    <label for="classSelect">Какое у Вас образование?</label>
                    <select class="form-control" id="classSelect" name="education">
                    <option>Начальное</option>
                    <option>Среднее</option>
                    <option>Высшее</option>
                    </select>
                    </div>
                    <div class="form-group">
                    <label for="form-check">Какие у Вас есть профессии?</label>
                    <div class="form-check">
                    <input class="form-check-input" type="radio" name="profession" 
                    value="инженер-исследователь" checked>
                    <label class="form-check-label" for="инженер-исследователь">инженер-исследователь</label>
                    </div>
                    <div class="form-check">
                    <input class="form-check-input" type="radio" name="profession" value="пилот">
                    <label class="form-check-label" for="пилот">пилот</label>
                    </div>
                    <div class="form-check">
                    <input class="form-check-input" type="radio" name="profession" value="строитель" checked>
                    <label class="form-check-label" for="строитель">строитель</label>
                    </div>
                    <div class="form-check">
                    <input class="form-check-input" type="radio" name="profession" value="экзобиолог">
                    <label class="form-check-label" for="экзобиолог">экзобиолог</label>
                    </div>
                    <div class="form-check">
                    <input class="form-check-input" type="radio" name="profession" value="инженер по терраформированию" 
                    checked>
                    <label class="form-check-label" for="инженер по терраформированию">инженер по терраформированию
                    </label>
                    </div>
                    <div class="form-check">
                    <input class="form-check-input" type="radio" name="profession" value="климатолог">
                    <label class="form-check-label" for="климатолог">климатолог</label>
                    </div>
                    <div class="form-check">
                    <input class="form-check-input" type="radio" name="profession" value="астрогеолог">
                    <label class="form-check-label" for="астрогеолог">астрогеолог</label>
                    </div>
                    <div class="form-check">
                    <input class="form-check-input" type="radio" name="profession" value="гляциолог" checked>
                    <label class="form-check-label" for="гляциолог">гляциолог</label>
                    </div>
                    </div>
                    <div class="form-group">
                    <label for="form-check">Укажите пол</label>
                    <div class="form-check">
                    <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                    <label class="form-check-label" for="male">Мужской</label>
                    </div>
                    <div class="form-check">
                    <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                    <label class="form-check-label" for="female">Женский</label>
                    </div>
                    </div>
                    <div class="form-group">
                    <label for="motivation">Почему Вы хотите принять участие в миисси?</label>
                    <textarea class="form-control" id="motivation" rows="3" name="motivation"></textarea>
                    </div>
                    <div class="form-group form-check">
                    <input type="checkbox" class="form-check-input" id="will_stay" name="will_stay">
                    <label class="form-check-label" for="will_stay">Готовы остаться на марсе?</label>
                    </div>
                    <button type="submit" class="btn btn-primary">Записаться</button>
                    </form>
                    </div>
                    </body>
                    </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form['profession'])
        print(request.form['sex'])
        print(request.form['motivation'])
        print(request.form['will_stay'])
        return "OK"


@app.route('/choice/<planet_name>')
def planet_choice(planet_name):
    planet_text = {'Марс': ['Эта планета близка к земле;', 'На ней много необходимых ресурсов;',
                            'На ней есть вода и атмосфера;', 'На ней есть небольшое магнитное поле;',
                            'Наконец она просто красива!'],
                   'Меркурий': ['Эта планета ближайшая к Солнцу;',
                                'Планета обращается вокруг Солнца за 88 земных суток;',
                                'Меркурий самая маленькая планета;', 'У планеты очень разряженная атмосфера;',
                                'Ускорение свободного падения на меркурии в два раза меньше чем на Земле!'],
                   'Венера': ['Принадлежит к семейству планет земной группы;',
                              'Атмосфера Венеры на 96% сотоит из углекислого газа;',
                              'Это самая горячая планета;', 'Венера не имеет естественных спутников;',
                              'Также Венера была главной целью для ранних межпланетных исследований!']}

    return f''' <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
                <title>Варианты выбора</title>
                <h1>Мое предложение: {planet_name}</h1>
                <div class="alert alert-primary" role="alert">
                 {planet_text[planet_name][0]}
                </div>
                <div class="alert alert-secondary" role="alert">
                 {planet_text[planet_name][1]}
                </div>
                <div class="alert alert-success" role="alert">
                 {planet_text[planet_name][2]}
                </div>
                <div class="alert alert-danger" role="alert">
                 {planet_text[planet_name][3]}
                </div>
                <div class="alert alert-warning" role="alert">
                 {planet_text[planet_name][4]}
                </div>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
               <title>Результаты</title>
               <h1>Результаты отбора</h1>
               <div class="alert alert-primary" role="alert">
                Претендента на участие в миссии {nickname}:  
               </div>
               <div class="alert alert-secondary" role="alert">
                Поздравляем! Ваш рейтинг после {level} этапа отбора 
               </div>
               <div class="alert alert-success" role="alert">
                составляет {rating}
               </div>
               <div class="alert alert-warning" role="alert">
                 Желаем удачи!
               </div>'''


@app.route('/carousel')
def carousel():
    return '''<link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
              <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" 
              integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" 
              crossorigin="anonymous"></script>
              <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" 
              integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" 
              crossorigin="anonymous"></script>
              <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" 
              integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" 
              crossorigin="anonymous"></script>
              <h1 style="text-align: center;">Пейзажи Марса</h1>
              <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
              <div class="carousel-inner">
              <div class="carousel-item active">
              <img class="d-block w-100" src="static/img/Пейзаж.png" alt="First slide">
              </div>
              <div class="carousel-item">
              <img class="d-block w-100" src="static/img/Пейзаж_2.png" alt="Second slide">
              </div>
              <div class="carousel-item">
              <img class="d-block w-100" src="static/img/Пейзаж_3.png" alt="Third slide">
              </div>
              </div>
              <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
              <span class="carousel-control-prev-icon" aria-hidden="true"></span>
              <span class="sr-only">Previous</span>
              </a>
              <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
              <span class="carousel-control-next-icon" aria-hidden="true"></span>
              <span class="sr-only">Next</span>
              </a>
              </div>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
