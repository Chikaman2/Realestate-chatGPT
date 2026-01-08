from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models.property import Property
from app.extensions import db

property_bp = Blueprint("properties", __name__, url_prefix="/api/properties")

# PUBLIC
@property_bp.route("/", methods=["GET"])
def get_properties():
    properties = Property.query.all()
    return jsonify([
        {
            "id": p.id,
            "title": p.title,
            "price": float(p.price),
            "location": p.location,
            "image_url": p.image_url
        } for p in properties
    ])

# ADMIN
@property_bp.route("/", methods=["POST"])
@jwt_required()
def create_property():
    data = request.json
    prop = Property(**data)
    db.session.add(prop)
    db.session.commit()
    return jsonify({"msg": "Property created"}), 201
