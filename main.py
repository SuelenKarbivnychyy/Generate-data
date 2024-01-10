from faker import Faker
import json

fake = Faker()

def generate_data(amount):
    """Genetares provided amount of fake data """

    data = {}

    for num in range(1, amount):
        data[num] = {}
        data[num]['name'] = fake.name()
        data[num]['address'] = fake.address()
        
    return data



def write_data_to_file(data):

    with open("people_data.json", "w") as file:
        json.dump(data, file)



def create():

    amount = int(input("How many fake data would you like to create? "))
    generate_data(amount)

    print("Your were sucessfully acomplished. You should see a json file created with the requested amount of data on your repository.")

    write_data_to_file(generate_data(amount))

create()

    

