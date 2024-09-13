import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, g, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'my_super_secret_key_123!@#'

# The database configuration
DATABASE_PATH = os.environ.get("FLASK_DATABASE", "sport_system_database")
DATABASE = os.path.join(os.getcwd(), DATABASE_PATH)

# Functions to help connect to the database
# And clean up when this application ends.
def get_db_connection():
    db = getattr(g, "_database", None)
    if db is None:
        print(f"Connecting to database: {DATABASE}")
        db = g._database = sqlite3.connect(DATABASE)
        print("Database connection established.")
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

# Home Page Route
@app.route("/homepage")
def home():
    return render_template("homepage.html")

# Login Page Route
@app.route("/login", methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        try:
            conn = get_db_connection()
            username = request.form["username"]
            password = request.form["password"]
            cursor = conn.cursor()
            cursor.execute("SELECT username, password_hash FROM registration WHERE username=?", (username,))
            user = cursor.fetchone()
            
            if user and len(user) > 1 and check_password_hash(user[1], password):
                session['username'] = user[0]
                flash('Login successful', 'success')
                return redirect(url_for("home"))
            else:
                flash('Invalid username or password', 'error')
            conn.close()
        except Exception as e:
            print(f"Error during login: {e}")
            flash('An error occurred during login. Please try again.', 'error')
    return render_template("login.html")

# Register Page Route
@app.route("/register", methods=["GET", "POST"])
def register_page():
    if request.method == "POST":
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            username = request.form["username"]
            email = request.form["email"]
            student_id = request.form["student_id"]
            password = request.form["password"]

            cursor.execute("SELECT username FROM registration WHERE username=?", (username,))
            existing_user = cursor.fetchone()

            if not existing_user:
                hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
                cursor.execute(
                    "INSERT INTO registration (username, email, student_id, password_hash) VALUES (?, ?, ?, ?)",
                    (username, email, student_id, hashed_password)
                )
                conn.commit()
                flash('Registration successful. You can now log in.', 'success')
                return redirect(url_for("login_page"))
            else:
                flash('Username already exists. Please choose a different one.', 'error')
            conn.close()
        except Exception as e:
            print(f"Error during registration: {e}")
            flash('An error occurred during registration. Please try again.', 'error')
    return render_template("register.html")

@app.route("/onlinebooking", methods=["GET", "POST"])
def reservation_page():
    conn = get_db_connection()
    cursor = conn.cursor()

    recent_reservation = None

    if request.method == "POST":
        try:
            event_name = request.form["event_name"]
            booking_date = request.form["booking_date"]
            time_slot = request.form["time_slot"]
            booking_time_str = f"{booking_date} {time_slot}"
            customer_name = request.form["customer_name"]
            email = request.form["email"]
            notes = request.form["notes"]

            cursor.execute('''
                INSERT INTO event_bookings (event_name, booking_time, customer_name, email, notes)
                VALUES (?, ?, ?, ?, ?)
            ''', (event_name, booking_time_str, customer_name, email, notes))

            conn.commit()

            recent_reservation = {
                "event_name": event_name,
                "booking_time": booking_time_str,
                "customer_name": customer_name,
                "email": email,
                "notes": notes
            }

            flash('Event booking successful!', 'success')
        except Exception as e:
            print(f'Error during booking: {e}')
            flash('An error occurred during booking. Please try again.', 'error')

    conn.close()
    return render_template("reservation.html", recent_reservation=recent_reservation)


if __name__ == '__main__':
    app.run(debug=True)