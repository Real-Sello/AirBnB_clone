![img](https://i.imgur.com/sftSnOT.png)
# <img src="https://iconape.com/wp-content/png_logo_vector/airbnb-2.png" width=30> 0x00. AirBnB clone - The console
`Group project` `Python` `OOP`
## Project Description
- This is the first part in building our first full web application: the AirBnB clone. This first step is very important because we will use what we build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…
- The first step is to write a command interpreter to manage our AirBnB objects.
- The goal of the project is to deploy on our server a simple copy of the [AirBnB website](https://www.airbnb.com/).
- The AirBnB website allows users to host anything, anywhere, so guests can enjoy everything, everywhere..
---
## The Console
![img](assets/hbnb_step1.png)
A command line interpreter without a visual interface built in `Python programming language` that allows developers to interact and manipulate the website's database directly.
### Starting The Console
- The console should be able to be started in both interactive mode using `./console.py` and non-interactive mode using `echo "command" | ./console.py`(where 'command' is command passed by user)
  ### *Example:*
    - *Executing in Interactive Mode*:
    ```bash
    $ ./console.py
    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit

    (hbnb)
    (hbnb)
    (hbnb) quit
    $
    ```
    - *Executing in Non-Interactive Mode*:
    ```bash
    $ echo "help" | ./console.py
    (hbnb)

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    (hbnb)
    $
    $ cat test_help
    help
    $
    $ cat test_help | ./console.py
    (hbnb)

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    (hbnb)
    $
    ```
- All tests should also pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`
## Authors
- [@Real-Sello](https://github.com/Real-Sello) | ALX | Cohort 10
___

## Copyright

Sello Prince Moneatse &copy; 2023 | All Rights Reserved
