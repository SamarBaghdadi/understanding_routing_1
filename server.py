from distutils.log import debug
from flask import Flask
my_pages_list=['','dojo','say','repeat']
app=Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:var_name>')
def say_name(var_name):
    return f'Hi {var_name}'

@app.route('/repeat/<int:number>/<string:var_name>')
def repeat(number,var_name):
    app_number=number
    app_var_name=var_name
    return number*var_name
@app.route('/<page_path>')
def sorry_msg(page_path):
    my_bool=False
    for element in my_pages_list:
        if page_path == element:
            my_bool=True
    if my_bool==False:
        return "Sorry baby!"
    

if __name__=="__main__":
    app.run(debug=True)