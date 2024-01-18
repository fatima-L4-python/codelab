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

# jess can't make it! Let's invite Max instead.
del(guests[1])
guests.insert(1, 'paul')

# Print the invitations again.
name = guests[0].title()
print("\n" + name + ",  come to dinner.")

name = guests[1].title()
print(name + ",  come to dinner.")

name = guests[2].title()
print(name + ",  come to dinner.")