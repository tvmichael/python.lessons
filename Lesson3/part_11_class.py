class AnnonymousSurvey():
    '''Збір анонмних відповідей'''

    def __init__(self, question):
        '''зберігаємо аноніміні запитанні і відповіді'''
        self.question = question
        self.responses = []

    def show_question(self):
        '''виводимо запитання'''
        print(self.question)

    def store_response(self, new_response):
        '''зберігаємо відповіді'''
        self.responses.append((new_response))

    def show_results(self):
        '''виводимо усі отримані відповіді'''
        print('Survey results')
        for response in self.responses:
            print('- '+ response)
