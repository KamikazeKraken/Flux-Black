from flask import Blueprint, render_template
from helpers import LinkItem


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
    socials = [
        LinkItem("Reddit", "https://www.reddit.com/u/fluxkraken"),
        LinkItem("X", "https://x.com/flux_kraken"),
    ]
    return render_template("pages/socials.html", socials=socials)

@bp.route("/projects")
def projects():
    return render_template("pages/projects.html")

@bp.route("/blog")
def blog():
    return render_template("pages/blog.html")

@bp.route("/admin")
def admin():
    return render_template("pages/admin.html")
