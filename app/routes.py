from flask import Blueprint, request, render_template
from app.services.database import get_client_info

bp = Blueprint("client", __name__)

@bp.route("/client")
def client_lookup():
    phone = request.args.get("number")
    data = get_client_info(phone)
    return render_template("client.html", client=data)
