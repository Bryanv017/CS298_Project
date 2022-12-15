import encrypter
from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route("/" , methods = ["POST" , "GET"])
def index():
    if request.method == 'POST':
        input_txt = request.form["input"]
        cipher = encrypter.encrypt(input_txt)
        return f"<h2>Encrypted Text: </h2><p>{cipher}</p>"
    else:
        return render_template('index.html')


if __name__ == "__main__":
    
    #run over http
    #app.run()
    #run over https
    app.run(ssl_context=('cert.pem', 'key.pem'))
