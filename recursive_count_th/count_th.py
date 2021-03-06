'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):   
    if len(word) == 0:
        return 0
    if len(word) == 1:
        return 0
    if word == 'th':
        return 1
    sum = 0
    if word[:2] == 'th':
        sum += 1
    if word[-2:] == 'th':
        sum += 1
    return sum + count_th(word[1:-1])


