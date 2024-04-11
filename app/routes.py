from flask import Blueprint, request, jsonify
from app.run_advice.air_quality_utils import get_air_pollution_data

bp = Blueprint("home", __name__)


@bp.route("/")
def home():
    return jsonify({"status": "ok"})


@bp.route("/run-advice", methods=["GET"])
def get_run_advice():
    """Returns air pollution data, air quality index, and if it's a good idea to run"""
    city = request.args.get("city")
    supported_cities = {"manila": {"lat": "14.5995", "lon": "120.9842"}}

    if city not in supported_cities:
        return jsonify({"status": "failed", "message": f"City={city} is not supported"}), 400

    response, code = get_air_pollution_data(supported_cities.get(city))

    return jsonify(response), code
