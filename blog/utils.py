import os
from datetime import datetime

def save_uploaded_file(uploaded_file, upload_path='mediafiles/posts/featured_images/'):
    # Create the directory path using the current date
    current_datetime = datetime.now()
    subfolder = current_datetime.strftime("%Y/%m%d")
    file_path = os.path.join(upload_path, subfolder)

    # Check if the directory exists, and if not, create it
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    # Generate a unique file name based on the current date and time
    unique_filename = current_datetime.strftime("%Y%m%d%H%M%S") + '_' + uploaded_file.name

    # Create the full path for the file
    file_path = os.path.join(file_path, unique_filename)

    with open(file_path, "wb+") as destination:
        for chunk in uploaded_file.chunks():
            destination.write(chunk)

    return file_path