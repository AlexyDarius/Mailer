import os

def generate_arbo(directory_path):
    # Define the base directory path
    base_directory = 'mailer'

    # Create the base directory
    base_directory_path = os.path.join(directory_path, base_directory)
    os.makedirs(base_directory_path)

    print(f"Directory structure created at: {base_directory_path}")
