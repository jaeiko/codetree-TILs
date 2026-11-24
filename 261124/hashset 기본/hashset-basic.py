n = int(input())
commands = []
x = []
s = set()

for i in range(n):
    cmd, val = input().split()
    commands.append(cmd)
    x.append(int(val))

    if commands[i] == "add":
        s.add(x[i])
    elif commands[i] == "remove":
        s.remove(x[i])
    elif commands[i] == "find":
        if int(val) in s:
            print("true")
        else:
            print("false")

# Please write your code here.
