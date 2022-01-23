# going to create a MODULE for flask_app,
# similiar to our constructor function in our classes
from flask import Flask

app = Flask(__name__)

app.secret_key = "guess@me"