from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import dojo


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo = dojo.Dojo.get_one({"id": data["dojo_id"]})

    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, created_at, updated_at) VALUES (%(dojo_id)s, %(first_name)s,%(last_name)s,%(age)s, NOW(), NOW());"

        # what does the INSERT query return?
        # it returns the id of the newly created row
        return connectToMySQL("dojos_ninjas").query_db(query, data)


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # results contains a list of dictionaries
        # each dictionary is a row in the table
        results = connectToMySQL("dojos_ninjas").query_db(query)

        # create an empty list to append all instances of collars
        ninjas = []

        # iterate over the DB results and create collars
        for row in results:
            # cls(row) == Dog(row) => User() Pizza() BankAccount() => creating an object / instance of the class
            ninjas.append(cls(row))
            
        return ninjas
