import requests
from decouple import config

class NotValidInputError(ValueError):
    def __init__(self,value) -> str:
        super().__init__(f"Your input == {value} is not valid, please check!")
    
    
class ChatGPTModel:
    def __init__(self,userInput,role=None):
        self.userInput=userInput
        self.url='https://openai80.p.rapidapi.com/chat/completions'
        self.role='user'

    def main(self):
            if self.userInput == '1':
                print("Debug: Completed at self.userInput=='1'")
                return NotValidInputError(self.userInput)
            elif self.userInput:
                payload = {
                "model": "gpt-3.5-turbo",
                "messages": [
                    {
                        "role": f"{self.role}",
                        "content": f"{self.userInput}"
                    }
                    ]
                }
                headers = {
                    "content-type": "application/json",
                    "X-RapidAPI-Key": "{}".format(config('API')),
                    "X-RapidAPI-Host": "openai80.p.rapidapi.com"
                }

                response = requests.request("POST", self.url, json=payload, headers=headers)
                response.text
                return response.json()['choices'][0]['message']['content']
            else:
                print('Debug input is not valid')   
                return RuntimeError     

