from flask import Flask, render_template, request, session
from flask_mysqldb import MySQL
import pandas as pd

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'book_recommend'
mysql = MySQL(app)

# Set a secret key for session management
app.secret_key = '8848'


@app.route('/')
def landpage():
     df = pd.read_csv('books.csv')

     name_list= df['category'].unique().tolist()

     return render_template('landpage.html', name_list=name_list)

    # Get the distinct list of names
    # name_list = df['category'].unique().tolist()

    # Render the HTML template with the name list
#  return render_template('landpage.html', name_list=name_list)
    # return render_template('landpage.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur = mysql.connection.cursor()

        # Verify the username and password in the database
        cur.execute("SELECT * FROM user_info WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()

        if user:
            # Store the user in the session
            session['username'] = user['username']
            return 'Logged in successfully!'
        else:
            error_message = 'Invalid username or password'
            return render_template('login.html', error_message=error_message)

    return render_template('login.html')



@app.route('/logout')
def logout():
    # Clear the session and log out the user
    session.clear()
    return 'Logged out successfully!'


@app.route('/forgotpassword')
def forgotpassword():
    return render_template('forgotpassword.html')


# @app.route('/signup')
# def signup():
#     return render_template('signup.html')
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        cur = mysql.connection.cursor()

        # Check if the username already exists in the database
        cur.execute("SELECT * FROM user_info WHERE username = %s", (username,))
        existing_user = cur.fetchone()

        if existing_user:
            error_message = 'Username already exists'
            return render_template('signup.html', error_message=error_message)

        # Insert the new user data into the database
        cur.execute("INSERT INTO user_info (username, password, email) VALUES (%s, %s, %s)", (username, password, email))
        mysql.connection.commit()

        # Store the user in the session
        session['username'] = username

        return render_template('login.html')

    return render_template('signup.html')






@app.route('/signup/genreofbook')
def genreofbook():
    return render_template('genreofbook.html')

# @app.route('/')
# def landpage():
#     # Read the CSV file into a DataFrame
#     df = pd.read_csv('books.csv')

#     # Get the distinct list of names
#     name_list = df['category'].unique().tolist()

#     # Render the HTML template with the name list
#     return render_template('landpage.html', name_list=name_list)



if __name__ == '__main__':
    app.run(debug=True)

