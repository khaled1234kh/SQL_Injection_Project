# SQL Injection Detection Script

This project is a basic SQL Injection (SQLi) testing script implemented in **Python** using the **requests** library. It simulates common SQL injection payloads against a login form and detects possible vulnerabilities based on the server's response.

## 📌 Features

- 🧪 Tests multiple common SQL injection payloads
- 📥 Sends POST requests with injection attempts
- 🔍 Analyzes server responses for success indicators
- 🧱 Helps identify insecure login endpoints

## ⚙️ How It Works

The system:
1. Defines a list of common SQL injection payloads
2. Sends each payload as the `username` field in a login request
3. Checks if the server response includes “Login successful”
4. Alerts the user if a payload bypasses authentication

## 🛠️ Requirements

- Python 3.x
- requests

Install dependencies using:

```bash
pip install -r requirements.txt
