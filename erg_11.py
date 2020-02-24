
import errno

# Main()

text = input("Please Enter the Text File Name or Path ")

while True :
    try:
        f = open(text, 'r')
        break
    except IOError as e:
        if e.errno == errno.EACCES:
            print("file exists, but isn't readable")
        elif e.errno == errno.ENOENT:
            print("file isn't readable because it isn't there or you have entered wrong name")
        text = input("Please Enter again the correct Text File Name or Path ")

number = input("Please Enter a 6-digit Integer: ")

while len(number) != 6 : 
    number = input("Thats not a 6-digit integer. Please Enter an 6-digit Integer: ")

number = [int(x) for x in str(number)]                  
number.sort()

contents = f.read().splitlines()                        

i = 0
count = 0
while i < len(contents) and count < 4 :                 
    count = 0                                           
    lst = []                                            
    for digit in range(len(number)) :                   
        if count == 4 :                                 
            break                                       
        for char in contents[i] :                        
            if char == str(number[digit]) :
                lst.insert(count , contents[i])         
                count = count + 1
                temp = contents[i]
                temp = temp.replace(char , '' , 1)     
                contents[i] = temp
                break
            if count == 4 :
                break
    i = i + 1

if count == 4 : 
    print("Yparxei diathesimi tetrada kai einai o arithmos " , lst[0])
else :
    print("Den iyparxei diathesimi tetrada")

f.close()