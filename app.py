from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Возвращаем шаблон index.html
    return render_template('index.html')

if __name__ == '__main__':
    # Запускаем приложение
    app.run(debug=True)
