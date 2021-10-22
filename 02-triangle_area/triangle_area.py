base = input("base: ")
height = input("height: ")

base = int(base)
height = int(height)


def get_triangle_area(base, height):
    area = base * height / 2
    
    return area


def get_triangle_type(base, height):
    triangle_type = ''
    
    if base == height:
        triangle_type = 'Equilatero'
    elif base < height:
        triangle_type = 'Isósceles'
    else:
        triangle_type = 'Escaleno'
    
    return triangle_type


print('''
Triangle area: {}
Triangle type: {}
'''.format(get_triangle_area(base, height), get_triangle_type(base, height)))


