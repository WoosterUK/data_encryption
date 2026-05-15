class FileFinder:
    """
    A class that returns a list of files in a given directory. Optionally, it
    can be extended to filter files by type or other criteria.
    """
    def __init__(self, directory):
        self.directory = directory

    def list_files(self):
        from os import listdir
        from os.path import isfile, join
        file_list = list(filter(
            lambda f: isfile(join(self.directory, f)),
            listdir(self.directory)
        ))
        file_list.sort()
        return file_list
    
    def filter_files_by_extension(self, extension):
        file_list = self.list_files()
        file_list = filter(lambda f: f.endswith(extension), file_list)
        file_list = list(file_list)
        return file_list

class InputFileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r') as file:
            return file.read()

def encrypt_csv_column(file_path, encryption_key):
    import csv
    from lib.encrypt import encrypt_data
    from os.path import splitext, join, dirname

    # Read the CSV file
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    # Encrypt the first column (ignoring the header)
    for i in range(1, len(rows)):
        if rows[i]:  # Check if the row is not empty
            rows[i][0] = encrypt_data(rows[i][0], encryption_key).hex()

    # Save the encrypted data to a new CSV file
    base_name, ext = splitext(file_path)
    new_file_path = join(dirname(file_path), f"{base_name}_encrypted{ext}")
    
    with open(new_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)

    print(f"Encrypted data saved to {new_file_path}")