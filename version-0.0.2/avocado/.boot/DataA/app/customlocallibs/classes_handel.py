from lib import file_handel
import error_handel


class user:
    def __init__(self, first_name, last_name, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password

    def delete_user():
        try:
            file_handel.write(1, "user")
            file_handel.write(2, "pass")
        except:
            error_handel.errortype4()

    def modify_user(self, username: str = "def", password: str = "def"):
        username = self.username
        password = self.password
        if username == "def":
            if password == "def":
                pass
            else:
                try:
                    file_handel.write(2, password)
                except:
                    error_handel.errortype4()
        else:
            try:
                file_handel.write(1, username)
            except:
                error_handel.errortype4()


class theme:
    def __init__(self, color1: int = 000, color2: int = 000, color3: int = 000, color4: int = 000, color5: int = 000, color6: int = 000) -> None:
        c1 = self.color1
        c2 = self.color2
        c3 = self.color3
        c4 = self.color4
        c5 = self.color5
        c6 = self.color6

        def delete_new_theme(self):
            pass


class check:
    def is_nummber(number):
        try:
            number = str(number)
            letter = int(number)
            return True
        except:
            return False

    def is_letter(letter):
        try:
            if type(letter) == bool:
                return False
            letter = str(letter)
            if letter.isalpha():
                return True
            else:
                return False
        except:
            return False


class sort:
    def letter_sorter(letters):
        try:
            str(letters)
            letters = list(letters)
            b = sorted(letters)
            return b
        except:
            pass

    def nummber_sorter(numbers):
        try:
            int(numbers)
            numbers = list(numbers)
            sorted_nummbers = numbers.sort()
            return sorted_nummbers
        except:
            pass
