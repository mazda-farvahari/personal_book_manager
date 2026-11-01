# Personal Book Manager
![Static Badge](https://img.shields.io/badge/python-3.12-blue)

A simple book manager built with python

## Features

- add multiple books
- save books
- load saved books
- admin mode

## Project Structure

```text
personal_book_manager/
│   .env.example
│   .gitignore
│   main.py
│   books.py
│   README.md
│   requirements.txt
│
├───images
│       sc1.png
│       demo.gif
└───
```

## Requirments
- Python
- python-dotenv


## Installaion
Install the requires packages:

```bash
python -m pip install -r requirements.txt
```

## Envoirment setup
create a `.env` as a template

Use `.env.example` as a template

Add your admin password

```env
BOOK_MANAGER_ADMIN_PASSWORD = your_password_here
```

replace `your_passsword_here` with your own admin password

## Run the programm
run the main file
```bash
python main.py
```

## How It Works

1. At the beginning of the program, it asks for the user’s name and then displays a welcome message.

2. Next, it asks the user whether they want to enter admin mode or not. If the user wants to enter, they must enter the password.

3. Then, the program asks the user how many books they want to add and asks them questions about each book based on the number they entered.

4. Finally, after the user has entered all the books, all the books are displayed, and they are saved in a file named `books.json`.

## Trobleshooting

### FileNotFoundError
1. What does this error mean? It means that the program cannot find the required file.
   
2. Why might it happen? The file may not exist, or it may be opened from an incorrect path.

3. What is the first thing we check? First, we check if the file exists. If it does, we check the path used to open it to find out where the problem is.

### JSONDecodeError
1. What does this error mean? It means that Python cannot read the JSON file.
2. Why might it happen? The JSON file may be empty or may not have a correct structure.

3. What is the first thing we check? First, we check if the file is empty. If it is not empty, we check the structure and format of the JSON file.

### ModuleNotFoundError (python-dotenv)
1. What does this error mean? It means that Python cannot find the python-dotenv library.
2. Why might it happen? This library may not be installed in the current Python environment, or the package may not be installed at all.

3. What is the first thing we check? We check whether the python-dotenv library is installed or not.

### Password Not Found in .env File
1. What does this problem mean? The program cannot read or find the password in the `.env` file.

2. Why might it happen? The password may not exist in the .env file, or the password variable may have an incorrect name.
3. What is the first thing we check? We check if the file exists. If it does, we check the name of the password variable.

## Screenshot 
![personal_task_manager_screenshot](images\sc1.png)

## Demo
![personal_task_manager_demo](images\demo.gif)