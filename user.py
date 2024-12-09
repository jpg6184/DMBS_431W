__admin_user = 'admin'
__admin_pword = 'password'

class User:
    def __init__(self, username, password, role="guest"):
        """
        username: The username of the user.
        password: The password of the user.
        role: The role of the user (default: "guest").
        """
        self.username = username
        self.password = password
        self.role = role

    def __str__(self):
        return f"User(username = {self.username}, role = {self.role})\n"

    @staticmethod
    def login():
        """
        return: A User object with the appropriate role.
        """
        print("----LOGIN----")
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Hardcoded credentials (replace with secure database authentication for production)
        if username == "admin" and password == "admin123":
            print("Logged in as Admin.\n")
            return User(username, password, role="admin")
        else:
            print("Logged in as Guest.\n")
            return User(username, password, role="guest")

    def is_admin(self):
        """
        Check if the user has admin privileges.

        :return: True if the user is an admin, False otherwise.
        """
        return self.role == "admin"
