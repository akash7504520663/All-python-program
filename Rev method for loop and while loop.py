def reverses(st):
    n = len(st)
    result = [0] * n
     
    for i in range(n):
        if (st[i] == ' '):
            result[i] = ' '
    j = n - 1
    for i in range(len(st)):
        if (st[i] != ' '):
            if (result[j] == ' '):
                j -= 1
            result[j] = st[i]
            j -= 1
    return ''.join(result)
if __name__ == "__main__":
 
    st = "I am harshad"
    print(reverses(st))
print ("use for loop and while loop method")
def a(Str):
   
    n = len(Str)
    Str = list(Str)
    start = 0
    end = n - 1
    while(start < end):
        if(Str[start] == ' '):
            start += 1
            continue
        elif(Str[end] == ' '):
            end -= 1
            continue
        else:
            Str[start], Str[end] = (Str[end],
                                    Str[start])
            start += 1
            end -= 1
    print(''.join(Str))
Str = "I am Harshad"
a(Str);
 
