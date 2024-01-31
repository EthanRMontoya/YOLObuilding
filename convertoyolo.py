import os

def convert_to_yolo(line):
    # Modify a single line for YOLO format
    return '0 ' + line.split(' ', 1)[1]

def convert_files_in_directory(directory_path='file path'):
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)

            # Read the input file
            with open(file_path, 'r') as input_file:
                lines = input_file.readlines()

            # Modify lines for YOLO format
            modified_lines = [convert_to_yolo(line) for line in lines]

            # Write the modified data back to the same file
            with open(file_path, 'w') as output_file:
                output_file.writelines(modified_lines)

            print(f"Conversion complete. File '{file_path}' has been overwritten with YOLO-formatted data.")

# Perform the conversion for all files in the 'train' directory
convert_files_in_directory()
