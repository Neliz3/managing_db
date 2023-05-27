from flask import Flask


app = Flask(__name__)

from . import general
from . import admin
from . import admin
