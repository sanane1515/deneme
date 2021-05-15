from functools import reduce
toCollect = list()
question = input("""This program will detect numbers which are equal or over to 15 and collect them.
Which one do you want to execute the progress with?
1. while loop
2. for loop
""")

if question == "1":
    i = 1
    try:
        while i<21:
            number = int(input("Number: "))
            i += 1

            if number >= 15:
                toCollect.append(number)


            if i == 21:
                break
            

        print("There are totally {} numners and they are: {} and their total value: {}".format(len(toCollect),toCollect,reduce(lambda x,y:x+y,toCollect)))
    except ValueError:
        print("Please enter numerical values")

elif question == "2":
    try:
        for j in range(1,21,1):
            number = int(input("Number: "))
            if number >= 15:
                toCollect.append(number)
            if j == 21:
                break
        print("There are totally {} numners and they are: {} and their total value: {}".format(len(toCollect),toCollect,reduce(lambda x,y:x+y,toCollect)))
    except ValueError:
        print("Please enter numerical values")
else:
    print("Please enter 1 or 2")
        
toQuit= input("To quit please enter random value")

