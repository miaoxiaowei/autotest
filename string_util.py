"""
找出str1中，str2出现的次数
"""
def find_str(str1, str2):
    if not str1 or not str2:
        return 0
    count = 0
    for i in range(len(str1)):
        if str1[i:i + len(str2)] == str2:
            count += 1
    return count
