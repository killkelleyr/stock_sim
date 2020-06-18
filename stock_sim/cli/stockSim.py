import os
import textwrap
os.system('mode con: cols=100 lines=40')
class cli():
    def __init__(self):
        self.clearScreen()
        
    def printLogo(self):
        '''
        When called, this method outputs the logo surrounded in a border
        '''
        logo = '''|                                                                                                  |
|                          _____ _             _     _____ _____ __  __                            |
|                         / ____| |           | |   / ____|_   _|  \/  |                           |
|                        | (___ | |_ ___   ___| | _| (___   | | | \  / |                           |
|                         \___ \| __/ _ \ / __| |/ /\___ \  | | | |\/| |                           |
|                         ____) | || (_) | (__|   < ____) |_| |_| |  | |                           |
|                        |_____/ \__\___/ \___|_|\_\_____/|_____|_|  |_|                           |
|                                                                                                  |'''
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
        '''
        When called, this method creates the header/footer to break up a section
        '''
        print("----------------------------------------------------------------------------------------------------")
        
    def printOptions(self, options):
        """
        When this method is called and supplied with a dictionary of options,
            the available options will be displayed and it will prompt the user
            to -- "Please Enter an option:"
            
        Arguments:
            options(dict) - dictionary where key is the option id and the value
                is the text that will be shown
        
        Returns:
            chosenOption - after a user successfully choses an option, this 
                method will return the chosen id
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
            
    def printInput(self, message):
        '''
        When called, this method allows a user to input text for use in a 
            custom place
            
        Arguments:
            message(string) - string used for prompting the user what to do next
        
        Returns:
            string of what the user entered in this step
        '''
        return(input(textwrap.fill(message, width = 62) + " "))
    
    def printLine(self, message):
        '''
        When called, this method allows to print messages to the screen and 
            should be used to display information to the user.
            
        Arguments:
            message(string) - string used for displaying text to the user
        
        Returns:
            None - prints to screen only
        '''
        print(textwrap.fill(message, width = 62))

class normalWorkflow():
    def __init__(self):
        self.display = cli()
        self.workflow()
    
    def workflow(self):
        options={'1':'Test Option number 1',
                 '2': 'Test Option number 2 where we see how long we can run this sentence on for'}

        
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