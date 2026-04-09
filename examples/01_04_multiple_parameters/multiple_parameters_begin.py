""" A Functional Breakfast """

def mix_and_cook():
    print('Mixing the ingredients')
    print('Greasing the frying pan')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it!')
    print('Cooking the other side\n')

def make_omelette(ingredient):
    mix_and_cook()
    omelette = f'a {ingredient} omelette'
    return omelette

def make_pancake(ingredient):
    make_omelette(ingredient)
    pancake = f'a delicious {ingredient} pancake'
    return pancake

# make breakfast for two
davide_breakfast = make_omelette('bacon')
osvaldo_breakfast = make_pancake('nutella')
print(f'davide is having {davide_breakfast}\n')
print(f'osvaldo is having {osvaldo_breakfast}\n')