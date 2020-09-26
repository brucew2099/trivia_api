import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app 
from models import setup_db, Question, Category

from config import SQLALCHEMY_TEST_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client

        self.app.config.from_object('config')
        self.app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_TEST_DATABASE_URI
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS

        #setup_db(self.app)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.repeated_question = {
            'question': 'What is the largest lake in Africa?',
            'answer': 'Lake Victoria', 
            'category': 2, 
            'difficulty': 3, 
        }

        self.new_question = {
            'question': 'Who is the 16th president of the United States of America?',
            'answer': 'Abraham Lincoln', 
            'category': 4,
            'difficulty': 2, 
        }
    
    def tearDown(self):
        """Executed after reach test"""

    """
    TODO
    Write at least one test for each service for successful operation and for expected errors.
    """

    def test_get_all_categories_success(self):
        result = self.client().get('/categories')
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'].get('1'), 'Science')
        self.assertTrue(data['total_categories'], len(Category.query.all()))

    def test_get_all_categories_post(self):
        result = self.client().post('/categories')
        data = json.loads(result.data)   
        self.assertEqual(result.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method Not Allowed')

    def test_get_all_categories_error(self):
        result = self.client().post('/categorie')
        data = json.loads(result.data)   
        self.assertEqual(result.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found')

    def test_delete_question_success(self):
        result = self.client().delete('/questions/24')
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 24)

    def test_delete_question_get(self):
        result = self.client().get('/questions/24')
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual('deleted' in data, False) 

    def test_delete_question_error(self):
        result = self.client().delete('/questions/999')
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual('deleted' in data, False) 

    def test_search_question_success(self):
        result = self.client().post('/questions', json={'searchTerm': 'Tom'})
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))

    def test_search_question_error(self):
        result = self.client().post('/questions', json={'searchTerm': 'kc'})
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertTrue('Unprocessable' in data['message'], True)

    def test_create_question_success(self):
        result = self.client().post('/questions', json=self.new_question)
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['created'] is not None, True)

    def test_create_question_error_repeated(self):
        result = self.client().post('/questions', json=self.repeated_question)
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertTrue('Unprocessable' in data['message'], True)

    def test_create_or_search_question_empty_payload(self):
        result = self.client().post('/questions')
        data = json.loads(result.data)
        self.assertEqual(result.status_code, 406)
        self.assertEqual(data['success'], False)
        self.assertTrue('Not Acceptable' in data['message'], True)

    def test_get_questions_by_category_success(self):
        result = self.client().get('/categories/1/questions')
        data = json.loads(result.data)
        self.assertEqual(data['success'], True)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['questions'] is not None, True)
        self.assertEqual(data['current_category'], 'Art')
        self.assertEqual(int(data['total_questions']), 4)

    def test_get_questions_by_category_post(self):
        result = self.client().post('/categories/1/questions')
        data = json.loads(result.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(result.status_code, 405)
        self.assertEqual('Method Not Allowed' in data['message'], True)

    def test_get_questions_by_category_error(self):
        result = self.client().get('/categories/100/questions')
        data = json.loads(result.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(result.status_code, 422)
        self.assertEqual('Unprocessable' in data['message'], True)

    def test_get_random_questions_for_quiz_success(self):
        result = self.client().post('/quizzes', json={'previous_questions': [], 'quiz_category': {'id': 0, 'type': 'click'}})
        data = json.loads(result.data)
        self.assertEqual(data['success'], True)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['question'] is not None, True)

    def test_get_random_questions_for_quiz_success_previous(self):
        result = self.client().post('/quizzes', json={'previous_questions': [15], 'quiz_category': {'id': 2, 'type': 'click'}})
        data = json.loads(result.data)
        self.assertEqual(data['success'], True)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['question'] is not None, True)

    def test_get_random_questions_for_quiz_error_empty(self):
        result = self.client().post('/quizzes')
        data = json.loads(result.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(result.status_code, 422)
        self.assertEqual('Unprocessable' in data['message'], True)

    def test_get_random_questions_for_quiz_error_get(self):
        result = self.client().get('/quizzes')
        data = json.loads(result.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(result.status_code, 405)
        self.assertEqual('Method Not Allowed' in data['message'], True)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()