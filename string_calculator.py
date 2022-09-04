def number_list(calStr):
    if calStr == '':
        return []


# return sum of elemenets in list 
def sum_list(num_list):
    ans = 0; 
    for number in num_list:
         ans += number
    return ans


def add(calStr):
    num_list = number_list(calStr)
    return sum_list(num_list)
    