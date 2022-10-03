from math import pi
class figure:
    name = ''
    side = 0
    formula = None
square_1 = figure()
square_1.name = 'square_1'
square_1.side = 2
square_1.formula = square_1.side ** 2

square_2 = figure()
square_2.name = 'square_2'
square_2.side = 3
square_2.formula = square_2.side ** 2

square_3 = figure()
square_3.name = 'square_3'
square_3.side = 4
square_3.formula = square_3.side ** 2

square_4 = figure()
square_4.name = 'square_4'
square_4.side = 5
square_4.formula = square_4.side ** 2

circle_1 = figure()
circle_1.name = 'circle_1'
circle_1.side = 1
circle_1.formula = (circle_1.side ** 2) * pi

circle_2 = figure()
circle_2.name = 'circle_2'
circle_2.side = 2
circle_2.formula = (circle_2.side ** 2) * pi

circle_3 = figure()
circle_3.name = 'circle_3'
circle_3.side = 3
circle_3.formula = (circle_3.side ** 2) * pi

circle_4 = figure()
circle_4.name = 'circle_4'
circle_4.side = 4
circle_4.formula = (circle_4.side ** 2) * pi

figures = {
    square_1.name : square_1.formula ,
    square_2.name : square_2.formula ,
    square_3.name : square_3.formula ,
    square_4.name : square_4.formula ,
    circle_1.name : circle_1.formula ,
    circle_2.name : circle_2.formula ,
    circle_3.name : circle_3.formula ,
    circle_4.name : circle_4.formula
}
for list in figures:
    print('{} = {} cm²'.format(list, figures[list]))