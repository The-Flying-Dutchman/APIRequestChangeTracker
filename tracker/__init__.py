from flask import Flask

app = Flask(__name__, instance_relative_config=True)

# Load the default configuration
app.config.from_object('config')
# load the specified file from the instance/ directory.
app.config.from_pyfile('config.py')

