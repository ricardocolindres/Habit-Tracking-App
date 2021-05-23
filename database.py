# Header File: database.py
# Database for Ness.
# History:
# Date    Programmer   - Description
# ---------- ---------- ----------------------------
# 05/04/2021     Ricardo Josue Colindres      - Created

import json


class DataBase:

    #! ******************************** Properties *******************************

    def __init__(self, username):
        self.username = username
        self.user_info = None

    #! ******************************** Methods *******************************

    def load(self):
        self.data_base = json.load(open('data/info/users.json'))
        for i, v in enumerate(self.data_base):
            if self.data_base[i]['username'] == self.username:
                self.user_info = self.data_base[i]
                break
        return self.user_info

    def update(self, new_user_info):
        self.data_base = json.load(open('data/info/users.json'))
        for i, v in enumerate(self.data_base):
            if self.data_base[i]['username'] == self.username:
                self.data_base[i] = new_user_info
                break

        json_userinfo = json.dumps(self.data_base, indent=1)
        with open('data/info/users.json', 'w') as outfile:
            outfile.write(json_userinfo)

        self.user_info = new_user_info


class FullDatabase:

    #! ******************************** Properties *******************************

    def __init__(self):

        self.credential_path = 'data/credentials/credentials.json'
        self.users_info_paths = 'data/info/users.json'
        self.credential_database = None
        self.users_info_database = None

    #! ******************************** Methods *******************************

    def load_credentials(self):

        self.credential_database = json.load(open(self.credential_path))
        return self.credential_database

    def load_users_info(self):

        self.users_info_database = json.load(open(self.users_info_paths))
        return self.users_info_database

    def update_database(self, credentials, users_info):

        json_credentials = json.dumps(credentials, indent=1)
        with open(self.credential_path, 'w') as outfile:
            outfile.write(json_credentials)

        json_userinfo = json.dumps(users_info, indent=1)
        with open(self.users_info_paths, 'w') as outfile:
            outfile.write(json_userinfo)
