from flask import Flask, request
from flask_cors import CORS  # Install with: pip install Flask-CORS
from app import create_app
from app.models import db

app = create_app()
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5500"}})  # Allow requests from your frontend

@app.before_request
def handle_options_requests():
    if request.method == 'OPTIONS':
        response = app.make_default_options_response()
        headers = response.headers

        headers['Access-Control-Allow-Origin'] = 'http://localhost:5500'
        headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        headers['Access-Control-Allow-Headers'] = 'Authorization, Content-Type'

        return response

with app.app_context(): 
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)