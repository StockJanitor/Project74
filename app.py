from flask import Flask, request, redirect, url_for,render_template
from flask_wtf.file import FileField
from flask_wtf import Form

from wtforms import SubmitField
import sqlite3


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"



@app.route('/',methods =["GET","POST"])
def index():
    form = UploadForm()
    if request.method =="POST":
        if form.validate():
            file_name = form.file_.data.name
            print(f"{file_name}")
            return render_template("home.html",form=form)
    return render_template("home.html",form=form)

class UploadForm(Form):
    # file field object
    file_ = FileField()

    # submit/upload object
    submit = SubmitField("Upload")




if __name__ == "__main__":
    app.run(debug=True)
