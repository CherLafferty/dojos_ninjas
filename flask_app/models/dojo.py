# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import ninja

# model the class after the dojo table from database
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    # Now we use class methods to query our database
    # @property
    # def full_name(self):
    #     return f"{self.first_name} {self.last_name}"

        # CREATE
    @classmethod
    def create(cls, data):
        # Data holds the individual dojo data to add a dojo to the DB
        # data is a dictionary
        # %(key_in_dict)s

        query = """
            INSERT INTO dojos (name, created_at, updated_at) 
            VALUES (%(name)s, NOW(), NOW());
        """
        result = connectToMySQL("dojos_ninjas").query_db(query, data)
        return result


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_ninjas').query_db(query)
        # Create an empty list to append our instances of users
        dojos = []
        # Iterate over the db results and create instances of users with cls.
        for d in results:
            dojos.append( cls(d) )
        return dojos
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( name, created_at, updated_at ) VALUES ( %(name)s, NOW(), NOW());"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_ninjas').query_db( query, data )

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL('dojos_ninjas').query_db(query,data)
        #result is a list thus []
        return cls(result[0])

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"

        results = connectToMySQL("dogs_schema").query_db(query, data)

        this_dog = cls(results[0])

        print(results)
        if results[0]["ninjas.id"] != None:
            for row_data in results:
                ninja_data = {
                    "id": row_data["ninjas.id"],
                    "first_name": row_data["first_name"],
                    "last_name" : row_data["last_name"],
                    "age": row_data["age"],
                    "created_at": row_data["ninjas.created_at"],
                    "updated_at": row_data["ninjas.updated_at"]
                }
                this_dojo.ninjas.append(ninja.Ninja(ninja_data))

        return this_dojo


    @classmethod
    def update(cls,data):
        query = "UPDATE dojos SET name=%(name)s,updated_at=NOW() WHERE id =%(id)s;"
        return connectToMySQL('dojos_ninjas').query_db( query, data )

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM dojos WHERE id =%(id)s;"
        return connectToMySQL('dojos_ninjas').query_db( query, data )