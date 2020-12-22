def is_string(var, var_name: str):
    ''' Check if var is instance of STRING
        Does nothing if var is string, raises TypeError if not
    '''
    if not isinstance(var, str):
            raise TypeError(var_name+' must be string!')
class Question:
    
    def __init__(self):
        # check parameter
        self._text = None
        self._answer = None
        self._user_answer = None
        self._type = "QandA"

    # Setter & Getter ---------------------------------------------------------
    def set_text(self, text: str):
        # check user input
        is_string(text, 'text')
        self._text = text
        return self
    
    def get_text(self):
        return self._text
   
    def set_answer(self, answer: str):
        # check user input
        is_string(answer, 'answer')
        self._answer = answer
        return self
    
    def get_answer(self):
        return self._answer

    def set_user_answer(self, user_answer: str):
        # check input
        is_string(user_answer, 'user_answer')
        self._user_answer = user_answer
        return self
    
    def get_user_answer(self):
        return self._user_answer
    
    def get_type(self):
        return self._type
    # -------------------------------------------------------------------------
    
    def verify(self):
        '''
        Return -1: no user input, True, False
        '''
        if self._user_answer:
            return self._user_answer == self._answer
        return -1

    def __str__(self):
        return ('Question:' + '{text:' + self.get_text() +
                ', answer:' + self.get_answer() + '}')

if __name__ == '__main__':
    q = Question()
    q.set_text('7x7=?').set_answer('49')
    print(q)

