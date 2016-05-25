from flask import Flask, render_template
#app = Flask(__name__)
app = Flask(__name__, static_url_path = "", static_folder = "static")

@app.route('/')
def bud():
    #return 'Hello World!'
    return render_template('index.html') 
  
@app.route('/gallery')
def bud():    
    return render_template('gallery.html') 
  
@app.route('/charity')
def bud():    
    return render_template('charity.html') 

if __name__ == '__main__':
    app.run()