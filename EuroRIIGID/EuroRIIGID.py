import random
listof={"Estonia": "Tallin","Finland": "Helsinki","Russia": "Moscow","England":"London","France":"Paris","Tallinn":"Estonia","Helsinki":"Finland","Moscow":"Russia","London":"England","Paris":"France"}
def check1():
    m = input('Write country or city: ')
    if m in listof.keys():
        output = listof[m]
        print(output)  
def change1():
    wrong1 = input('Write country or city: ')
    del listof[wrong1]
    new_listof_value=input('Change the word: ')
    listof[wrong1] = new_listof_value
    listof[new_listof_value] = wrong1
def change2():
    wrong1 = input('Write country or city: ')
    del listof[wrong2]
    new_listof_value=input('Change the word: ')
    listof[wrong2] = new_listof_value
    listof[new_listof_value] = wrong2
def test():
    count = 0
    testlist=[]
    for element in listof.keys():
        testlist.append(element)
    for i in range(5):
        random_element = random.sample(testlist, 1)[0]
        print(random_element)
        test_write = input('Your answer: ')
        i += 1
        if test_write == listof[random_element]:
            print('Good job')
            count=count+1
        else:
            print('Bad job')
    print('U have been competed test for',count*20,'%.')
while True:
    try:
        a=int(input("1 - Check the county or city\n2 - change the city(if u saw a mistake)\n3 - change the town(if u saw a mistake)\n4 - check yourself(test)\nWHat u want: "))
        if a==1:
            check1()
        elif a==2:
            change1()
        elif a==3:
            change2()
        elif a==4:
            test()
    except:
        print('Mistake, try one more time')
        ValueError
