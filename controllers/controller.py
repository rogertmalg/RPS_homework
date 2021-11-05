from flask import render_template #might need request, redirect
from app import app

@app.route('/')
def home():
    return render_template('index.html')