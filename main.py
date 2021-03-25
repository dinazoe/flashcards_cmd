import json

print("What function do you want to run? 1 for saving questions and answers and 2 for listing questions and answers")

possible_answers = ["1", "2"]

wanted_function = input()

def start_new_json(file_name):
    start = """
    {
        "data": [

        ]
    }

    """

    file = open(file_name, "w")
    file.write(start)
    file.close()

def append_json(file_name, new_data):
    with open(file_name) as data_file:    
        old_data = json.load(data_file)

    old_data['data'].append(new_data)

    with open(file_name, 'w') as outfile:
        json.dump(old_data, outfile)

def main():
    if wanted_function == "1":
        while True:
            print("Input your question:")
            question = input()
            print("Input your answer:")
            answer = input()

            data = {
                'question': question,
                'answer': answer
            }

            with open('data.json') as json_file:
                d = json.load(json_file)

            d['data'].append(data)

            with open('data.json','w') as f:
                json.dump(d, f)


    if wanted_function == "2":
        while True:
            with open('data.json') as json_file:
                data = json.load(json_file)
            
            for answer in data['data']:
                

                print(f"{answer['question']}")

                t = input()
                print(f"{answer['answer']}")


if wanted_function in possible_answers:
    main()
else:
    print("You have to input either 1 or 2")