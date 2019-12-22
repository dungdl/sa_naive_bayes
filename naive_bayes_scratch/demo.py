import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import predict

app = Flask(__name__)

# SET HOST AND PORT
HOST="127.0.0.1"
PORT="5000"

# UPLOAD PROCESS
@app.route('/', methods = ['GET', 'POST'])
def index():
   if request.method == 'POST':
      review  = request.form.get("input")
      predict_result = predict.run(review)
      return render_template('home.html', input=review, print_result=predict_result)
   return render_template('home.html')

if __name__ == "__main__":
   app.run(host=HOST, port=PORT, debug=True)