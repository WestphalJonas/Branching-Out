import json


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)


def filter_users_by_age_range(min_age, max_age):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if min_age <= user["age"] <= max_age]

    for user in filtered_users:
        print(user)


def filter_users_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if email.lower() in user["email"].lower()]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = (
        input(
            "What would you like to filter by? (Options: 'name', 'age', 'age_range', 'email'): "
        )
        .strip()
        .lower()
    )

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        try:
            age_to_search = int(input("Enter an age to filter users: ").strip())
            filter_users_by_age(age_to_search)
        except ValueError:
            print("Please enter a valid age (number).")
    elif filter_option == "age_range":
        try:
            min_age = int(input("Enter minimum age: ").strip())
            max_age = int(input("Enter maximum age: ").strip())
            if min_age > max_age:
                print("Minimum age cannot be greater than maximum age.")
            else:
                filter_users_by_age_range(min_age, max_age)
        except ValueError:
            print("Please enter valid ages (numbers).")
    elif filter_option == "email":
        email_to_search = input(
            "Enter an email or part of an email to filter users: "
        ).strip()
        filter_users_by_email(email_to_search)
    else:
        print(
            "Filtering by that option is not supported. Please choose from: 'name', 'age', 'age_range', 'email'"
        )
