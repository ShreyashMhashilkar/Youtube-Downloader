from flask import Flask,redirect,url_for,render_template,request
from downloadVideo import download_video
app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def get_num():
    if request.method == "POST":
        link_name = request.form["nm"]
        download_video(link_name)
        return "<h1>Video is downloaded</h1>"
    else:
        return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)