# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("C:\Users\sahil\OneDrive\Documents\C-116 Project # 2 - BYJU")
def home():

    name = "Sahil N" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/templates/father.html")

# define the route to mother webpage
@app.route("/templates/mother.html")

# define the route to friends webpage
@app.route("/templates/friend.html")

# add other routes, if you want
@app.route("/index.html")



# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
