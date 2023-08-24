from flask import Flask

app = Flask(__name__)

from . import general
from . import admin
from . import utils
from . import shop_order
from . import auth
