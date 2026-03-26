from app import create_app
from app.extensions import db
from app.models import Recipe, User

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    alice = User(username="alice", email="alice@example.com")
    bob = User(username="bob", email="bob@example.com")
    db.session.add_all([alice, bob])
    db.session.commit()

    recipes = [
        Recipe(
            title="Pasta Primavera",
            description="A fresh vegetable pasta dish.",
            instructions="Boil pasta, sauté vegetables, combine, and serve.",
            prep_time=25,
            user_id=alice.id,
        ),
        Recipe(
            title="Chocolate Cake",
            description="A rich and moist chocolate cake.",
            instructions="Mix ingredients, bake for 35 minutes, and cool before serving.",
            prep_time=60,
            user_id=bob.id,
        ),
    ]

    db.session.add_all(recipes)
    db.session.commit()

    print("Database seeded successfully.")
