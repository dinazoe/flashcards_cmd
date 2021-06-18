parser.add_argument('-n', type=str, action="store", help="Start a new subject", default=False, dest="new")import json
import argparse
from types import new_class
from lib import colors

possible_arg_list = ["test", "save", "list"]
parser = argparse.ArgumentParser(description='Process the choice.')

parser.add_argument('-t', action="store_true", help="Take the test", default=False, dest="test")
parser.add_argument('-json', type=str, action="store", help="The name of the json file you will be using", default="data", dest="json")
parser.add_argument('-s', action="store_true", help="Save aswers to a subject", default=False, dest="save")
parser.add_argument('-l', action="store_true", help="List the available subjects", default=False, dest="list")
parser.add_argument('-n', type=str, action="store", help="Start a new subject", default=False, dest="new")
parser.add_argument('-h', type=str, action="store", help="Start helper", default=False, dest="helper")

args = parser.parse_args()

def print_jsons() -> None:
    """
    prints the jsons in the main directory of project
    """
    from os.path import isfile, join, dirname, realpath
    from os import listdir

    mypath = dirname(realpath(__file__))
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    json = [f for f in files if ".json" in f]
    print("Below are your subject options")
    print(json)

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

    if args.new != False:
        file_name = args.new
        if ".json" not in file_name:
            file_name = file_name + ".json"
        
        start_new_json(file_name)

    if args.list == True:
        print_jsons()
        exit(0)

    if args.save == True :

        json_name = args.json
        
        if len(args.json) > 0:
            if ".json" not in args.json:
                json_name = args.json + ".json"
            else:
                json_name = args.json

        while True:
            print("Input your question:")
            question = input()
            print("Input your answer:")
            answer = input()

            data = {
                'question': question,
                'answer': answer
            }

            with open(json_name) as json_file:
                d = json.load(json_file)

            d['data'].append(data)

            with open('data.json','w') as f:
                json.dump(d, f)


    if args.test == True:

        json_name = args.json
        
        if len(args.json) > 0:
            if ".json" not in args.json:
                json_name = args.json + ".json"
            else:
                json_name = args.json
        
        while True:
            with open(json_name) as json_file:
                data = json.load(json_file)
            
            for answer in data['data']:
                colors.change_text_color_to_default()
                print("-----------------------")
                
                colors.change_text_color_to_green()
                print(f"{answer['question']}")

                t = input()
                colors.change_text_color_to_blue()
                print(f"{answer['answer']}")


if __name__ == "__main__":
    main()
