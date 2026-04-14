n = int(input())

# Please write your code here.
def is_magic_number(n):
    num_to_digit = str(n)

    if n % 2 == 0 and (int(num_to_digit[0]) + int(num_to_digit[1])) % 5 == 0:
        return "Yes"
    else:
        return "No"

print(is_magic_number(n))