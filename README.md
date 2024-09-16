# WarwickActive_sport_system
# It is recommended to download the file ending with .rar, which is the full version of Warwick Active
This Flask-based web application manages user authentication and event bookings for a sports system. It uses SQLite as its database to handle registrations, logins, and event reservations.

# Features
User Registration: Users can register by providing a username, email, student ID, and password.
User Login: Registered users can log in using their credentials.
Event Booking: Users can book events by providing event details, and their bookings are stored in the database.
Cancel Booking: Users can cancel previously made bookings.
Flash Messages: The application provides feedback through flash messages for successful and failed actions.

# Installation Instructions
Prerequisites
Python 3.x
Flask
SQLite
Werkzeug (for password hashing)

# Setup
1. Clone the repository (or download the code): 
git clone https://github.com/your_repo/sport_system_app.git
cd sport_system_app

2. Install dependencies: Install Flask and other necessary packages using pip: pip install Flask Werkzeug

3. Set Up the SQLite Database: By default, the application will use an SQLite database file named sport_system_database.db. If you'd like to change the database location or name, you can set the environment variable FLASK_DATABASE before running the app.

4. Run the Application: To start the web server, execute the following command in the project directory: python app.py
The application will run in debug mode by default.

# Directory Structure
app.py: Main application file containing the Flask routes and logic.
templates/: Folder containing HTML templates for rendering web pages.
homepage.html
login.html
register.html
reservation.html
static/: (Optional) Folder for storing static files like CSS and JavaScript.

# Environment Variables
FLASK_DATABASE: Set this to change the path to the SQLite database file. If not set, it defaults to sport_system_database.db.

# Routes
1. Home Page (/homepage):
Displays the homepage for logged-in users.

3. Login Page (/login):
Allows users to log in. On success, the user is redirected to the homepage.

3. Registration Page (/register):
Enables new users to register. The user must provide a unique username, email, student ID, and password.

4. Event Booking (/onlinebooking):
Users can book sports events by filling out a form with event details.

5. Cancel Booking (/cancelbooking):
Allows users to cancel their event bookings.

# Database
The SQLite database contains two main tables:
1. registration:
Stores user registration data (username, email, student_id, password_hash).

2. event_bookings:
Stores event booking information (event_name, booking_time, customer_name, email, notes).

# Security
1. Password Hashing: Passwords are hashed using Werkzeug's generate_password_hash function before storing them in the database.
2. Session Management: Flask's session management is used to store the logged-in user's session data securely.

# Known Issues
The application is currently in development, and features like email validation and session timeout need to be implemented.
Proper error handling and input validation should be enhanced for production use.

# Future Improvements
Implement user profile management.
Add more detailed event management features, such as updating bookings or user notifications.
Enhance security with measures such as CSRF protection and rate limiting.

# License
This project is licensed under the MIT License.

# Contact
For any questions or issues, please reach out at u5556335@live.warwick.ac.uk.
