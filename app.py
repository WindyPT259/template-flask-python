from flask import Flask, render_template
from flask_cors import CORS
from src.routes.routes import routes
from src.models.db import db

# CREATE APP
app = Flask(__name__, static_url_path="", static_folder="public")
app.config.from_object("config")
db.init_app(app)
CORS(app)

app.register_blueprint(routes)


@app.before_first_request
def initialize_database():
    db.create_all()


@app.teardown_request
def shutdown_session(exception=None):
    db.session.remove()


# errors
@app.errorhandler(404)
def not_found(error):
    return render_template("404.html")


def main():
    app.run(host="0.0.0.0", debug=True, threaded=True)


if __name__ == "__main__":
    main()
