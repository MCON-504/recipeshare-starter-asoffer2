from flask import Blueprint, jsonify, request

from .extensions import db
from .models import Recipe



def home():
    return {"message": "RecipeShare API is running"}


def get_recipes():
    recipes = Recipe.query.order_by(Recipe.created_at.desc()).all()
    return jsonify([recipe.to_dict() for recipe in recipes])


def get_recipe(recipe_id: int):
    recipe = Recipe.query.get_or_404(recipe_id)
    return jsonify(recipe.to_dict())


def create_recipe():
    data = request.get_json() or {}

    missing = [field for field in required_fields if field not in data]
    if missing:
        return {"error": f"Missing required fields: {', '.join(missing)}"}, 400

    recipe = Recipe(
        title=data["title"],
        description=data["description"],
        instructions=data["instructions"],
        prep_time=data["prep_time"],
    )

    db.session.add(recipe)
    db.session.commit()

    return jsonify(recipe.to_dict()), 201

def delete_recipe(recipe_id: int):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
