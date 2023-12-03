import pickle


def filter_dump(filename, objects: list, typename: type):
    with open(filename, 'wb') as file:
        pickle.dump([obj for obj in objects if type(obj) == typename], file)
