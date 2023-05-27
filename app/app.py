from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Greetings</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                text-align: center;
                padding-top: 100px;
            }

            h1 {
                color: #333333;
            }

            p {
                color: #777777;
            }
        </style>
    </head>
    <body>
        <h1>Hello ami!</h1>
        <p>Hope you're doing great!</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()

