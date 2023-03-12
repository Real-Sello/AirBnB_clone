#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models import base_model


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of a class, saves it to the JSON file,
        and prints the id
        """
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        instance = HBNBCommand.classes[class_name]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id
        """
        args = arg.split()

        if not arg:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(class_name, args[1])

        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id, and saves the
        change into the JSON file
        """
        args = arg.split()

        if not arg:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(class_name, args[1])

        if key not in storage.all():
            print("** no instance found **")
            return

        storage.all().pop(key)
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on
        the class name
        """
        args = arg.split()
        objs = []

        if not arg:
            for obj in storage.all().values():
                objs.append(str(obj))
            print(objs)
            return

        class_name = args[0]

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        for obj in storage.all().values():
            if obj.__class__.__name__ == class_name:
                objs.append(str(obj))

        print(objs)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)
        """
        comm = line.split()
        if not line:
            print("** class name missing **")
        elif comm[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(comm) == 1:
            print("** instance id missing **")
            return
        elif comm[0] + "." + comm[1] not in storage.all().keys():
            print("** no instance found **")
            return
        elif len(comm) == 2:
            print("** attribute name missing **")
            return
        elif len(comm) == 3:
            print("** value missing **")
            return
        else:
            object = storage.all()
            key = comm[0] + "." + comm[1]
            if key in object:
                if comm[2] not in self.attributes:
                    if comm[3][0] in self.specs and comm[3][-1] in self.specs:
                        setattr(object[key], comm[2], str(comm[3][1: -1]))
                    else:
                        setattr(object[key], comm[2], str(comm[3]))
                    storage.save()
            else:
                print("** no instance found **")
                return

    def do_count(self, line):
        """
        retrieve the number of instances of a class
        usage: <class name>.count()
        """
        count = 0
        objects = storage.all()
        if line in self.classes:
            for key in objects.keys():
                search_class = key.split(".")
                if search_class[0] == line:
                    count += 1
            print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
