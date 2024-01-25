t_room, t_cond = map(int, input().split(" "))
mode = input()

if mode == "freeze":
    print(max(t_room, t_cond))
elif mode == "heat":
    print(min(t_room, t_cond))
elif mode == "auto":
    print(t_cond)
else:
    print(t_room)