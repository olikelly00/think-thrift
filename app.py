from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("SEED DATA HERE")

# Retrieve all items from seed data


# List them out
