from flask import Flask, render_template
from flask_migrate import Migrate
from models.models import db

# from routes.our_services import our_services
from routes.management_console import management_console

app = Flask(__name__)
app.config.from_object("config")
db.init_app(app)
migrate = Migrate(app, db)

# app.register_blueprint(our_services, url_prefix='/our-services')
app.register_blueprint(management_console, url_prefix="/management")


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port='5000')
