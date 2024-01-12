#!/usr/bin/python3

"""defined HBNB console"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import re
from shlex import split

def parse(arg):
    curly_b = re.search(r"\{(.*?)\]", arg)
    brakets = re.search(r"\[(.*?)\]", arg)
    if curly_b is None:
        if brakets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lex = split(arg[:brakets.span()[0]])
            ret = [i.strip(",") for i in lex]
            ret.append(brakets.group())
            return ret
    else:
        lex = split(ar[:curly_b.span()[0]])
        ret = [i.strip(",") for i in lex]
        ret.append(curly_b.group())
        return ret


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB
    Attribute:
        prompt (str): the command prompt
    """
    
    prompt = '(hbnb) '
    __classes = {
        "BaseModel",
        "User",
        "State",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (ctrl+D)"""
        print("")
        return True

    def emptyline(self):
        """Do nothing when an empty line is enterd"""
        pass

    def do_create(self, arg):
        """Usage: creat <class>
                Create a new class instance and print its id
                """
        ar = parse(arg)
        if len(ar) == 0:
            print("** class name missing **")
        elif ar[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(ar[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)"""
        ar = parse(arg)
        obj = storage.all()
        if len(ar)==0:
            print("** class doesn't exist **")
        elif ar[0] not in HBNBCommand.__classes:
            print("** class dosen't exist **")
        elif len(ar) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(ar[0], ar[1]) not in obj:
            print("** no instance found **")
        else:
            print(obj["{}.{}".format(ar[0], ar[1])])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
