"""Colors"""
color1 = input()
color2 = input()

mixed_colors = {color1, color2}

primary_colors = {"Red", "Yellow", "Blue"}

if mixed_colors.issubset(primary_colors):
    if len(mixed_colors) == 1:
        print(color1)
    elif mixed_colors == {"Red", "Yellow"}:
        print("Orange")
    elif mixed_colors == {"Red", "Blue"}:
        print("Violet")
    elif mixed_colors == {"Yellow", "Blue"}:
        print("Green")
else:
    print("Error")
