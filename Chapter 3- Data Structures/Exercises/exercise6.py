# Invite some people to dinner.
guests = ['stefan', 'tyler', 'milo']

name = guests[0].title()
print(name + ",  come to dinner.")

name = guests[1].title()
print(name + ",  come to dinner.")

name = guests[2].title()
print(name + ",  come to dinner.")

name = guests[1].title()
print("\nSorry, " + name + " can not make it to dinner.")

# tyler can't make it! Let's invite paul instead.
del(guests[1])
guests.insert(1, 'paul')

# Print the invitations again.
name = guests[0].title()
print("\n" + name + ", come to dinner.")

name = guests[1].title()
print(name + ",  come to dinner.")

name = guests[2].title()
print(name + ",  come to dinner.")

# We ordered bigger table, going to add some more people to the list.
print("\nWe got a bigger table!")
guests.insert(0, 'anka')
guests.insert(2, 'rufus')
guests.append('bass')

name = guests[0].title()
print(name + ",  come to dinner.")

name = guests[1].title()
print(name + ",  come to dinner.")

name = guests[2].title()
print(name + ",  come to dinner.")

name = guests[3].title()
print(name + ",  come to dinner.")

name = guests[4].title()
print(name + ",  come to dinner.")

name = guests[5].title()
print(name + ",  come to dinner.")

# Oh no, the table won't arrive on time!
print("\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print("Sorry, " + name.title() + " the table is full.")

name = guests.pop()
print("Sorry, " + name.title() + " the table is full.")

name = guests.pop()
print("Sorry, " + name.title() + " the table is full.")

name = guests.pop()
print("Sorry, " + name.title() + " the table is full.")

# There should be two people left. Let's invite them.
name = guests[0].title()
print(name + ",come to dinner.")

name = guests[1].title()
print(name + ",come to dinner.")

# Empty out the list.
del(guests[0])
del(guests[0])

# Prove the list is empty.
print(guests)