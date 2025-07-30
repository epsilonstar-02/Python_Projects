# Day 66 - Cafe & WiFi API

## Building RESTful APIs with Flask

This project demonstrates how to build a RESTful API using Flask and SQLAlchemy. The API manages a database of cafes with WiFi and power sockets for remote working.

### Features:
- **RESTful API Design**: Implements all HTTP methods (GET, POST, PATCH, DELETE)
- **SQLAlchemy ORM**: Database operations with modern SQLAlchemy syntax
- **JSON Responses**: All API endpoints return JSON data
- **Error Handling**: Proper HTTP status codes and error messages
- **API Security**: DELETE operations require API key authentication

### API Endpoints:

#### GET Endpoints:
- `GET /` - Homepage with API documentation
- `GET /random` - Returns a random cafe from the database
- `GET /all` - Returns all cafes in the database
- `GET /search?loc=LOCATION` - Search cafes by location

#### POST Endpoints:
- `POST /add` - Add a new cafe (requires form data with cafe details)

#### PATCH Endpoints:
- `PATCH /update-price/<cafe_id>?new_price=PRICE` - Update coffee price for a specific cafe

#### DELETE Endpoints:
- `DELETE /report-closed/<cafe_id>?api-key=KEY` - Delete a cafe (requires API key: "TopSecretAPIKey")

### Database Schema:
The Cafe model includes:
- `id` - Primary key
- `name` - Cafe name (unique)
- `map_url` - Google Maps URL
- `img_url` - Cafe image URL
- `location` - Cafe location/neighborhood
- `seats` - Number of seats available
- `has_toilet` - Boolean for toilet availability
- `has_wifi` - Boolean for WiFi availability
- `has_sockets` - Boolean for power socket availability
- `can_take_calls` - Boolean for call-friendly environment
- `coffee_price` - Average coffee price

### Installation:
```bash
pip install flask flask-sqlalchemy
```

### Usage:
1. Run the Flask application: `python main.py`
2. Access the homepage at `http://localhost:5000`
3. Use the API endpoints as documented above

### Example API Calls:

**Get Random Cafe:**
```
GET http://localhost:5000/random
```

**Add New Cafe:**
```
POST http://localhost:5000/add
Content-Type: application/x-www-form-urlencoded

name=Great Coffee&map_url=https://maps.google.com&img_url=https://example.com/image.jpg&loc=Shoreditch&sockets=1&toilet=1&wifi=1&calls=0&seats=20&coffee_price=£2.50
```

**Update Price:**
```
PATCH http://localhost:5000/update-price/1?new_price=£3.00
```

**Delete Cafe:**
```
DELETE http://localhost:5000/report-closed/1?api-key=TopSecretAPIKey
```

This project teaches REST API principles, HTTP methods, status codes, and building production-ready APIs with Flask.
