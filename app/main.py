class Person:
    people = {}

    def __init__(self, person: dict) -> None:
        self.name = person["name"]
        self.age = person["age"]
        self.husband = person["husband"]
        self.wife = person["wife"]
        people[person["name"]] = self


def create_person_list(people: list) -> list:
    # write your code here
    pass
