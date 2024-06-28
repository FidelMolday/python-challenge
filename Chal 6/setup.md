    Navigate to or create a directory where you want to create your project (e.g., cd Documents/MyProject).

    Run the following command to create a virtual environment:

For Windows:

python -m venv venv

For macOS and Linux:

python3 -m venv venv




    Activate the virtual environment:

For Windows:

venv\Scripts\activate

For macOS and Linux:

source venv/bin/activate




    With your virtual environment activated, install the necessary packages using the pip package manager:

pip install streamlit

    Once you have all the required packages, create a "requirements.txt" file that lists them by running this command:

pip freeze > requirements.txt



    Regularly update your virtual environment and installed packages by running:

pip install --upgrade pip
pip install --upgrade -r requirements.txt
