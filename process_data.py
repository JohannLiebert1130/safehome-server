from database import Database


class ProcessData(object):
    """docstring for ProcessData."""

    def __init__(self, arg):
        super(ProcessData, self).__init__()
        self.arg = arg

    @staticmethod
    def process(data):
        Database.initialize()
        first_colon = data.find(':')
        index = data[:first_colon]
        if index == '0':
            # register a user
            second_colon = data.find(':', first_colon + 1)
            account = data[first_colon + 1:second_colon]
            password = data[second_colon + 1:]
            print("account: ",account,"password: ",password)
            return ProcessData.register(account, password)
        elif index == '1':
            # user login
            second_colon = data.find(':', first_colon + 1)
            account = data[first_colon + 1:second_colon]
            password = data[second_colon + 1:]
            print("account",account,"password",password)
            return ProcessData.login(account, password)
        elif index == '2':
            # change user's password
            second_colon = data.find(':', first_colon + 1)
            account = data[first_colon + 1:second_colon]

            third_colon = data.find(':', second_colon + 1)
            o_pw = data[second_colon + 1:third_colon]
            n_pw = data[third_colon + 1:]
            return ProcessData.change_password(account, o_pw, n_pw)
        elif index == '3':
            pass
        elif index == '4':
            pass
        else:
            print("Invalid data received!")

    @staticmethod
    def register(account, password):
        user_data = Database.find_one("users", {'account': account})
        if user_data is None:
            Database.insert("users",{"account":account,"password":password})
            return "1" # register successfully
        else:
            return "-3" # user already exists

    @staticmethod
    def login(account, password):
        user_data = Database.find_one("users", {'account': account})
        if user_data is None:
            return "-1"  # user not found!
        else:
            if user_data['password'] == password:
                return "1"  # verify successfully
            else:
                return "-2"  # error password

    @staticmethod
    def change_password(account, o_pw, n_pw):
        user_data = Database.find_one("users", {'account': account})
        if user_data is None:
            return "-1"  # user not found!
        else:
            if user_data['password'] == o_pw:
                user_data['password'] = n_pw
                Database.update("users",{'account': account},user_data)
                return "1"  # change password successfully
            else:
                return "-2"  # error password

    @staticmethod
    def query_sensor_info(data):
        pass

    @staticmethod
    def query_camera_info(data):
        pass
