from unittest import TestCase
from model import ChatGPTModel
import requests

class TestRequest(TestCase):
    def test_request_get(self):
        req=requests.get('https://openai80.p.rapidapi.com/chat/completions')
        self.assertNotEqual(req.status_code,'204')
        
    def test_correct_answer(self):
        answer1=ChatGPTModel('Capital of Poland')
        answer2=ChatGPTModel('Capital of Poland')
        self.assertEqual(answer1.main(), answer2.main())