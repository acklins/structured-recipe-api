
from fastapi import APIRouter, HTTPException

router = APIRouter()

# In-memory "database" — a simple list of dicts.

recipes: list[dict] = [
    {"id": 1, "title": "Pasta Carbonara", "cuisine": "Italian", "servings": 2},
    {"id": 2, "title": "Tacos al Pastor", "cuisine": "Mexican", "servings": 4},
]

# Simple counter to generate new IDs
_next_id = 3

#Returns all recipes.
@router.get("/")
def list_recipes():
    return recipes

# returns a single recipe by id
# Return 404 if not found
@router.get("/{recipe_id}")#path parameter creates var part of url

def get_recipe(recipe_id: int):

#loops through every recipe.
    for recipe in recipes:

#compares stored ID with the requested ID in the url
        if recipe["id"] == recipe_id:
            return recipe
    raise HTTPException(status_code=404, detail="Recipe not found")

# Creates a new recipe with its new id and HTTP 201
@router.post("/", status_code=201)
def create_recipe(recipe: dict):
#use id outside of function
    global _next_id
#new dict; id comes from counter
    new_recipe = {
        "id": _next_id,
        "title": recipe["title"],
        "cuisine": recipe["cuisine"],
        "servings": recipe["servings"],
        "ingredients": recipe["ingredients"]
    }
#add recipe to our pretend db
    recipes.append(new_recipe)

#increment the id
    _next_id += 1
    return new_recipe