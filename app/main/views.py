from datetime import datetime
from . import main
from .. import db
from ..models import User


@main.route('/', methods=['GET', 'POST'])
def index():
    pass
