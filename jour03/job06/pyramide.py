str = "abcdefghijklmnopqrstuvwxyz" * 10

incr = 0
while True:
    if len(str) == 0:
        break
    print(str[:incr + 1])
    str = str[incr + 1:]
    incr += 1