import re

# return list of number
def number_list(calStr):
    # for empty string
    if calStr == '':
        return []
    
    pattern = ',|\n'
    
    # for multiple delimiter
    delimiter = ""
    if calStr[0:2] == "//":
        calStr = calStr[2:]
        delimiter, calStr = re.split('\n',calStr, 1)
    
    if delimiter != "":
        pattern +=  ('|' + delimiter)
        
    num_list = []
    for num in re.split(pattern=pattern , string= calStr):
        if len(num) == 0 :
            continue
        elif len(num) <= 1 and ord(num) >= 97 and ord(num) <= 122:
            num_list.append(ord(num) - 96)
        else :
            num_list.append(int(num))
    
    return num_list

# if negative value in num_list then raise error
def check_negatives(num_list):
    negative_num_list = []
    for number in num_list:
        if number < 0:
            negative_num_list.append(number)
    
    if len(negative_num_list) > 0 :
        raise ValueError('Negatives not allowed {}'.format(negative_num_list))            

# remove a number bigger then 1000
def remove_big_number(num_list):
    for number in num_list:
        if number > 1000:
            num_list.remove(number)
    
    return num_list

# return sum of elemenets in list 
def sum_list(num_list,odd_even_in):
    ans = 0; 
    num_len = len(num_list)
    
    if odd_even_in == 0:
        num_list = num_list[1:num_len+1:2]
    elif odd_even_in == 1:
        num_list = num_list[0:num_len+1:2]
        
    for number in num_list:
         ans += number
    return ans

# add function
def add(calStr):
    odd_even_in = None
    if len(calStr) >= 3:
        if calStr[:3] == "0//":
            odd_even_in = 0
        elif calStr[:3] == "1//":
            odd_even_in = 1
    
    if odd_even_in != None:
        calStr = calStr[3:]
    
    num_list = number_list(calStr)
    
    # if negative number in num_list then raise exception
    check_negatives(num_list)
    
    # if number in num_list is larger then 1000 remove it
    updated_num_list = remove_big_number(num_list)
    
    return sum_list(updated_num_list,odd_even_in)
    