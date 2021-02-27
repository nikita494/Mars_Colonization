from flask import Flask

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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
