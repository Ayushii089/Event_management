from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__, template_folder='templates')

# --- Database Connection Function ---
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password123",   # ⚠️ change this to your MySQL password
        database="event_management"
    )

# --- Home Page: Show All Events ---
@app.route('/')
def show_events():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM events")
    events = cursor.fetchall()
    conn.close()
    return render_template('live_events.html', events=events)

# --- Add Event Page (Form) ---
@app.route('/add', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        name = request.form['event_name']
        date = request.form['event_date']
        description = request.form['description']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO events (event_name, event_date, description) VALUES (%s, %s, %s)",
                       (name, date, description))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('add_event.html')

if __name__ == '__main__':
    app.run(debug=True)
