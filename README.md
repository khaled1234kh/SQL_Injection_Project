# SQL Injection Demo

## Description
This project demonstrates SQL injection vulnerabilities and how to detect and protect against them.

## Features
- Vulnerable Flask web app (`vulnerable_app.py`)
- Detection script (`detect_sql_injection.py`)
- Secure Flask web app (`secure_app.py`)

## Setup

1. Clone the repo:
   ```
   git clone https://github.com/yourusername/sql-injection-demo.git
   cd sql-injection-demo
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the vulnerable app:
   ```
   python vulnerable_app.py
   ```

4. In another terminal, run the detection script:
   ```
   python detect_sql_injection.py
   ```

5. Try SQL injection manually in the login form (e.g., username: `' OR '1'='1`, any password).

6. Run the secure app to see protection:
   ```
   python secure_app.py
   ```

## Protection
The secure app uses parameterized queries to prevent SQL injection.

## Video Demo
[YouTube Link Here]

## Author
Your Name
