class VariablesClass:
    __username = "mailtesting797@gmail.com"
    __password = "test123test"
    searchText = "toothpaste"
    amazonSignInUrl = "https://www.amazon.com/gp/sign-in.html"

    @classmethod
    def get_username(cls):
        return cls.__username

    @classmethod
    def get_password(cls):
        return cls.__password
