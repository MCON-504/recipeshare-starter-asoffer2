# RecipeShare Flask Starter

A starter Flask backend for a **RecipeShare** project using:

- Flask
- PostgreSQL
- Flask-SQLAlchemy
- Flask-Migrate
- python-dotenv



## Project Structure

```text
recipeshare-flask-starter/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│   ├── models.py
│   └── routes.py
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── run.py
└── seed.py
```

## Features Included

- Flask app factory
- PostgreSQL configuration via environment variables
- SQLAlchemy models for `User` and `Recipe`
- Relationship: one user can have many recipes
- Basic API endpoints:
  - `GET /`
  - `GET /api/recipes`
  - `GET /api/recipes/<id>`
  - `POST /api/recipes`
- Seed script with starter data

## 1. Create and activate a virtual environment

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows PowerShell

```cmd
python -m venv .venv
.venv\Scripts\Activate.bat
```

## 2. Install dependencies

The project requires the following packages:

#### Core

| Package | Version | Purpose |
|---|---|---|
| `Flask` | 3.1.0 | Web framework |
| `Flask-SQLAlchemy` | 3.1.1 | ORM integration |
| `Flask-Migrate` | 4.0.7 | Database migrations (Alembic) |
| `psycopg2-binary` | 2.9.10 | PostgreSQL adapter |
| `python-dotenv` | 1.0.1 | Load `.env` variables |

#### Authentication

| Package | Version | Purpose |
|---|---|---|
| `Flask-Login` | 0.6.2 | Session-based user login |
| `Flask-Security` | 5.1.0 | Role & security management |
| `Flask-JWT-Extended` | 4.4.4 | JWT token authentication |

Install all packages at once:

```bash
pip install -r requirements.txt
```

## 3. Create the PostgreSQL database

In PostgreSQL:

```sql
CREATE DATABASE recipeshare;
```

## 4. Set environment variables

Copy `.env.example` to `.env` and update the connection string.

Example:

```env
DATABASE_URL=postgresql://postgres:password@localhost/recipeshare
FLASK_APP=run.py
FLASK_ENV=development
```

## 5. Initialize migrations

```bash
flask db init
flask db migrate -m "Create user and recipe tables"
flask db upgrade
```

## 6. Seed the database

```bash
python seed.py
```

## 7. Run the app

```bash
flask run
```

Or:

```bash
python run.py
```

## Sample Endpoints

### Get all recipes

```http
GET /api/recipes
```

### Get one recipe

```http
GET /api/recipes/1
```

### Create a recipe

```http
POST /api/recipes
Content-Type: application/json
```

Example body:

```json
{
  "title": "Tomato Soup",
  "description": "Simple homemade soup.",
  "instructions": "Cook tomatoes, blend, and simmer.",
  "prep_time": 30,
  "user_id": 1
}
```

---

## 8. Examining Database Changes

Use `psql` to inspect the database directly as you interact with the API. This helps you understand how HTTP requests translate into real database operations.

### Open a psql session

```bash
psql -U postgres -d recipeshare
```

> Replace `postgres` with your PostgreSQL username if different.

---

### View existing data

```sql
-- See all users
SELECT * FROM users;

-- See all recipes
SELECT * FROM recipes;

-- See recipes with their owner's name
SELECT recipes.id, recipes.title, users.username
FROM recipes
JOIN users ON recipes.user_id = users.id;
```

---

### After adding a record (POST)

1. Make a `POST /api/recipes` request (via curl, Postman, or your frontend).
2. In psql, run:

```sql
SELECT * FROM recipes ORDER BY id DESC LIMIT 5;
```

You should see the new recipe at the top of the results.

---

### After updating a record (PUT / PATCH)

1. Make an update request to modify a recipe.
2. In psql, confirm the change:

```sql
SELECT id, title, description, prep_time FROM recipes WHERE id = <your_recipe_id>;
```

Compare the values before and after your request to verify the update was applied.

---

### After deleting a record (DELETE)

1. Make a `DELETE` request for a specific recipe.
2. In psql, confirm the row is gone:

```sql
SELECT * FROM recipes WHERE id = <your_recipe_id>;
```

You should get **0 rows** back if the delete was successful.

---

### Tip: count rows

A quick way to check how many records exist before and after an operation:

```sql
SELECT COUNT(*) FROM recipes;
SELECT COUNT(*) FROM users;
```

---

### Exit psql

```bash
\q
```


