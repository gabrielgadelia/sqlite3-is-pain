from flask import Flask
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("mziuri.db")
c = conn.cursor()

c.execute
("""
    (first_name text,
    last_name text,
    age integer,
    university text,
    is_active text,      
    major text,
    when_started_learning integer,
    when_end_learning integer)
""")
conn.commit

c.execute(" INSERT INTO users VALUES ('michael', 'smith', 30, 'Stanford', 'he is not active', 'math', 2017, 2024)")
c.execute(" INSERT INTO users VALUES ('michael', 'maria', 35, 'harvard', 'she is active', 'history', 2017, 2024)")
c.execute(" INSERT INTO users VALUES ('michael', 'lincoln', 27, 'Stanford', 'he is not active', 'english', 2017, 2024)")
c.execute(" INSERT INTO users VALUES ('michael', 'angelina', 45, 'TSU', 'she is active', 'comunication', 2017, 2024)")
c.execute(" INSERT INTO users VALUES ('michael', 'nick', 50, 'Stanford', 'he is not active', 'quantom physics', 2017, 2024)")

# con.close
# cursor.close

@app.route("/")
def home():
    return "Hello World!"

if __name__ == "__main__":
    app.run()