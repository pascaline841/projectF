<h1 align="center">FinX Project</h1>
<br>
<br>

## OVERVIEW
Beta version of a simple metrics extraction system and a Restful API endpoint where we can check and filter the requested metrics.


## REQUISITORIES
Python 3 <br>
Django <br>

## INSTALLATION
Start by closing the repository :
```
git clone https://github.com/pascaline841/projectF
```
Start access the project folder

## for Window
Create a virtual environment
```
python -m venv env
```
Enable the virtual environment
```
cd env/scripts
source activate
```

## for Linux or macOS
Create a virtual environment 
```
python3 -m venv env
```
Activate the virtual environment with 
```
source env/bin/activate 
```
## . . . 
Install the python dependencies to the virtual environment
```
pip install -r requirements.txt
```

## EXECUTION
Run the program
```
python manage.py runserver
```
Launch :

http://127.0.0.1:8000

To access to the admin account : login : admin / password: Finx2022

http://127.0.0.1:8000/admin 

## DATABASE
By default the new entry will be write and stock in the default database. To change it go to setting.py and put the database you want first in DATABASE_ROUTERS = [] <br>
Example to test the program : <br>
john doe john.doe@test.com <br>
jane doe jane.doe@test.com <br>
double test double@test.com
## Test the program
```
python manage.py test
```
## Explications
Un programme qui fonctionne de façon asychrone, c'est un programme qui évite au maximum de passer du temps à attendre sans rien faire et qui va optimiser ce temps d'attente autant que possible.
Dans notre cas les recherches vont se faire simultanément sur les 2 bases de données.
Dans ce programme il y a peu de données donc la réponse est rapide mais il faut imaginer avec 
de trés grosses bases données ou il sera interessant d'avoir les recherches faites en meme temps 
plutot qu'une aprés l'autre.
Asyncio est une bibliothèque permettant de faire de la programmation asynchrone en utilisant la syntaxe async/await.