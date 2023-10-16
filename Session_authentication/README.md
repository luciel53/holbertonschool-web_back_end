# Project Badge
![Project Progress](https://progress-bar.dev/100/?title=completed)

## User Authentication Service

- **Master:** Emmanuel Turlay, Staff Software Engineer at Cruise
- **Weight:** 1
- Your score will be updated as you progress.

In the industry, you should not implement your own authentication system and use a module or framework that does it for you (like in Python-Flask: Flask-User). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

### Resources

Read or watch:

- Flask documentation
- Requests module
- HTTP status codes

### Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes

### Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5)
- You should use SQLAlchemy 1.3.x
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions should be type annotated
- The flask app should only interact with Auth and never with DB directly.
- Only public methods of Auth and DB should be used outside these classes

### Setup

You will need to install bcrypt:

```bash
pip3 install bcrypt
```

## Tasks

### 0. User Model
**Mandatory**
*Score: 100.00% (Checks completed: 100.00%)*

In this task, you will create a SQLAlchemy model named User for a database table named users (by using the mapping declaration of SQLAlchemy). The model will have the following attributes:

- `id`, the integer primary key
- `email`, a non-nullable string
- `hashed_password`, a non-nullable string
- `session_id`, a nullable string
- `reset_token`, a nullable string

Example code:

```python
#!/usr/bin/env python3
"""
Main file
"""
from user import User

print(User.__tablename__)

for column in User.__table__.columns:
    print("{}: {}".format(column, column.type))

bob@dylan:~$ python3 main.py
users
users.id: INTEGER
users.email: VARCHAR(250)
users.hashed_password: VARCHAR(250)
users.session_id: VARCHAR(250)
users.reset_token: VARCHAR(250)
bob@dylan:~$
```
## Repo:

- GitHub repository: [holbertonschool-web_back_end](https://github.com/luciel53/holbertonschool-web_back_end)
- Directory: [user_authentication_service](https://github.com/luciel53/holbertonschool-web_back_end/tree/main/user_authentication_service)
- File: [user.py](https://github.com/luciel53/holbertonschool-web_back_end/blob/main/user_authentication_service/user.py)


1. Create User

   In this task, you will complete the `DB` class provided in the `db.py` file to implement the `add_user` method.

   ```python
   from db import DB
   from user import User

   my_db = DB()

   user_1 = my_db.add_user("test@test.com", "SuperHashedPwd")
   print(user_1.id)

   user_2 = my_db.add_user("test1@test.com", "SuperHashedPwd1")
   print(user_2.id)
	bob@dylan:~$ python3 main.py
	1
	2
	bob@dylan:~$
	```



