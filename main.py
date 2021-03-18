from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def main():
    return "<h2>Миссия Колонизация Марса</h2>"


@app.route('/index')
def index():
    return "<h2>И на Марсе будут яблони цвести!</h2>"


@app.route('/promotion')
def promotion():
    return """<pre><h3>Человечество вырастает из детства.
Человечеству мала одна планета.
Мы сделаем обитаемыми безжизненные пока планеты.
И начнем с Марса!
Присоединяйся!<h3></pre>"""


@app.route('/image_mars')
def image_mars():
    return """<!doctype html>
                    <html>
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="http://pngimg.com/uploads/mars_planet/mars_planet_PNG15.png" 
                        width="300" height="300"><br>
                        Вот она какая, красная планета.
                      </body>
                    </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}" 
                    width="300" height="300"><br>

                    <div class="alert alert-dark" role="alert">
                    <h5>Человечество вырастает из детства.<h5>
                    </div> 

                    <div class="alert alert-success" role="alert">
                    <h5>Человечеству мала одна планета.<h5>
                    </div>
                    
                    <div class="alert alert-dark" role="alert">
                    <h5>Мы сделаем обитаемыми безжизненные пока планеты.<h5>
                    </div>
                    
                    <div class="alert alert-warning" role="alert">
                    <h5>И начнем с Марса!<h5>
                    </div>
                    
                    <div class="alert alert-danger" role="alert">
                    <h5>Присоединяйся!</h5>
                    </div>
                  </body>
                </html>"""


@app.route('/astronaut_selection')
def astronaut_selection():
    with open('space.html') as file:
        html = file.read()
    return html


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
