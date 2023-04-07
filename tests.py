from unittest import TestCase
from model import ChatGPTModel,NotValidInputError
import requests
from bot import TOKEN


class TestRequest(TestCase):
    def setUp(self):
        model=ChatGPTModel()

    def test_request_get(self):
        req=requests.get('https://openai80.p.rapidapi.com/chat/completions')
        self.assertNotEqual(req.status_code,'204')
        
    def test_correct_answer(self):
        answer1=self.model('Capital of Poland')
        self.assertEqual(answer1.main(), 'Warsaw')

    def test_user_input(self):
        with self.assertRaises(NotValidInputError):
            resp=ChatGPTModel(' ').main()


    def test_bot_token(self):
        self.assertIsNone(TOKEN,'')
