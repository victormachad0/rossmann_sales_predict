import os
from dotenv import find_dotenv, load_dotenv

path_to_dotenv_file = os.path.abspath("utils/.env")

load_dotenv(path_to_dotenv_file)

TOKEN = os.getenv("TOKEN")

print("Path: ", path_to_dotenv_file)
