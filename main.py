from flask import Flask, request, render_template, redirect

# Создаем экземпляр приложения Flask
app = Flask(__name__)
# Создаем пустой словарь пользователей
users = {}

# Загружаем пользователей из файла и добавляем их в словарь
with open('users.txt', 'r') as f:
    for line in f:
        username, password = line.strip().split(':')
        users[username] = password
# Определяем маршрут для главной страницы
@app.route('/')
def index():
    return render_template('login.html')

# Определяем маршрут для страницы авторизации
@app.route('/login', methods=['POST'])
# Получаем имя пользователя и пароль из формы
def login():
    username = request.form['username']
    password = request.form['password']
    # Проверяем, есть ли такой пользователь в словаре и совпадает ли его пароль
    if username in users and users[username] == password:
        return redirect('/home')
    else:
        return render_template('login.html', error='Invalid username or password')
# Определяем маршрут для домашней страницы
@app.route('/home')
def home():
    return 'Welcome to the home page!'

# Функция для сохранения пользователей в файл
def save_users():
    with open('users.txt', 'w') as f:
        for username, password in users.items():
            f.write(f'{username}:{password}\n')

if __name__ == '__main__':
    app.run(debug=True)