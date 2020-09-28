# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we"ll use handle the lightweight sqlite database. You"ll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we"ll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 


## Tasks - @DONE

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

## Endpoints

### GET `/categories`

- Retrieves all categories.
- Request parameters: 
  - NONE
- Response JSON:
```json
    {
        "success": true,
        "categories": {
            1: "Science", 
            2: "Art", 
            3: "Geography", 
            4: "History", 
            5: "Entertainment", 
            6: "Sports"
        }, 
        "total_categories": 6
    }
```

#### GET `/questions`

- Returns all questions in paginated form.
- Request parameters: 
  - NONE
- Response JSON:
```json
    {
        "success": true,
        "questions": [
            {
                "answer": "Apollo 13", 
                "category": 5, 
                "difficulty": 4, 
                "id": 2, 
                "question": "What movie earned To..., in 1996?"
            }, 
            {
                "answer": "Tom Cruise", 
                "category": 5, 
                "difficulty": 4, 
                "id": 4, 
                "question": "What actor did autho...ed Lestat?"
            }, 
            {
                "answer": "Maya Angelou", 
                "category": 4, 
                "difficulty": 2, 
                "id": 5, 
                "question": "Whose autobiography ...?"
            }, 
            {
                "answer": "Edward Scissorhands", 
                "category": 5, 
                "difficulty": 3, 
                "id": 6, 
                "question": "What was the title o...ppendages?"
            }, 
            {
                "answer": "Muhammad Ali", 
                "category": 4, 
                "difficulty": 1, 
                "id": 9, 
                "question": "What boxer...sius Clay?"
            }, 
            {
                "answer": "Brazil", 
                "category": 6, 
                "difficulty": 3, 
                "id": 10, 
                "question": "Which is the only te...ournament?"
            }, 
            {
                "answer": "Uruguay",
                "category": 6, 
                "difficulty": 4, 
                "id": 11, 
                "question": "Which country won th...p in 1930?"
            }, 
            {
                "answer": "George Washington Carver",
                "category": 4, 
                "difficulty": 2, 
                "id": 12, 
                "question": "Who invented Peanut Butter?"
            }, 
            {
                "answer": "Lake Victoria",
                "category": 3, 
                "difficulty": 2, 
                "id": 13, 
                "question": "What is the largest ...in Africa?"
            }, 
            {
                "answer": "The Palace of Versailles",
                "category": 3, 
                "difficulty": 3, 
                "id": 14, 
                "question": "In which royal palac...f Mirrors?"
            }
        ],
        "total_questions": 25,
        "categories": ["Science", "Art", "Geography", "History", "Entertainment", "Sports"]
    }
```

### DELETE `/questions/<int:question_id>`

- Deletes the question with the specified ID
- Request Parameters: 
  - question_id - ID of question to be deleted
- Response JSON:
```json
    {
        "success": true,
        "deleted": 35,
        "questions": [
        {
            "answer": "Apollo 13", 
            "category": 5, 
            "difficulty": 4, 
            "id": 2, 
            "question": "What movie earned To..., in 1996?"
        }, 
        {
            "answer": "Tom Cruise", 
            "category": 5, 
            "difficulty": 4, 
            "id": 4, 
            "question": "What actor did autho...ed Lestat?"
        }, 
        {
            "answer": "Maya Angelou", 
            "category": 4, 
            "difficulty": 2, 
            "id": 5, 
            "question": "Whose autobiography ...?"
        }, 
        {
            "answer": "Edward Scissorhands", 
            "category": 5, 
            "difficulty": 3, 
            "id": 6, 
            "question": "What was the title o...ppendages?"
        }, 
        {
            "answer": "Muhammad Ali", 
            "category": 4, 
            "difficulty": 1, 
            "id": 9, 
            "question": "What boxer...sius Clay?"
        }, 
        {
            "answer": "Brazil", 
            "category": 6, 
            "difficulty": 3, 
            "id": 10, 
            "question": "Which is the only te...ournament?"
        }, 
        {
            "answer": "Uruguay", 
            "category": 6, 
            "difficulty": 4, 
            "id": 11, 
            "question": "Which country won th...p in 1930?"
        }, 
        {
            "answer": "George Washington Carver", 
            "category": 4, 
            "difficulty": 2, 
            "id": 12, 
            "question": "Who invented Peanut Butter?"
        }, 
        {
            "answer": "Lake Victoria", 
            "category": 3, 
            "difficulty": 2, 
            "id": 13, 
            "question": "What is the largest ...in Africa?"
        }, 
        {
            "answer": "The Palace of Versailles", 
            "category": 3, 
            "difficulty": 3, 
            "id": 14, 
            "question": "In which royal palac...f Mirrors?"
        }
        ],
        "total_questions": 25
    }
```

