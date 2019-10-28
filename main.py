import json

CURRENT_TURN = 0
DOCTORS_MOVES_COUNT = 2
ASSISTANTS_MOVES_COUNT = 2
PLAGUE_MOVES_COUNT = 1


def read_json_data(path):
    ''' Read data from json file
    Returns
    -------
    dict
        json readed into python dict
    '''
    with open(path, 'r') as file:
        return json.load(file)


paths = read_json_data('data/paths.json')

# TODO: create all characters and fill it with correct data
characters = read_json_data('data/characters.json')

# TODO: create all skills
skills = read_json_data('data/skills.json')

# TODO: create all strains
strains = read_json_data('data/strains.json')

game_map = {
    '1' : {
        'name': '',
        'characters' : [],
        'strains' : [],
        'mission' : False,
        },
    '2' : {
        'name': '',
        'characters' : [],
        'strains' : [],
        'mission' : False,
        },
    '3' : {
        'name': '',
        'characters' : [],
        'strains' : [],
        'mission' : False,
        },
    '4' : {
        'name': '',
        'characters' : [],
        'strains' : [],
        'mission' : False,
        },
    '5' : {
        'name': '',
        'characters' : [],
        'strains' : [],
        'mission' : False,
        },
    '6' : {
        'name': '',
        'characters' : [],
        'strains' : [],
        'mission' : False,
        },
    '7' : {
        'name': '',
        'characters' : [],
        'strains' : [],
        'mission' : False,
        },
    '8' : {
        'name': '',
        'characters' : [],
        'strains' : [],
        'mission' : False,
        },
    '9' : {
        'name': '',
        'characters' : [],
        'strains' : [],
        'mission' : False,
        },
    '10' : {
        'name': '',
        'characters' : [],
        'strains' : [],
        'mission' : False,
        },
    '11' : {
        'name': '',
        'characters' : [],
        'strains' : [],
        'mission' : False,
        },
    '12' : {
        'name': '',
        'characters' : [],
        'strains' : [],
        'mission' : False,
        },
    '13' : {
        'name': '',
        'characters' : [],
        'strains' : [],
        'mission' : False,
        },
    '14' : {
        'name': '',
        'characters' : [],
        'strains' : [],
        'mission' : False,
        },
    '15' : {
        'name': '',
        'characters' : [],
        'strains' : [],
        'mission' : False,
        },
}



def get_doctors():
    ''' Get all doctors from characters

    Returns
    -------
    dict
        Dictionary like <characters> but with doctors only
    '''
    # doc_ids = ['-1', '-2', '-3']
    doc_ids = ['-1']
    doctors = {}
    for doc_id in doc_ids:
        doctors[doc_id] = characters[doc_id]
    return doctors


def place_character(place, character):
    ''' Places character to possition on the map

    Parameters
    ----------
    place : str
        id of possition to place character
    character : str
        id of character
    '''
    game_map[place]['characters'].append(character)
    characters[character]['current_possition'] = place


def initial_placing():
    ''' Initial placement of characters
    Fills <game_map> with charactes id
    and puts <current_possition> to characters
    Each player can place any avaliable character 
    to any avaliable place exept Steepe (0)
    Turn order: (Bachelor -> Haruspex -> Devotress) X 3 -> Plague
    Plague can be placed in any empty spot and Steepe (0)
    '''

    avaliable_assistants = {
        'Bachelor' : ['-1', '1', '2', '3'],
        'Haruspex' : ['-2', '4', '5', '6'],
        'Devotress' : ['-3', '7', '8', '9'],
    } # -X for doctors

    avaliable_places = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']

    doctors = [x[1] for x in characters.items() if '-' in x[0]]
    print(doctors)

    for i in range(4):
        for doctor in doctors:
            doctor_name = doctor['name']
            assistants_to_be_placed = avaliable_assistants[doctor_name]
            print(assistants_to_be_placed)

            character = ''
            while 1:
                print(f'{doctor_name} - {assistants_to_be_placed}')
                character = input()

                if character in assistants_to_be_placed:
                    break
                else:
                    print('This character is already placed. Input another one.')
            
            place = ''
            while 1:
                print(f'Input place')
                print(f'Avaliable places: {avaliable_places}')

                place = input()

                if place in avaliable_places:
                    break
                else:
                    print('This place is occupied. Input another one.')

            place_character(place, character)
            avaliable_places.remove(place)
            avaliable_assistants[doctor_name].remove(character)

    avaliable_places.append('0') # Plague can start in steepe
    plague_place = ''
    print('\n' + '-' * 21)
    while 1:
        print('Input plauge starting place')
        print(f'Avaliable places: {avaliable_places}')

        plague_place = input()

        if plague_place in avaliable_places:
            break
        else:
            print('This place is occupied. Input another one.')
    
    place_character(plague_place, '0')
    print('Plague placed')
    print('-' * 21)


def move_to(character, place):
    '''
    Parameters
    ----------
    character : str
        id of character
    place : str
        id of place
    '''
    current_possition = characters[character]['current_possition']
    # Update character possition
    characters[character]['current_possition'] = place
    # Remove character old possition from game map
    game_map[current_possition]['characters'].remove(character)
    # Update game map with new character possition
    game_map[place]['characters'].append(character)
    print(f'{character} moved from {current_possition} to {place}')
  

def move(character):
    '''
    Shows avaliable moves and asks to input place then moves character.
    '''

    moves_count = 0
    if character in ['-1', '-2', '-3']:
        moves_count = DOCTORS_MOVES_COUNT
    elif character == '0':
        moves_count = PLAGUE_MOVES_COUNT
    else:
        moves_count = ASSISTANTS_MOVES_COUNT

    print(f'Avaliable moves count = {moves_count}')
    for i in range(moves_count):
        print(f'Performing move {i}')
        current_possition = characters[character]['current_possition']
        avaliable_moves = paths[current_possition]
        # Remove Steepe from avaliable moves if character not Plague
        if character != '0' and '0' in avaliable_moves:
            avaliable_moves.remove('0')

        print(f'Avaliable moves: {avaliable_moves}')
        print('Write "q" to stop')
        user_input = ''
        while 1:
            user_input = input('Input move: ')

            if user_input in avaliable_moves:
                break
            else:
                print('Cant move here')

        if user_input == 'q':
            break
        else:
            move_to(character, user_input)


def pick_skill(character):
    ''' Pick a skill from avaliable for this character

    Parameters
    ----------
    character : str
        character id
    '''
    doctors_skills = [x[0] for x in skills.items() if x[1]['doctor'] == character]
    avaliable_skills = [x for x in doctors_skills if x not in characters[character]['skills_played']]
    doctor_name = characters[character]['name']

    print(f'Pick a skill for {doctor_name}')
    print(f'Avaliable skills: {avaliable_skills}')

    user_input = ''
    while 1:
        user_input = input('Input skill: ')

        if user_input in avaliable_skills:
            break
        else:
            print('Cant pick this skill')
    
    characters[character]['skills_in_hand'].append(user_input)
    del skills[user_input]


def get_strain_from_deck():
    '''
    TODO : implement this
    '''
    pass


def get_strain_from_discard():
    '''
    TODO: implement this
    '''
    pass


def game_initiation():
    '''

    '''
    initial_placing()

    doctors = get_doctors()
    for doc_id, doctor in doctors.items():
        pick_skill(doc_id)

    get_strain_from_deck()


game_initiation()
# move_to('-1','15')
# print(game_map)

# pick_skill('-1')
# print(characters['-1'])

# move('-1')