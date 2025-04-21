from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>YouDub is working!</h1><p>Welcome to the deployed version on Render.</p>"

