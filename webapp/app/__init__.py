from flask import Flask

app = Flask(__name__)

app.BREW_TIMER = None

from app import views, api