### POST `/questions`

- Creates a new question or search for questions with specified search phrase based on whether the search field in the UI is filled in.
- Request parameters:
  - NONE (form body is sent in through form submission)
- Response: JSON
  - 1. Adding new question
```json
    {
        "success": true,
        "created": 35,
        "questions": [
        {
            "answer": "Apollo 13", 
            "category": 5, 
            "difficulty": 4, 
            "id": 2, 
            "question": "What movie earned To..., in 1996?"
        }, 
        {
            "answer": "Tom Cruise", 
            "category": 5, 
            "difficulty": 4, 
            "id": 4, 
            "question": "What actor did autho...ed Lestat?"
        }, 
        {
            "answer": "Maya Angelou", 
            "category": 4, 
            "difficulty": 2, 
            "id": 5, 
            "question": "Whose autobiography ...?"
        }, 
        {
            "answer": "Edward Scissorhands", 
            "category": 5, 
            "difficulty": 3, 
            "id": 6, 
            "question": "What was the title o...ppendages?"
        }, 
        {
            "answer": "Muhammad Ali", 
            "category": 4, 
            "difficulty": 1, 
            "id": 9, 
            "question": "What boxer...sius Clay?"
        }, 
        {
            "answer": "Brazil", 
            "category": 6, 
            "difficulty": 3, 
            "id": 10, 
            "question": "Which is the only te...ournament?"
        }, 
        {
            "answer": "Uruguay", 
            "category": 6, 
            "difficulty": 4, 
            "id": 11, 
            "question": "Which country won th...p in 1930?"
        }, 
        {
            "answer": "George Washington Carver", 
            "category": 4, 
            "difficulty": 2, 
            "id": 12, 
            "question": "Who invented Peanut Butter?"
        }, 
        {
            "answer": "Lake Victoria", 
            "category": 3, 
            "difficulty": 2, 
            "id": 13, 
            "question": "What is the largest ...in Africa?"
        }, 
        {
            "answer": "The Palace of Versailles", 
            "category": 3, 
            "difficulty": 3, 
            "id": 14, 
            "question": "In which royal palac...f Mirrors?"
        }
        ],
        "total_questions": 26
    }
```
  - 2. Search for questions
```json
    {
        "success": true,
        "questions": [
        {
            "answer": "Tom Cruise",
            "category": 5,
            "difficulty": 4,
            "id": 4,
            "question": "What actor did auth...her beloved Lestat?"
        }
        ],
        "total_questions": 26
    }
```

### GET `/categories/<int:category_id>/questions`

- Retrieves questions by category based on the category ID from the url.
- Request parameters: 
  - category_id - ID of category interested
- Response: JSON
```json
    {
        "success": true,
        "questions": [
        {
            "answer": "Lake Victoria", 
            "category": 3, 
            "difficulty": 2, 
            "id": 13, 
            "question": "What is the largest ...in Africa?"
        }, 
        {
            "answer": "The Palace of Versailles", 
            "category": 3, 
            "difficulty": 3, 
            "id": 14, 
            "question": "In which royal palac...f Mirrors?"
        }, 
        {
            "answer": "Agra", 
            "category": 3, 
            "difficulty": 2, 
            "id": 15, 
            "question": "The Taj Mahal is loc...dian city?"
        }
        ],
        "current_category": "Geography",
        "total_questions": 25
    }
```

### POST `/quizzes`

- Retrieves random question from the same category which is not in previous question list.
- Request parameters:
  - NONE (form body is sent in through form submission)
- Response JSON:
```json
    {
        "success": true,
        "question": {
            "answer": "George Washington Carver",
            "category": 4,
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
        }
    }

```
## Error Handling

Errors are returned in the following JSON format:
```json
      {
        "success": "False",
        "error": 404,
        "message": "Not Found",
      }
```

The error codes currently returned are:

* 400 – Bad Request
* 404 – Not Found
* 405 - Method Not Allowed
* 406 - Not Acceptable
* 422 – Unprocessable
* 500 – Something"s Not Right

## Testing

To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```