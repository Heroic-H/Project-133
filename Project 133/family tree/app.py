# importing modules from flask library

from flask import Flask , render_template


# creating instance of class Flask, by providing __name__ keyword as argument

app = Flask(__name__)


# write the routes using decorator functions

# default route or 'URL'

@app.route("/")

def home():
    name = "Hussein" # write your name
    age = "13" # write your age
    return render_template('index.html' , name = name , age = age)
    return "With thanks to Hussein Day for making this web site possible with his awsome coding skills."

# define the route to father webpage
@app.route("/father")
def fatherPage():
    return render_template('father.html', index_variable = "Flask")
# define the route to mother webpage
@app.route("/mother")
def motherPage():
    return render_template('mother.html', index_variable = "mother")
# define the route to friends webpage
@app.route("/friend")
def friendPage():
    return render_template('friend.html', index_variable = "friend")
# add other routes, if you want

#if __name__  ==  '__main__':
def jls_extract_def():
    return app


jls_extract_def().run(debug=True)