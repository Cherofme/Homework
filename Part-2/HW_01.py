class Footballclub:
    name = ''
    city = ''
    score = 0


class Chempionship:
    country = ''
    name_of_chemp = ''
    footballclubs = []


chempionshipua = Chempionship
chempionshipua.country = 'Ukraine'
chempionshipua.name_of_chemp = 'Divizia' 

real = Footballclub()
real.name = 'real'
real.city = 'Madrid'
real.score = 74

liverpul = Footballclub()
liverpul.name = 'liverpul'
liverpul.city = 'Liverpul'
liverpul.score = 66

manchester = Footballclub()
manchester.name = 'manchester'
manchester.city = 'Moscow'
manchester.score = 35

shachtar = Footballclub()
shachtar.name = 'shachtar'
shachtar.city = 'Thailand'
shachtar.score = 50



def worstteam():
    worstscore = min(real.score, liverpul.score, manchester.score, shachtar.score)
    if worstscore == real.score:
        return print('У команды {} меньше всего очков: {}'.format(real.name, real.score))
    elif worstscore == liverpul.score:
        return print('У команды {} меньше всего очков: {}'.format(liverpul.name, liverpul.score))
    elif worstscore == manchester.score:
        return print('У команды {} меньше всего очков: {}'.format(manchester.name, manchester.score))
    else:
        return print('У команды {} меньше всего очков: {}'.format(shachtar.name, shachtar.score))

worstteam()