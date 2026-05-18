class User:

    def __init__(self, first_name, last_name, user_name):

        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name

    def describe_user(self):

        return f"User name is {self.first_name} {self.last_name}"

    def greet_user(self):

        return f"Hello {self.first_name} {self.last_name}!" 
    
class Admin(User):

    def __init__(self, first_name, last_name, username):
        
        super().__init__(first_name, last_name, username)
    
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"Administrator ({self.user_name}) privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

site_admin = Admin("Tedore", "Ghlonti", "Tedo_admin")
site_admin.show_privileges()