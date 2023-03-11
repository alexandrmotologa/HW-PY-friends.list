MAX_FRIENDS = 100

friends = []

while len(friends) < MAX_FRIENDS:
    name = input("Add friend name: ")
    if not name:
        break
    if len(friends) >= MAX_FRIENDS:
        print("You have reached the maximum number of friends.")
        break
    if name in friends:
        print("This name is already on the list.")
    else:
        friends.append(name)

print("You have", len(friends), "friends")
for i in range(len(friends)):
    print(" ",i,">>", friends[i])