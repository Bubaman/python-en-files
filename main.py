#print(dir(name))
#print('Hello ' + input('Enter your name: ') + '!')

def greeting(greet):
    return lambda name: f'{greet}, {name}' 

mor_greet = greeting('Good morning')

ev_greet = greeting('Good evening')

print(mor_greet('Andrey'))

print(ev_greet('Andrey'))