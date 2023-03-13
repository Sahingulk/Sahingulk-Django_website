# django_project
 
To run the project locally
Clone the project
git clone [repo url]

cd DjangoChatRooms

Create a virtual environment
python3 -m venv venv

Activate the virtual environment
for MAC/Linux: source venv/bin/activate
for Windows: venv\Scripts\activate.bat
Install the requirements
pip install -r requirements.txt

Migrate the database
cd app

python manage.py makemigrations

python manage.py migrate

Run the server
python manage.py runserver

Open the browser and go to http://127.0.0.1:8000/ to see the project