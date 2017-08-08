import unittest
from part_11_class import AnnonymousSurvey

class TestAnnonymousSurvey(unittest.TestCase):
    '''Test AnnonymousSurvey'''
    def setUp(self):
        '''Create survey'''
        question = 'What language did you first learn to speak?'
        self.my_survey = AnnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Ukranian']

    def test_store_single_response(self):
        '''single'''
        #question = 'What language did you first learn to speak?'
        #my_survey = AnnonymousSurvey(question)
        #my_survey.store_response('English')
        #self.assertIn('English', my_survey.responses)
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        '''three responses'''
        #question = 'What language did you first learn to speak?'
        #my_survey = AnnonymousSurvey(question)
        #responses = ['English', 'Spanish', 'Ukranian']
        #for response in responses:
         #   my_survey.store_response(response)
        #for response in responses:
         #   self.assertIn(response, my_survey.responses)
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
#
if __name__ == '__main__':
    unittest.main()