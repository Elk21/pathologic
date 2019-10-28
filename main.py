CURRENT_TURN = 0

characters = {
    '0': {
        'name' : 'Plague',
        'type' : 'plague',
        'color' : 'black',
        'current_possition' : '-1',
    },

    '-1': {
        'name' : 'Bachelor',
        'type' : 'doctor',
        'color' : 'blue',
        'current_possition' : '-1',
        'quarantine' : True,
        'resources' : {
            'coin' : 1,
            'key' : 0,
            'secret' : 0,
        },
        'skills' : [],
        'skills_in_hand' : [],
        'skills_played' : [],
        'assistants' : ('1', '2', '3'),
        'banned_assistant' : '0', # 0 - no banned assistant
    },

    '1': {
        'name' : 'Junior Vlad',
        'type' : 'assistant',
        'color' : 'blue',
        'current_possition' : '-1',
        'quarantine' : True,
        'serves_to' : '-1', # bachelor
        'banned_by' : '0', # 0 means not banned
        'donor' : False,
        'resource': 'secret',
    },

    '2': {
        'name' : 'Mary',
        'type' : 'assistant',
        'color' : 'blue',
        'current_possition' : '-1',
        'quarantine' : True,
        'serves_to' : '-1', # bachelor
        'donor' : False,
        'resource': 'coin',
    },

    '3': {
        'name' : 'Andrew',
        'type' : 'assistant',
        'color' : 'blue',
        'current_possition' : '-1',
        'quarantine' : True,
        'serves_to' : '-1', # bachelor
        'donor' : False,
        'resource': 'key',
    },
}

skills = {
    '1' : {
        'name' : '',
        'doctor' : '-1',
        'description' : '',
        'type' : 'reaction',
    },

    '2' : {
        'name' : '',
        'doctor' : '-2',
        'description' : '',
        'type' : 'reaction',
    },

    '3' : {
        'name' : '',
        'doctor' : '-3',
        'description' : '',
        'type' : 'reaction',
    },
}

paths = {
    '0' : [1, 2, 3, 4, 5, 6, 7],
    '1' : [11, 2, 0],
    '2' : [1, 3, 0],
    '3' : [2, 4, 11, 0],
    '4' : [3, 5, 11, 12, 0],
    '5' : [4, 12, 0],
    '6' : [7, 13, 0],
    '7' : [6, 13, 0],
    '8' : [13, 14],
    '9' : [10, 14, 15],
    '10' : [9, 11, 15],
    '11' : [1, 3, 4, 10, 12, 15],
    '12' : [4, 5, 11, 13, 15],
    '13' : [6, 7, 8, 12, 14],
    '14' : [8, 9, 13],
    '15' : [9, 10, 11, 12],
}

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


def game_init():
    '''
        Initial placement of characters
        Fills game_map with charactes id
        and puts current_possition to characters
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

    avaliable_places.append('0')
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
    Shows avaliable moves and asks to input place
    then moves character
    '''
    current_possition = characters[character]['current_possition']
    avaliable_moves = paths[current_possition]

    print(f'Avaliable moves: {avaliable_moves}')
    user_input = ''
    while 1:
        user_input = input('Input move: ')

        if user_input in avaliable_moves:
            break
        else:
            print('Cant move here')

    move_to(character, user_input)


def pick_skill(character):
    doctors_skills = [x[0] for x in skills.items() if x[1]['doctor'] == character]
    avaliable_skills = [x for x in doctors_skills if x not in characters[character]['skills_played']]

    print('Pick a skill')
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



class Plague():
    name = 'Plague'
    turn = 0
    color = 'black'
    possition = 0


# game_init()
# move_to('-1','15')
# print(game_map)

pick_skill('-1')