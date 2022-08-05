'''
Created on Jun 03, 2022

@author: error042
'''

class Model:
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.previous_value = ''
        self.value = ''
        self.operator = ''

    def calculate(self, caption):
        if caption == 'C':
            self.value = ''

        elif caption == '+/-':
            self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value

        elif caption == '.':
            if not caption in self.value:
                self.value += caption
            elif self.value[-1] == caption:
                self.value = self.value[:-1]

        elif caption == '%':
            self.operator = '/'
            self.previous_value = self.value
            self.value = '100'
            self.value = str(self._evaluate())

        elif caption == '=':
            self.value = str(self._evaluate())

        elif isinstance(caption, int):
            self.value += str(caption)

        else:
            if self.value:
                self.operator = caption
                self.previous_value = self.value
                self.value = ''

        return self.value

    def _evaluate(self):
        return eval(self.previous_value+self.operator+self.value)