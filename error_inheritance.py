
class BotModelError:
    @staticmethod
    def error():
         ...
    

class NotValidInputError(ValueError):
    """Ovewriting ValueError returns a string of wrong input with message1"""
    def __init__(self,value) -> str:
        super().__init__(f"Your input == {value} is not valid, please check!")
    
