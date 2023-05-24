# Project and Tasks on Personal Data Management Concepts: 

- ## Examples of Personally Identifiable Information (PII)
- ## How to implement a log filter that will obfuscate PII fields
- ## How to encrypt a password and check the validity of an input password
- ## How to authenticate to a database using environment variables

## Tasks:

### [0. Regex-ing](./filtered_logger.py)
Write a function called `filter_datum` that returns the log message obfuscated:
* Arguments: 
    * `fields`: a list of strings representing all fields to obfuscate
    * `redaction`: a string representing by what the field will be obfuscated
    * `message`: a string representing the log line
    * `separator`: a string representing by which character is separating all fields in the log line (`message`)
* The function should use a regex to replace occurrences of certain field values.
* `filter_datum` should be less than 5 lines long and use `re.sub` to perform the substitution with a single regex
```
bob@dylan:~$
bob@dylan:~$ ./main.py
name=egg;email=eggmin@eggsample.com;password=xxx;date_of_birth=xxx;
name=bob;email=bob@dylan.com;password=xxx;date_of_birth=xxx;
bob@dylan:~$
```

### [1. Log formatter](./filtered_logger.py)
Copy the following code into `filtered_logger.py`.
```
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError
```
Update the class to accept a list of strings `fields` constructor argument.

Implement the `format` method to filter values in incoming log records using `filter_datum`. Values for fields in `fields` should be filtered.

DO NOT extrapolate `FORMAT` manually. The `format` method should be less than 5 lines long.
```
bob@dylan:~$
bob@dylan:~$ ./main.py
[HOLBERTON] my_logger INFO 2019-11-19 18:24:25,105: name=Bob; email=***; ssn=***; password=***;
bob@dylan:~$
```

### [2. Create logger](./filtered_logger.py)
Use [user_data.csv](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2019/11/a2e00974ce6b41460425.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230524%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230524T180416Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=18986baf70daa4d1c9d0b9af73bc89a60491b0ec9a43efe3d8054e79c408e2fe) for this task

Implement a `get_logger` function that takes no arguments and returns a `logging.Logger` object.

The logger should be named `user_data` and only log up to `logging.INFO` level. It should not propagate messages to other loggers. It should have a `StreamHandler` with `RedactingFormatter` as formatter.

Create a tuple `PII_FIELDS` constant at the root of the module containing the fields from `user_data.csv` that are considered PII. `PII_FIELDS` can contain only 5 fields - choose the right list of fields that can be considered as "important" PII data or information that must be hidden in logs. Use it to parameterize the formatter.

**Tips:**
* `[What Is PII, non-PII, and personal data?](https://piwik.pro/blog/what-is-pii-personal-data/)`
* `[Uncovering Password Habits](https://www.digitalguardian.com/blog/uncovering-password-habits-are-users-password-security-habits-improving-infographic)`

```
bob@dylan:~$
bob@dylan:~$ ./main.py
<class 'logging.Logger'>
PII_FIELDS: 5
bob@dylan:~$
```

### [3. Connect to secure database](./filtered_logger.py)
Database credentials should NEVER be stored in code or checked into version control. One secure option is to store them as environment variable.

Implement the `get_db` function that returns a connector to a database(`mysql.connector.connection.MySQLConnection` object).

- Use the `os` module to obtain credentials from the environment:
- Use the module `mysql-connector-python` to connect to the MySQL database (`pip3 install mysql-connector-python`)
```
bob@dylan:~$ 
bob@dylan:~$ cat main.sql | mysql -uroot -p
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT COUNT(*) FROM users;" | mysql -uroot -p my_db
Enter password: 
2
bob@dylan:~$ 
```

```
bob@dylan:~$
bob@dylan:~$ PERSONAL_DATA_DB_USERNAME=root PERSONAL_DATA_DB_PASSWORD=root PERSONAL_DATA_DB_HOST=localhost PERSONAL_DATA_DB_NAME=my_db ./main.py
2
bob@dylan:~$
```

### [4. Read and filter data](./filtered_logger.py)
Implement a `main` function that takes no arguments and returns nothing.
The function will obtain a database connection using `get_db` and retrieve all rows in the `users` table and display each row under a filtered format:
```
[HOLBERTON] user_data INFO 2019-11-19 18:37:59,596: name=***; email=***; phone=***; ssn=***; password=***; ip=e848:e856:4e0b:a056:54ad:1e98:8110:ce1b; last_login=2019-11-14T06:16:24; user_agent=Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN);
```
Filtered fields:
* `name`
* `email`
* `phone`
* `ssn`
* `password`
only your `main` function should run when the module is executed.
```
bob@dylan:~$ 
bob@dylan:~$ cat main.sql | mysql -uroot -p
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT COUNT(*) FROM users;" | mysql -uroot -p my_db
Enter password: 
2
bob@dylan:~$ 
```

```
bob@dylan:~$ 
bob@dylan:~$ cat main.sql | mysql -uroot -p
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT COUNT(*) FROM users;" | mysql -uroot -p my_db
Enter password: 
2
bob@dylan:~$ 
```