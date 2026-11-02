
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

student = {
    "student_id": "STU1024",
    "subject": "Cloud Computing",
    "marks": 85
}

@app.route('/')
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>University Management System</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f1f5f9;
                color: #1e293b;
            }
            header {
                background: #173b70;
                color: white;
                padding: 25px 8%;
            }
            header h1 { margin: 0; }
            main {
                max-width: 850px;
                margin: 55px auto;
                padding: 20px;
            }
            .card {
                background: white;
                padding: 30px;
                border-radius: 16px;
                box-shadow: 0 5px 20px #00000012;
            }
            .details {
                display: flex;
                gap: 15px;
                flex-wrap: wrap;
                margin-top: 25px;
            }
            .item {
                flex: 1;
                min-width: 150px;
                background: #eff6ff;
                padding: 20px;
                border-radius: 12px;
            }
            .item h2 { color: #1d4ed8; }
            a {
                display: inline-block;
                margin-top: 25px;
                padding: 12px 22px;
                background: #2563eb;
                color: white;
                text-decoration: none;
                border-radius: 8px;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>University Management System</h1>
            <p>Student Academic Dashboard</p>
        </header>
        <main>
            <div class="card">
                <h2>Welcome, Student!</h2>
                <p>Your academic results are available below.</p>
                <div class="details">
                    <div class="item">
                        <p>Student ID</p>
                        <h2>STU1024</h2>
                    </div>
                    <div class="item">
                        <p>Subject</p>
                        <h2>Cloud Computing</h2>
                    </div>
                    <div class="item">
                        <p>Marks</p>
                        <h2>85 / 100</h2>
                    </div>
                </div>
                <a href="/results">View API Results</a>
            </div>
        </main>
    </body>
    </html>
    """)

@app.route('/results')
def results():
    return jsonify(student)

app.run(host='0.0.0.0', port=5000)
