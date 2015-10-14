#!flask/bin/python
from app import app
import warnings

warnings.simplefilter('error')

app.run(debug=True)
