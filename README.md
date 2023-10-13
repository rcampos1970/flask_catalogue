# README

## Flask Catalogue Uploader

This Python code is a simple Flask application that allows users to submit product information, such as name, description, and price, which is then stored in an Excel file ("Cathalogue.xlsx"). 

### Prerequisites
1. Python
2. Flask
3. openpyxl

### Usage
1. Ensure that you have the necessary libraries installed (Flask and openpyxl).
   - You can install Flask using: `pip install Flask`
   - You can install openpyxl using: `pip install openpyxl`

2. Place the "Cathalogue.xlsx" Excel file in the same directory as the script.

3. Run the script using a Python interpreter.

4. Access the application in your web browser at `http://127.0.0.1:5000`.

5. Fill out the product information form fields (name, description, and price).

6. Click the "Submit" button to add the product information to the Excel file.

7. The product details will be appended to the Excel file, and a new row will be created for each submission.

### Important Notes
- The Excel file structure is expected to have product information in columns A, B, and C.
- The code increments the row number for each submission to ensure each entry is added to a new row in the Excel file.
- The Flask application serves a basic HTML form on the root path ("/") for user input.
- Make sure to replace "Cathalogue.xlsx" with the actual path to your Excel file if it's in a different location.

Feel free to customize the code and the HTML template ("index.html") to better suit your needs.
