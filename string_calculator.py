import re

def number_list(calStr):
    # for empty string
    if calStr == '':
        return []
    
    pattern = ','
    
    num_list = []
    for num in re.split(pattern=pattern , string= calStr):
        num_list.append(int(num))
    
    return num_list


# return sum of elemenets in list 
def sum_list(num_list):
    ans = 0; 
    for number in num_list:
         ans += number
    return ans


def add(calStr):
    num_list = number_list(calStr)
    return sum_list(num_list)
    