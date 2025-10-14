# Q1 print following patterns

# (a)

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# (b)

#       *
#     * * *
#   * * * * *
# * * * * * * *

for i in range(1, 5):
    for j in range(4 - i):
        print(" ", end="")
    for k in range(i):
        print("* ", end="")
    print()


# (c)

#   *
# * * *
#   *

for i in range(1, 4):
    if (i == 1) or (i == 3):
        print("  *",end="")
    else:
        for j in range(3):
                print("* ", end="")
    print()



# (D)

# * * *
# *   *
# *   *
# * * *

for i in range(4):
  for j in range(3):
    if ((i == 1) or (i == 2)) and (j == 1 ):
      print("  ", end="")
    else:
     print("* ",end="")
  print()

# (E)

# *   *
#   *
# *   *

for i in range(3):
  for j in range(2
                 ):
    if (i == 1) and (j == 0 or j == 2):
      print(" ", end="")
    else:
      print("* ",end="")
  print()