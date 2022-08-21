import glob
import io
import os
import uuid

import numpy as np
from flask import Flask, jsonify, make_response, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    title = "Inicio"
    return render_template('index.html', title=title)



if __name__ == '__main__':
    app.run(debug=True)