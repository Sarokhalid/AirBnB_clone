#!/usr/bin/python3

"""defined HBNB program console"""

import cmd
import json
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
    """This is function parsing the argument string"""
    curly_b = re.search(r"\{(.*?)\}", arg)
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
        lex = split(arg[:curly_b.span()[0]])
        ret = [i.strip(",") for i in lex]
        ret.append(curly_b.group())
        return ret


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB
    Attribute:
        prompt (str): the command prompt
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "Place",
        "Amenity",
        "Review"
    }

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        ar = arg.split()
        argd = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            ar = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", ar[1])
            if match is not None:
                command = [ar[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argd.keys():
                    call = "{} {}".format(ar[0], command[1])
                    return argd[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

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
        """Usage: create <class>
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
        """Usage: show <class> <id> or <class>.show(<id>)
        display the string representation of a class instance
        of a given id """
        ar = parse(arg)
        obj = storage.all()
        if len(ar) == 0:
            print("** class name missing **")
        elif ar[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(ar) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(ar[0], ar[1]) not in obj:
            print("** no instance found **")
        else:
            print(obj["{}.{}".format(ar[0], ar[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
            Delete a class instance of a given id"""
        ar = parse(arg)
        obj = storage.all()
        if len(ar) == 0:
            print("** class name missing **")
        elif ar[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(ar) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(ar[0], ar[1]) not in obj.keys():
            print("** no instance found **")
        else:
            del obj["{}.{}".format(ar[0], ar[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representation of all instances
        of a given class if no class is specified display
        all instatiated objects"""
        ar = parse(arg)
        if len(ar) > 0 and ar[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for OBJ in storage.all().values():
                if len(ar) > 0 and ar[0] == OBJ.__class__.__name__:
                    objl.append(OBJ.__str__())
                elif len(ar) == 0:
                    objl.append(OBJ.__str__())
            print(objl)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of given class"""
        ar = parse(arg)
        count = 0
        for OBJ in storage.all().values():
            if ar[0] == OBJ.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <atrribute_value>
        or <class>.update(<id>, <attribute_name>, <attribute_value>)
        or <class>.update(<id>, <dictionary>)
        Update a class instanse of a given id by adding or updating
        a given attribute  key/value or dictionary"""
        ar = parse(arg)
        obj = storage.all()
        if len(ar) == 0:
            print("** class name missing **")
            return False
        if ar[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(ar) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(ar[0], ar[1]) not in obj.keys():
            print("** no instance found **")
            return False
        if len(ar) == 2:
            print("** attribute name missing **")
            return False
        OBJ = obj["{}.{}".format(ar[0], ar[1])]
        if len(ar) == 3:
            try:
                type(eval(ar[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(ar) == 4:
            OBJ = obj["{}.{}".format(ar[0], ar[1])]
            if ar[2] in OBJ.__class__.__dict__.keys():
                valtype = type(OBJ.__class__.__dict__[ar[2]])
                OBJ.__dict__[ar[2]] = valtype(ar[3])
            else:
                OBJ.__dict__[ar[2]] = ar[3]
        elif type(eval(ar[2])) == dict:
            OBJ = obj["{}.{}".format(ar[0], ar[1])]
            for key, value in eval(ar[2]).items():
                if (key in OBJ.__class__.__dict__.keys() and
                        type(OBJ.__class__.__dict__[key]) in
                        {str, int, float}):
                    valtype = type(OBJ.__class__.__dict__[key])
                    OBJ.__dict__[key] = valtype(value)
                else:
                    OBJ.__dict__[key] = value
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
