# bounce.py
#
# Exercise 1.5
newheight = 100 # initial height
i = 1  # number of times routine run
while i < 11:
    print(i, round(newheight * 3/5,4))
    newheight = newheight * 3/5
    i = i + 1
