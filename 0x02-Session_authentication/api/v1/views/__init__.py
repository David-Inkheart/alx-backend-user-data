#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

# This import must be placed here to avoid circular import
from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.session_auth import *

User.load_from_file()
