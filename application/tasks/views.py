from application import app, db
from flask import render_template, request
from application.tasks.models import Task

@app.route("/tasks/new/")
def tasks_form():
    return render_template("tasks/new.html")

@app.route("/tasks/", methods=["POST"])
def tasks_create():
    t = Task(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return "hello world!"
