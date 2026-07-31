user_friends = input("Enter 3 friends names separated by a comma:").split(",")
print(user_friends)

read_people = open("people.txt","r")
get_people = [line.strip() for line in read_people.readlines()]
print(get_people)

read_people.close()

friends_set = set(user_friends)
people_set = set(get_people)

people_nearby = friends_set.intersection(people_set)

nearby_friend = open("nearby_friend.txt","w")
for friend in people_nearby:
    nearby_friend.write(friend)
    print(friend)
    nearby_friend.write("\n")

nearby_friend.close()


