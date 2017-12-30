from app.method import Route
from app.Controller import Control
from flask import Flask
import os


app = Flask(os.getcwd())

app.secret_key = 'any random string'

app.config.from_object(__name__)

route = Route(app)

pages = Control()


