from lib.database_connection import DatabaseConnection


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("SEED DATA HERE")

