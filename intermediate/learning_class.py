# Learning classes, attributes, objects and object methods in Python.
class User:
    def __init__(self, user_id, username):
        # These parameters(user_id and username) should be provided while creating an object.
        # And provided parameters should be set as an attribute of that created object.
        self.id = user_id
        self.username = username

        # This is a default value
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1

# Create two users.
user_1 = User(username="user_1", user_id="001")
user_2 = User(username="user_2", user_id="002")

# Let user1 follow user2
user_1.follow(user_2)

# Print the follower and following attributes of these users.
print(f"User 1 following: {user_1.following}")
print(f"User 1 follower: {user_1.follower}")
print(f"User 2 following: {user_2.following}")
print(f"User 2 follower: {user_2.follower}")


