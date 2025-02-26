# Pointator 3000

Pointator 3000 is a Python application designed to record and save 2D point data, compute metrics such as delta distances, and export the results as CSV files. The project follows an MVC structure and implements unit tests for key functionalities.

## Features

- **Recording Points:** Add, retrieve, and clear points in 2D space.
- **Saving Data:** Save recorded points in CSV format with the following columns:
    - Frame Number
    - deltaTime
    - x-coordinate
    - y-coordinate
    - Scale
    - Distance Covered (delta distance)
    - deltaX
    - deltaY
- **File Management:** Automatically check for file name conflicts, prompt for overwriting or renaming, and validate disk space before saving.
- **Menu & Shortcuts:** (Planned) Access the save functionality via a File menu with "Save" and "Save as" items and shortcuts (Ctrl+s and Ctrl+Shift+s).

## Project Structure

```
Pointator 3000/
├── controller/
│   └── controller.py            # Controller logic (TODO: Implementation)
├── data/
│   └── (CSV files saved here)
├── models/
│   ├── filerepo.py              # File repository class to handle saving and file management
│   ├── point.py                 # Point class representing 2D points
│   └── testModels.py            # Unit tests for models
└── views/
        └── view.py                  # UI/view layer (TODO: Implementation)
README.md                        # Project documentation
```

## Requirements & Tasks

This project is built to meet the following requirements:

1. **Export Functionality:** Save point data into a CSV file following the specified format.
2. **File Menu:** Provide a File menu with "Save" and "Save as" options.
3. **Shortcuts:** Implement keyboard shortcuts (Ctrl+s and Ctrl+Shift+s) for saving operations.
4. **File Explorer Integration:** The "Save as" option should open a file explorer with the default directory set to `data`.
5. **File Update:** Allow updating an already open CSV file.
6. **Error Handling:** Display informative error messages if saving fails, no data exists, or disk space is insufficient.
7. **File Name Conflicts:** Prompt the user before overwriting an existing file and automatically generate a new name if needed.

For full details, refer to the attached requirements document in `/Cahier des charges/exigences.txt`.

## Installation

1. Clone or download the repository.
2. Install dependencies (if any) using pip:
     ```
     pip install -r requirements.txt
     ```
     (A requirements file may be added in the future as the project evolves.)

## Usage

Run the main application:
```
python Pointator 3000/main.py
```

## Running Tests

Unit tests are available for the models. Execute the tests using:
```
python -m unittest discover -s Pointator\ 3000
```

## Future Work

- Implement the controller and view layers.
- Integrate a graphical user interface (GUI) for easier interaction.
- Enhance error handling and file validation.

Happy coding!
