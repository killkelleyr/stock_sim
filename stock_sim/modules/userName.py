from dbReader import dbReader
from dbWriter import dbWriter

userNames = {}
userNamesDB = {}

class userName():
    def __init__(self, userName = None, permissionLevel = 0, password = None, 
                 createDate = None, recentDate = None):
        self.userName = userName
        self.password = bytes(str(password),encoding='utf-8')
        self.permissionLevel = int(permissionLevel)
        self.startDate = startDate
        self.mostRecentDate = mostRecentDate

    def importFromDB():
        users = dbReader.executeQuery("select * from username")
        for x in users:
            userNamesDB[x[1]] = userName(x[1],x[2],x[3],x[4],x[5])
        return userNamesDB
    
    def passwordHasher(password):
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        hashedPass = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                         salt, 100000)
        hashedPass = binascii.hexlify(hashedPass)
        return (salt + hashedPass).decode('ascii')

    def passwordVerification(storedPassword, providedPassword):
        salt = str(storedPassword[:64],'utf-8')
        storedPassword = str(storedPassword[64:],'utf-8')
        hashedPass = hashlib.pbkdf2_hmac('sha512',providedPassword.encode('utf-8'),salt.encode('ascii'),100000)
        hashedPass = binascii.hexlify(hashedPass).decode('ascii')
        return hashedPass == storedPassword

    def login(permissionsRequired = 0, verbose = False):
        """
        Definition:
            This function is used for authorizing a user. It checkes if a user
            exists and if the user has the propper access level required

        Arguments:
            permissionsRequired -- permission level required to continue program
            verbose -- defaults to False, set true to print user info

        Returns:
            userName -- if access is permitted
            False -- if access is denied
        """
        currentUsers = userName.importFromDB()
        loginAttempts=0
        while True:
            user = input("Please enter user name: ")
            if user in currentUsers.keys():
                user = currentUsers[user]
                if verbose:
                    userName.printUser(user)

                if user.permissionLevel >= permissionsRequired:
                    passwordAttempts = 0
                    if permissionsRequired == 0:
                        return user.userName

                    while passwordAttempts < 3:
                        password = getpass("Please Enter Password: ")
                        if userName.passwordVerification(user.password,password):
                            if verbose:
                                print("Access Granted")
                            dbWriter.updateUserLogin(user.userName)
                            return user.userName
                        else:
                            print("Access Denied")
                            print("Incorrect password")
                            passwordAttempts+=1
                            if passwordAttempts >= 3:
                                print("Too many login attempts")
                                return False
                else:
                    print("Access Denied!")
                    print("Insufficient user access level")
                    return False
            else:
                loginAttempts+=1
                print ("User Does not exist! Please try again")
                if loginAttempts == 3:
                    print("Too Many Login Attemtps")
                    return False

    def createUser(permissionLevel=0):
        """
        This function can be called to create a new user
        """
        currentUsers = userName.importFromDB()

        newUserName = ""
        while True:
            newUserName=""
            print("---- Create a user ----")
            newUserName = input("Please enter your userID: ")
            if newUserName  in currentUsers.keys():
                print("User already exists")
            else:
                print("Created User")
                break
                False

        while True:
            print("New User: {}".format(newUserName))
            print("Passwords must be minimum 6 charachters\n")
            password = getpass("Please enter a password: ")
            if len(password) >= 5:
                confirmation = ""
                while password != confirmation:
                    confirmation = getpass("Please re-enter password for confirmation: ")
                password = userName.passwordHasher(password)
                confirmation=""
                break
                False
            else:
                print("password too short")
                
        print("User {} created".format(newUserName))
        permission=0
        dbWriter.writeUserName(newUserName, permission, password)