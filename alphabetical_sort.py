# Program accepts a string of lowercase letters and 
# returns the longest substring of letters 
# which occur in alphabetical order.


def check(a,b):
    lst = [a,b]
    if lst == sorted(lst):
        return True
    else:
        return False

def leng(t):
    if t == '':
        return 0
    else:
        return 1 + leng(t[:-1])

# Program only works with lowercase letters a-z

print('Mash the letters a few times on the keyboard')
s = input()
count = 1
hicount = 0
letters = leng(s)
letsList = []
finalStr = ''

for j in range(letters-1):
    count = 1
    del letsList[:]
    letsList.append(s[j])
    for i in range (j,letters-1):
        if check(s[i], s[i+1]) == True:
            count +=1
            letsList.append(s[i+1])
        else:
            break
    if (count > hicount):
        hicount = count
        finalStr = ''.join(letsList)


print(finalStr)
                    
        
    
