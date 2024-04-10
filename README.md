# JOKE API W/FLASK

Description
This Flask application provides a simple API for managing and retrieving jokes. It allows users to perform various operations such as fetching a random joke, getting a joke by its ID, filtering jokes by type, adding a new joke, modifying an existing joke, and deleting jokes.

Endpoints
GET /random

Returns a random joke from the collection of jokes.
GET /jokes/int:joke_id

Returns the joke with the specified ID.
GET /filter?type=<joke_type>

Returns all jokes of the specified type.
POST /jokes

Adds a new joke to the collection. Requires JSON payload with joke and joketype fields.
PUT /jokes/int:joke_id

Modifies an existing joke with the specified ID. Requires JSON payload with joke and/or joketype fields to update.
PATCH /jokes/int:joke_id

Partially modifies an existing joke with the specified ID. Supports updating joke and/or joketype fields.
DELETE /jokes/int:joke_id

Deletes the joke with the specified ID.
DELETE /jokes?masterkey=<master_key>

Deletes all jokes from the collection. Requires providing a master key as a query parameter for authorization.
