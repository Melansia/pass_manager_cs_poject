import os


def create_directory(directory_path="./Users/"):
    if not os.path.exists(directory_path):  # Check if the directory doesn't exist
        os.makedirs(directory_path)  # Create the directory