import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# First Option
who_pay = random.choice(friends)
print(who_pay)

# Second Option
random.shuffle(friends)
who_pay = friends[0]
print(who_pay)

# Third Option
who_pay = random.randint(0, len(friends) - 1)
print(friends[who_pay])

# Fourth Option
who_pay = random.randrange(0, len(friends))
print(friends[who_pay])
