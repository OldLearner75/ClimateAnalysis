

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)
session = Session(engine)
app = Flask(__name__)


#I don't understand anything that goes in here. Rewatched the videos, still don't get it.  

if __name__ == '__main__':
    app.run()
