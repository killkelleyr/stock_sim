import os

class cli():
        
    def printLogo(self):
        logo = '''
|       _____ _             _     _____ _____ __  __         |
|      / ____| |           | |   / ____|_   _|  \/  |        |
|     | (___ | |_ ___   ___| | _| (___   | | | \  / |        |
|      \___ \| __/ _ \ / __| |/ /\___ \  | | | |\/| |        |
|      ____) | || (_) | (__|   < ____) |_| |_| |  | |        |
|     |_____/ \__\___/ \___|_|\_\_____/|_____|_|  |_|        |
        '''
        self.headerFooter()
        print(logo)
        self.headerFooter()
        
    def clearScreen(self):
        """
        """
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')
    
    def headerFooter(self):
        print("--------------------------------------------------------------")
        
    def printOptions(self, options):
        """
        prints whatever options are sent
        """
        print("Please choose Option")
        optionNum = 1
        for x in options:
            print("Option {}: {}".format(optionNum, x))
    
    def validateOption():
        """
        Use this to validate an option chosen from the printOptions function.
            Will check than the option chose was a vaild choice
        """
        #TODO: ADD THIS IN
            
    def printInput(self, message):
        return(input(message))
    
    def printLine(self, message):
        print(message)

class normalWorkflow():
    def __init__(self):
        self.display = cli()
        self.workflow()
    
    def workflow(self):
        options=['Login','Create User']
        optionChosen=None
        while optionChosen != "1" and optionChosen != "2":
            self.display.printLogo()
            self.display.printOptions(options)
            self.display.headerFooter()
            optionChosen=self.display.printInput("Please choose an option: ")
            self.display.clearScreen()
        self.display.printLine("Received {}".format(optionChosen))

def main():
    """
    main function
    """
    normalWorkflow()

if __name__ == "__main__":
    main()