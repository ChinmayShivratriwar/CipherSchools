def pattern1():
    rows = 5 #ascii of A
    for i in range(1 ,rows + 1):
        for j in range(1 , rows):

            if j <= (rows - i):
                print(" " , end=' ')
            else:
                print("*",end=" ")
        print()

def pattern2():
    asVL = 65 #ascii of A
    for i in range(5):
        for j in range(i+1):
            alpha = chr(asVL)
            print(alpha , end=" ")
            asVL = asVL + 1

        print()

pattern1()
print()
print()
pattern2()