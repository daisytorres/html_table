from flask import Flask, render_template 
app = Flask(__name__)    

# @app.route('/') 
# def hello_world():
#     return 'Hello World!, seriously Hello'  

@app.route('/html_table')
def my_list():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Cho'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'}
        ]

    return render_template("index.html", users=users)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.