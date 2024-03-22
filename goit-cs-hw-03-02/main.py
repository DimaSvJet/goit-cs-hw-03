from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import PyMongoError


client = MongoClient(
    f"mongodb+srv://dimasvjet:Dima159753@dimasvjet.w4aq7vo.mongodb.net/?retryWrites=true&w=majority&appName=DimaSvJet",
    server_api=ServerApi('1')
)

try:
    client.admin.command('ping')
    print('Pinged your deployment. Successfull  connections')
except Exception as e:
    print(e)

db = client.book


def create():
    try:
        name = input("Enter name: ").title()
        age = int(input("Enter age: "))
        features_input = input(
            "List the features of the animal through a comma ")
        features = [feature.strip() for feature in features_input.split(',')]
        document = {"name": name, "age": age, "features": features}
        db.cats.insert_one(document)
        print("Your pet is in a database")
    except PyMongoError as e:
        print(e)
    except ValueError as e:
        print(e)


def find_all():
    result = db.cats.find({})
    for el in result:
        print(el)


def find_name():
    try:
        name = input("Enter name: ").title()
        result = db.cats.find_one({"name": name})
        print(result)
        return result
    except PyMongoError as e:
        print(e)
    except ValueError as e:
        print(e)


def update_age():
    cat = find_name()
    if cat:
        new_age = int(input("Enter new age: "))
        try:
            db.cats.update_one({"name": cat['name']}, {
                               "$set": {"age": new_age}})
            updated_cat = db.cats.find_one({"name": cat['name']})
            print("The pet's age has updated: ", updated_cat)
        except PyMongoError as e:
            print(e)
    else:
        print("No such pet found")


def update_feature():
    cat = find_name()
    if cat:
        try:
            new_feature = input("Enter new feature: ")
            db.cats.update_one({"name": cat['name']}, {
                               "$push": {"features": new_feature}})
            updated_cat = db.cats.find_one({"name": cat['name']})
            print("The pet's feature has added: ", updated_cat)
        except PyMongoError as e:
            print(e)
        except ValueError as e:
            print(e)
    else:
        print("No such pet found")


def delete_all():
    try:
        db.cats.delete_many({})
        print("The database is empty!")
    except PyMongoError as e:
        print(e)


def delete_pet():
    cat = find_name()
    if cat:
        try:
            db.cats.delete_one({"name": cat['name']})
            print(f"The pet {cat['name']} has been deleted: ", cat['name'])
        except PyMongoError as e:
            print(e)
    else:
        print("No such pet found")


def main():
    while True:
        print("Next choice")
        print("1 - Add a new pet")
        print("2 - Show all records")
        print("3 - Show record by the name")
        print("4 - Chenge pet's age")
        print("5 - Add a new feature")
        print("6 - Delete all records")
        print("7 - Delete record by the name")
        print("8 - Exit")
        choice = int(input("Choose your next action: "))

        if choice == 1:
            create()
        elif choice == 2:
            find_all()
        elif choice == 3:
            find_name()
        elif choice == 4:
            update_age()
        elif choice == 5:
            update_feature()
        elif choice == 6:
            delete_all()
        elif choice == 7:
            delete_pet()
        elif choice == 8:
            break
        else:
            print("Uncorrect choice. Please, try again")


if __name__ == "__main__":
    main()
