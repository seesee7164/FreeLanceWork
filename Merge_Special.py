# This is a special version of mergesort addapted for use in String_Full_Census
# The biggest difference is that it takes in a list containing tuples and
# sorts those from largest to smallest and sorting alphabetically amongst ties

# This function compares two string and returns true if the first one goes
# before the second alphabetically and false otherwise
def SortAlphabetically(string1, string2):
    s1 = string1
    s2 = string2
    while(len(s1) > 0):
        ascii1 = int(ord(s1[0]))
        if ascii1 <= 122 and ascii1 >= 97:
            ascii1 -= 32
        ascii2 = int(ord(s2[0]))
        if ascii2 <= 122 and ascii2 >= 97:
            ascii2 -= 32
        if ascii1 < ascii2:
            return True
        elif ascii1 > ascii2:
            return False
        s1 = s1[1:]
        s2 = s2[1:]
    return True

def mergesplit(List):
    if len(List) > 2:
        mid = len(List)//2
        return mergesort(mergesplit(List[:mid]), mergesplit(List[mid:]))
    elif len(List) == 2:
        if List[0][1] > List[1][1]:
            return List
        elif List[0][1] == List[1][1]:
            if SortAlphabetically(List[0][0],List[1][0]):
                return List
            else:
                return [List[1],List[0]]
        else:
            return [List[1],List[0]]
    else:
        return List

def mergesort(List1, List2):
    ret = []
    while len(List1) > 0 and len(List2) > 0:
        if List1[0][1] > List2[0][1]:
            ret.append(List1[0])
            List1.pop(0)
        elif List1[0][1] == List2[0][1]:
            if SortAlphabetically(List1[0][0],List2[0][0]):
                ret.append(List1[0])
                List1.pop(0)
            else:
                ret.append(List2[0])
                List2.pop(0)
        else:
            ret.append(List2[0])
            List2.pop(0)
    if len(List1) > 0:
        return ret + List1
    else:
        return ret + List2