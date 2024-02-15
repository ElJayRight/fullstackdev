# Idea
Have a flask api that can call the backend sql database and reterive file contents passed out as plain text.

The api calls should be structured as:
```
/method/language
```

There will be 2 supported http methods:
GET to get data and PUT to add data.

## GET Method
If no language is given it should result to showing all avaliable languages for the method.

For example if `apc` had `c` and `rust` and the user called
```
/apc/
```

The output should be:
```
[
    'c',
    'rust'
]
```

If no method is called it should return each method and the supported languages

## PUT Method

Will check if the entry is in the db and if so will return:
```
already in db
```

Otherwise it will upload the data to the sql server.


# SQL API Calls

is_in_db(method, language= optional) -> [true, false] 

get_data(method, language= optional) -> data

add_record(method, language) -> [true, false]






