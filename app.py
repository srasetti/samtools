import flask
from flask import jsonify
import sqlite3 as sql
from samtools.lib import is_palindrome

# Create the application.
app = flask.Flask(__name__)

@app.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')

@app.route('/api/ispalindrome/<string>')
def ispalyndrome(string):
    output = {
    'String' : string,
    'Verdict' : is_palindrome(string)
    }
    return jsonify(output)

if __name__ == '__main__':
    app.debug=True
    app.run()
