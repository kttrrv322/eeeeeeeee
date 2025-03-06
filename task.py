from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name}</h1>
                        <h3>Эта планета близко к Земле;</h3>
                        <div class="alert alert-success" role="alert">
                          <h3>На ней много ресурсов;</h3>
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          <h3>На ней есть вода и атмосфера;</h3>
                        </div>
                        <div class="alert alert-warning" role="alert">
                          <h3>На ней есть небольшое магнитное поле;</h3>
                        </div>
                        <div class="alert alert-danger" role="alert">
                          <h3>Наконец, она просто красива!</h3>
                        </div>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
