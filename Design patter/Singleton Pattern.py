# Singleton Pattern

class DatabaseConnection():
    _instance = None

    def __new__(cls):
        if cls._instance is None:  # Check if an instance already exists
            cls._instance = super().__new__(cls)
            print("Connecting to Database!")
        return cls._instance


db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1 is db2)

# Output -
'''Connecting to Database!
True'''