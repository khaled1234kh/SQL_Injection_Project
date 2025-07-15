from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('demo.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    c.execute('INSERT OR IGNORE INTO users (id, username, password) VALUES (1, "admin", "adminpass")')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # VULNERABLE QUERY
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        conn = sqlite3.connect('demo.db')
        c = conn.cursor()
        c.execute(query)
        result = c.fetchone()
        conn.close()
        if result:
            message = 'Login successful!'
        else:
            message = 'Login failed!'
    return render_template_string('''
        <h2>Login</h2>
        <form method="post">
            Username: <input name="username"><br>
            Password: <input name="password" type="password"><br>
            <input type="submit" value="Login">
        </form>
        <p>{{message}}</p>
    ''', message=message)

if __name__ == '__main__':
    init_db()
    app.run(debug=True) 