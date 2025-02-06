"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()

    read_file = open(filename)

    for line in read_file:
        unique_species = line.rstrip().split("|")[1]
        species.add(unique_species)
    
    return species

all_species("villagers.csv")

def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    read_file = open(filename)

    for line in read_file:
        name, species = line.rstrip().split("|")[0:2]

        if search_string in ("All", species):
            villagers.append(name)
            
    return sorted(villagers)

get_villagers_by_species("villagers.csv", "All")


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []

    read_file = open(filename)

    for line in read_file:
        name, hobby = line.rstrip().split("|")[0:4:3]

        if hobby == "Fitness":
            fitness.append(name)
        elif hobby == "Nature":
            nature.append(name)
        elif hobby == "Education":
            education.append(name)
        elif hobby == "Music":
            music.append(name)
        elif hobby == "Fashion":
            fashion.append(name)
        elif hobby == "Play":
            play.append(name)

    return [sorted(fitness), sorted(nature), sorted(education),
             sorted(music), sorted(fashion), sorted(play)]

all_names_by_hobby("villagers.csv")

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    read_file = open(filename)

    for line in read_file:
        all_data_tuple = tuple(line.rstrip().split("|"))
        all_data.append(all_data_tuple)

    return all_data

all_data("villagers.csv")

def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """
    read_file = open(filename)

    for line in read_file:
        name = line.rstrip().split("|")[0]
        motto = line.rstrip().split("|")[4]

        if name == villager_name:
            return motto
    
    return None

find_motto("villagers.csv", "Ash")


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    likeminded_villagers = set()

    read_file = open(filename)
        
    personality = None

    for line in read_file:
        name = line.rstrip().split("|")[0]
        villager_personality = line.rstrip().split("|")[2]

        if name == villager_name:
            personality = villager_personality
            break

    if personality:
        for line in read_file:
            name = line.rstrip().split("|")[0]
            villager_personality = line.rstrip().split("|")[2]

            if villager_personality == personality:
                likeminded_villagers.add(name)

    return likeminded_villagers

find_likeminded_villagers("villagers.csv", "Cyrano")        

