# fetwebsite

## How to deploy
- Download the source code
```sh
git clone https://github.com/pythonbrad/fetwebsite.git
cd fetwebsite
```
- Create a virtual environment
```sh
python3 -m venv .fet_venv
```
- Install the requirements
```sh
source .fet_venv/bin/activate
pip install -r requirements.txt
```
- Config the environement (create a .env file in function of .env_example)
```sh
echo "django_session=session_key" >> .env
echo "db_name=database" >> .env
echo "db_user=user" >> .env
echo "db_pass=password" >> .env
echo "db_host=127.0.0.1" >> .env
echo "db_port=3306" >> .env
```
- Config the database
```sh
python manage.py makemigrations
python manage.py migrate
```
- Config the static directory (media and static folder)


## NB
The website should be config before usage. We are open in case of problem.