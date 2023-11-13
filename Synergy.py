pets = dict()
endingException = [11, 12, 13, 14]
endingGod = [1]
endingLet = [5, 6, 7, 8, 9]
endingGoda = [2, 3, 4]
print('Сколько животных вы хотите ввести в базу данных?')
amount = int(input())

for i in range(amount):
    print(f'Животное #{i + 1}:')
    nickname = input('Кличка: ')
    typePet = input('Вид питомца: ')
    age = int(input('Возраст: '))
    if age < 0: raise Exception('Неверно указано сколько лет')
    owner = input('Имя хозяина: ')

    pet = {
        'typePet': typePet,
        'age' : age,
        'owner' : owner
        }
    
    pets.update({f'{nickname}' : pet})

for nickname in pets:
    pet = pets[nickname]
    typePet = pet['typePet']
    age = pet['age']
    owner = pet['owner']
    ending = ''
    if age >= 10:
        twoNumber = int(str(age)[-2:])
        if twoNumber in endingException: ending = 'лет'
        elif twoNumber % 10 in endingGod: ending = 'год'
        elif twoNumber % 10 in endingLet: ending = 'лет'
        elif twoNumber % 10 in endingGoda: ending = 'года'
        elif twoNumber % 10 == 0: ending = 'лет'
    elif age < 10 and age > 0:
        if age in endingException: ending = 'лет'
        elif age % 10 in endingGod: ending = 'год'
        elif age % 10 in endingLet: ending = 'лет'
        elif age % 10 in endingGoda: ending = 'года'
    
    print(f'Это желторотый {typePet} по кличке "{nickname}". Возраст питомца: {age} {ending}. Имя владкльца: {owner}')