s = input()
num_list = list(map(int, s.replace('-', '+').split('+')))
plus_minus = [letter for letter in s if not letter.isdecimal()]

try:
    n = plus_minus.index('-')
    total = sum(num_list[:n+1]) - sum(num_list[n+1:])
    print(total)

except:
    print(sum(num_list))