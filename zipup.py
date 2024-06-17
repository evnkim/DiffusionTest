import os
import zipfile

def zip_files(folder_path, extension, ex2, output_zip_file):
    # Create a new ZIP file
    with zipfile.ZipFile(output_zip_file, 'w') as zipf:
        # Walk through the directory
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(extension) or file.endswith(ex2):
                    # Create a complete file path
                    file_path = os.path.join(root, file)
                    # Add file to the ZIP file
                    zipf.write(file_path, os.path.relpath(file_path, folder_path))

# Example usage:
folder_path = '../'  # Change this to your folder's path
extension1 = '.py'  # Change the file extension you want to zip
ex2 = '.ipynb'
output_zip_file = 'EVANKIM.zip'  # Output ZIP file name

zip_files(folder_path, extension1,ex2, output_zip_file)