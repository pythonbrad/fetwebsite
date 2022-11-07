# fetwebsite

## Preview
![Preview](https://repository-images.githubusercontent.com/543677366/2dc949b7-baa9-4e81-a7fb-c29b1c5c589f)

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
- Config the environement (.env file)
```sh
cp .env_example .env
```
- Config the database
```sh
python manage.py makemigrations
python manage.py migrate
```
- Config the static directory (media and static folder)


## NB
The website should be config before usage. We are open in case of problem.
