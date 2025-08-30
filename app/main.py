class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_persons = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for person in people:
        person_class = Person.people[person["name"]]
        if person.get("wife"):
            person_class.wife = Person.people[person["wife"]]
        elif person.get("husband"):
            person_class.husband = Person.people[person["husband"]]

    return list_of_persons
