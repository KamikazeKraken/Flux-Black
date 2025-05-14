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

@bp.route("/socials")
def socials():
    return render_template("pages/socials.html")

@bp.route("/projects")
def projects():
    return render_template("pages/projects.html")

@bp.route("/blog")
def blog():
    return render_template("pages/blog.html")

@bp.route("/admin")
def admin():
    return render_template("pages/admin.html")
