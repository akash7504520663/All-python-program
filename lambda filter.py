def is_even(n):
    if n%2==0:
        return True
    else:
        return False
print(list(filter(is_even,[122,3232,3445,3243])))




print(list(filter(lambda n:n%2==0,[122,3232,3445,3243])))
