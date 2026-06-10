# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using the FastAPI framework to practice routing, request validation, response models, and standard CRUD operations.

## 📝 Tasks

### 🛠️ Create API Endpoints

#### Description

Build a FastAPI application that manages a collection of items. Implement endpoints for listing items, returning a single item by ID, adding new items, updating existing items, and deleting items.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Store items in an in-memory data structure such as a list or dictionary
- Implement `GET /items` to return all items
- Implement `GET /items/{item_id}` to return a single item or a 404 error if not found
- Implement `POST /items` to accept JSON data and add a new item
- Implement `PUT /items/{item_id}` to update an existing item
- Implement `DELETE /items/{item_id}` to remove an item and return a confirmation message

### 🛠️ Add Validation and Documentation

#### Description

Use Pydantic models and FastAPI features to validate incoming data, provide clear endpoint documentation, and support optional query parameters.

#### Requirements
Completed program should:

- Define Pydantic models for item creation and item responses
- Validate request fields such as `name`, `description`, and `price`
- Require `price` to be greater than 0 and `name` to be non-empty
- Accept an optional query parameter for filtering items
- Use response models and endpoint summaries for automatic API docs
- Confirm the app can be browsed with Swagger UI at `/docs` and ReDoc at `/redoc`
