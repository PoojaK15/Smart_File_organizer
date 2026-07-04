# Smart File Organizer

A lightweight Python automation tool that organizes files into categorized folders based on their file extensions. The application automatically creates the required directories (if they do not already exist) and moves files into the appropriate folders, making file management faster, cleaner, and more efficient.

---

## Overview

Managing folders with mixed file types can quickly become unorganized. Smart File Organizer automates this process by scanning a user-specified directory, identifying files based on their extensions, and placing them into predefined folders.

The project is built entirely using Python's standard libraries, making it simple, portable, and easy to run without installing additional dependencies.

---

## Key Features

* Automatically creates category folders when they are not present.
* Organizes files based on their file extensions.
* Supports multiple image, document, and video formats.
* Performs case-insensitive extension matching.
* Uses only Python's built-in libraries.
* Simple command-line interface.
* Lightweight and easy to maintain.

---

## Technologies Used

* Python 3
* os module
* shutil module

---

## Supported File Types

| Category  | Supported Extensions    |
| --------- | ----------------------- |
| Images    | `.jpg`, `.jpeg`, `.png` |
| Documents | `.pdf`, `.txt`, `.docx` |
| Videos    | `.mp4`, `.mkv`, `.avi`  |

---

## Project Structure

Smart-File-Organizer/
│
├── smart_file_organizer.py
└── README.md


---

## Workflow

User enters folder path
          │
          ▼
Check whether category folders exist
          │
          ▼
Create missing folders
          │
          ▼
Scan all files in the selected directory
          │
          ▼
Identify file extension
          │
          ▼
Move file to the appropriate folder

---

## Usage

After running the script, enter the path of the folder you want to organize.

Example:

```text
Enter folder path:
C:\Users\Pooja\Downloads
```

---

## Sample Output

```text
Created folder: Images
Created folder: Documents
Created folder: Videos

Moved photo.jpg -> Images
Moved report.pdf -> Documents
Moved lecture.mp4 -> Videos
```

---

## Future Enhancements

* Support additional file categories such as Audio, Archives, and Executables.
* Allow users to define custom categories and file extensions.
* Develop a graphical user interface (GUI).
* Add automatic folder monitoring.
* Implement duplicate file detection.
* Generate activity logs for organized files.

---

## Author

**Pooja Karakoti**

Python Developer | AI & Automation Enthusiast


