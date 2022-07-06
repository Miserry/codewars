def likes(names):

    text_to_return = ''

    if len(names) > 3:
        text_to_return = f'{names[0]}, {names[1]} and {len(names) - 2} others like this'

    elif len(names) == 3:
        text_to_return = f'{names[0]}, {names[1]} and {names[2]} like this'

    elif len(names) == 2:
        text_to_return = f'{names[0]} and {names[1]} like this'

    elif len(names) == 1:
        text_to_return = f'{names[0]} likes this'

    else:
        text_to_return = f'no one likes this'

    return text_to_return