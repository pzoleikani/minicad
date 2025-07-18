# Scientific Software Engineering Homework SS2025

## Exercises

### Prerequisites

You can download the starting point for the application from StudIP.

### Exercise 1

To make yourself familiar with the current state of the application, create a UML class diagram of the important classes to reflect the general application design. The diagram should identify the volatile and stable parts (core) of the application. To create UML diagrams you can use online services like draw.io.

### Exercise 2

Your objective is to develop a new dialog feature that enables users to generate rectangles. To achieve this, you must design a new dialog class and a standalone function that creates both the dialog and the actual rectangle. Additionally, you should ensure that this function is registered within the ActionFactory. All changes need be done in ui/dialogs.py.

### Exercise 3

Implement the drawing mechanism of the class Triangle. The drawing method of the already existing shapes will give you a good orientation for the implementation of the drawing method for the new shape type.

### Exercise 4

Currently a user can translate any shape. In addition, the user should also be able to scale any shape. Implement the scaling behavior for all available shape types and the corresponding scaling dialog.

### Exercise 5

The command pattern is a proven way to implement an undo/redo mechanism. Extend the already existing CommandStack class (the invoker) to support the undo/redo mechanism accordingly.

### Final Result

A user of the mini-cad app should be able to create circles, squares, rectangles and triangles. They can translate and scale shapes. Additionally, the user should be able to undo and redo all of the changes.

## Installation & Running

1. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment in your terminal

   **Windows**

   _Powershell_

   ```bash
   .venv\Scripts\Activate.ps1
   ```

   _cmd.exe_

   ```bash
   .venv\Scripts\activate.bat
   ```

   **Linux/macOS**

   ```bash
   source .venv/bin/activate
   ```

3. Install the dependencies

   Install the project dependencies by running the following command in your terminal.

   ```bash
   pip install .
   ```

4. Select virtual environment in VS Code

   If you have the Python extension installed in VS Code, you will be asked automatically if the virtual environment should be used for your workspace once you have created it. Select 'Yes'. If the pop up does not show up automatically, you can select the virtual environment automatically in the bottom right (you have to open a Python file first). For more details, refer to this guide: https://code.visualstudio.com/docs/python/environments#_working-with-python-interpreters

5. Run the application

   ```bash
   python main.py
   ```
