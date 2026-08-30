# python
**Note-** While creating folder, do not use hyphen`-` in folder name, instead you can use underscore `_` . 
## There are two applications present in this folder
- **python_app :**
It contains some examples in python core.

- **fastapi_app :**
It contains some REST endpoint to show case user management.

## Setup Virtual Environment
Using Python's `venv` module to create a virtual environment is a best practice that helps you manage dependencies and avoid conflicts across projects. It keeps your development environment clean, organized, and easier to maintain.

1. Create the Environment

    Navigate to your project directory and run the creation command based on your operating system.

    **Windows:** 

    ```
    python -m venv .venv
    ```

    **Linux:**
 
    ```
    python3 -m venv .venv
    ```

    **The above command will create a `.venv` folder.**

2. Activate the Environment
    You must activate the environment before installing packages or running your scripts. Run below command to activate the Python's virtual environment.

    **Windows (Command Prompt):** 
    ```
    .venv\Scripts\activate.bat
    ```

    **Windows (PowerShell):**

    ```
    .venv\Scripts\Activate.ps1
    ``` 

    **Linux:**
    ```
    source .venv/bin/activate
    ```

    Your terminal prompt will now display (.venv) at the beginning, confirming it is active.

    **Note:** You need to activate the environment every time when you open the command prompt.

## Install dependencies

Once activated, any package you install via the official Python Package Index will live exclusively inside this Virtual environment.

- Install a package: 
```
pip install <package_name> (e.g., pip install requests)
```

- Install packages from requirements.txt

```
pip install -r requirements.txt
```


- View installed packages: 

```
pip list
```