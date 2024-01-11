#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB"""
    prompt = '(hbnb) '
    
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        "Exit the program on EOF (ctrl+D"""
        return True
    
    def emptyline(self):
        """Do nothing when an empty line is enterd"""
        pass

    
if __name__ == '__main__':
        HBNBCommand().cmdloop()
