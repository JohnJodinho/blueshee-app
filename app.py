# Flask App Template for Chat Agent
from flask import Flask, request, jsonify, send_file
from texts import SHAPE, SOUTH_WEST, MISCO, SYSTEM_INSTRUCTION
import pandas as pd
import json
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font, Alignment, PatternFill
from openpyxl.drawing.image import Image
from docx import Document
import os
import datetime
import re
import io

app = Flask(__name__)

# Route for handling chat interactions
@app.route('/chat', methods=['POST'])
def chat():

    user_input = request.json.get('message', '')

    response_text = "This is a sample response based on user input."

    return jsonify({"response": response_text})

# Route for file upload, if users upload files for processing
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    file = request.files['file']
    
    response_text = f"Received file: {file.filename}"
    return jsonify({"response": response_text})

# Route for file download if user needs to download a generated file
@app.route('/download', methods=['GET'])
def download_file():

    output = io.BytesIO()
    with open("generated_file.xlsx", "rb") as f:  # Replace with dynamically created files
        output.write(f.read())
    output.seek(0)
    return send_file(output, as_attachment=True, download_name="generated_file.xlsx")

# Health check route for testing the app status
@app.route('/health', methods=['GET'])
def health_check():
    return "Health check: OK", 200

if __name__ == '__main__':
    # Set debug to False for production deployment
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)), debug=False)
