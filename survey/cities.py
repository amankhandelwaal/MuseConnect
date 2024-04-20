from flask import Flask, render_template, request
import mysql.connector as ms

app = Flask(__name__)

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',  # Replace 'username' with your MySQL username
    'password': 'vishwa',  # Replace 'password' with your MySQL password
    'database': 'museconnect'
}

# Function to establish MySQL connection
def get_db_connection():
    conn = ms.connect(**db_config)
    return conn

@app.route('/')
def home():
    return render_template('cities.html')

@app.route('/selectOption', methods=['POST','GETS'])
def button_clicked():
    if request.method == 'POST':
        selected_button = request.form[id]
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("insert into city_data values('selected_button')")
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/test')
def tests():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)