def write_file(file_name, file_content):
    pass
    file_name_with_extension = str(file_name) + '.txt'
    with open(file_name_with_extension, 'w') as file:
        file.write(file_content)
    
write_file(file_name="test_file", file_content="This is a test content." )

def append_file(file_name, append_content):
    pass
    file_path = str(file_name) + '.txt'
    with open(file_path, 'a') as file:
        file.write(append_content)
append_file(file_name="test_file", append_content="This is a test content.")

def read_file(file_name):
    pass
    file_path = file_name.with_suffix('.txt')
    with open(file_path, 'r') as file:
        file_content = file.read()
    return file_content
