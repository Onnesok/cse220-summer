def flatten(n, a):
    if len(n) == 0:
        return a
    else:
        if type(n[0]) == int:
            a.append(n[0])
            return flatten(n[1:], a)
        elif type(n[0]) == list:
            a = flatten(n[0], a)
            return flatten(n[1:], a)

#given_list = [1, 2,[16,8], [3,4]]
given_list = [1, [2, [3, [4], 5], 6], 7, 8, [9, [[10, 11], 12], 13], 14, [15, [16, [17]]]]
output = flatten(given_list, [])
print(output)
#print(given_list[0], type(given_list), given_list[1:])



