def draw_area():
    for i in  area:
        print(*i)
    print()

area = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"],]
print("Добро пожаловать в крестики-нолики")
print("----------------------------------")
draw_area()
area[0][0] = "X"
draw_area()