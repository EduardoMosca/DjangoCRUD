# CRUD in Django

This is a small project with a todolist written in DJango.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install CRUD.

```bash
pip install -r requirements.txt
```

## Usage

### First create the environment

```bash
python -m venv .env
```

### Active the environment

```bash
#For Windows users
./.env/Scripts/activate

#For Linux users
. .env/bin/activate
```

### Run the application

```bash
python manage.py runserver
```

## Application routes

### The application contains the main routes of an application (GET, POST, PUT and DELETE)

```Bash
#GET and POST route access
localhost:8000/app/
```

### JSON formmat to POST route (all items in the body are mandatories)

```Json
{
	"body": {
		"title": "test",
		"activity": "activity",
		"done": false
	}
}
```

```Bash
#GET(by ID), put PUT and DELETE route access
#ID is an integer number
localhost:8000/app/ID
```

```Json
{
	"body": {
		"title": "test",
		"activity": "activity",
		"done": false
	}
}
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
