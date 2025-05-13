from flask import Blueprint, render_template


bp = Blueprint(
   "root",
   __name__
)


@bp.route("/")
def landing():
    return render_template("pages/landing.html")

@bp.route("/home")
def index():
    return render_template("pages/index.html")