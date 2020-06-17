import os
import textwrap

class cli():
        
    def printLogo(self):
        logo = '''|                                                            |
|       _____ _             _     _____ _____ __  __         |
|      / ____| |           | |   / ____|_   _|  \/  |        |
|     | (___ | |_ ___   ___| | _| (___   | | | \  / |        |
|      \___ \| __/ _ \ / __| |/ /\___ \  | | | |\/| |        |
|      ____) | || (_) | (__|   < ____) |_| |_| |  | |        |
|     |_____/ \__\___/ \___|_|\_\_____/|_____|_|  |_|        |
|                                                            |'''
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
        self.headerFooter()
        for x in options:
            print(textwrap.fill("Option {}: {}".format(x, options[x]) , width=62))
            print()
        self.headerFooter()
        while True:
            chosenOption = input("Please enter an option: ")
            if chosenOption in options.keys():
                return chosenOption
    
    def validateOption():
        """
        Use this to validate an option chosen from the printOptions function.
            Will check than the option chose was a vaild choice
        """
        #TODO: ADD THIS IN
            
    def printInput(self, message):
        return(input(textwrap.fill(message, width = 62) + " "))
    
    def printLine(self, message):
        print(textwrap.fill(message, width = 62))

class normalWorkflow():
    def __init__(self):
        self.display = cli()
        self.workflow()
    
    def workflow(self):
        options={'1':'Test Option number 1',
                 '2': 'Test Option number 2 where we see how long we can run this sentence on for'}
        optionChosen=None
        print(options.keys())
        for x in options.keys():
            print(x)
        
        self.display.printLogo()
        optionChosen = self.display.printOptions(options)
        self.display.clearScreen()
        self.display.printLine("Here is an example of some custom text on our pages. You can also add in custom variables as seen here and display them as you normally would. After using the input method above we received the value -> {}".format(optionChosen))
        self.display.printLine("With that option value received you can create custom functions which can bring you to a new screen")
        self.display.printLine("In addition to utilizing the printOptions method and the printLine method. You can call the printInput method to have a user enter an input to be used later")
        val = self.display.printInput("Here is an example of a custom input option:  ")

def main():
    """
    main function
    """
    normalWorkflow()

if __name__ == "__main__":
    main()