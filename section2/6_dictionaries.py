my_set = {1,3,5}
my_dict = {'name':'Jose', 'age': 90, 'grades': [13,45,66,90]}
another_dict ={1:15, 2:75, 3:150}

lottery_player = {
    'name': 'Rolf',
    'numbers': (13,45,66,23,22)
}
# print(sum(lottery_player['numbers']))

lottery_players = [
    {
        'name': 'Rolf',
        'numbers': (13,45,66,23,22)
    },
    {
        'name': 'Jhon',
        'numbers': (14,56,80,23,22)
    },
]

universities = [
    {
        'name': 'Oxford',
        'location': 'UK'
    },
    {
        'name': 'MIT',
        'location': 'US'
    }
]
# print(universities)

lottery_player['name'] = 'Brian'
# lottery_player['numbers'][0] = 50 #erro, pois 'numbers' é uma tupla, imutável (13,45,66,23,22)

# print(lottery_player)

##

print(lottery_players)