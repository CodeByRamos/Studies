import random
def count_sheeps():
    ovelhalist = ""
    sheep_yes = 0
    sheep_no = 1
    i = 0
    if i != 10:
        ovelha = random.randint(0,1)
        i+=1
        if ovelha == sheep_yes:
            ovelhalist += True
        elif ovelha == sheep_no:
            ovelhalist += False
    return ovelhalist

printar = print(count_sheeps())
print(printar)
            
        