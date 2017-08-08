from part_11_class import AnnonymousSurvey
question = 'Wat language did you first learn to speak?'
my_survey = AnnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time to quit ")
while True:
    response = input('Lenguage: ')
    if response == 'q':
        break
    my_survey.store_response(response)

print("\n Thank you ...")
my_survey.show_results()