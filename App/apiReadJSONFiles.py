# Here we will define our base directory and you will be reading the JSON files within the data folder and get the results
import json
BASE_DIR = r"C:\Dev\GenAI-AgenticAICERT/"  # we are giving our base directory and at the end forward slash/ so that it can go inside "data" folder
#Now we will read users from users.json
def read_user():
    with open(f"{BASE_DIR}data/users.json") as stream:    #stream is just a variable
        users = json.load(stream)
        return users

#Now we will read position and return question from questions.json
def read_questions(position: int):
    with open(f"{BASE_DIR}data/questions.json") as stream:
        questions = json.load(stream)

    for question in questions:
        if question['position'] == position:
            res = question.get('question')
            print(res)
            return res

#Now we will read question_id and return alternative from alteratives.json
def read_alternatives(question_id: int):
    with open(f"{BASE_DIR}data/alternatives.json") as stream:
        alternatives = json.load(stream)

    for alternative in alternatives:
        if alternative['question_id'] == question_id:
            res = alternative.get('alternative')
            print(res)
            return res


#Now we will write the logic for User to be able to call the information from JSON
#below is the space where user will give the input
#below will be API interface for user
if __name__ == "__main__":
    print(read_user()) #reading user from users.json
    read_questions(1)  #User is giving position and API will return question
    read_alternatives(1) #User is giving question_id and API will return alternative