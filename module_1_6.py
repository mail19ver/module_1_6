# Работа со словарями
print('---------------------------Работа со словарями-------------------------------')

my_dict = {'James': 1985, 'Alex': 2004, 'Natali': 1998}
print('Dict:', my_dict)
print('Existing value:', my_dict['Alex'])
print('Not existing value:', my_dict.get('Max'))
my_dict.update({'Stan': 3004,
               'Tom': 2019})
a = my_dict.pop('Natali')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)

#Работа с множествами
print('---------------------------Работа с множествами------------------------------')
my_set ={0.0,2024, 1, 2, 5,  'Фибоначчи', (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144),'Apple', 1, 2, 3}
print('Set:', my_set)
my_set.update(['Google', 2025])
my_set.discard(2)
print('Modified set: ', my_set)