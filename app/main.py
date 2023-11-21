class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self
    pass


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])
    for person in people:
        if person.get("wife") is not None:
            Person.people[person["name"]].wife\
                = Person.people[person["wife"]]
        elif person.get("husband") is not None:
            Person.people[person["name"]].husband\
                = Person.people[person["husband"]]

    return list(Person.people.values())
    pass
