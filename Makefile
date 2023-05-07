bash:
	poetry shell 

serve:
	poetry run python app.py 

lint:
	poetry run black .
	poetry run isort .
	poetry run flake8 .

lint_check:
	poetry run flake8 
	poetry run black . --check 
	poetry run isort . -c 

init_db:
	poetry run python setup.py init_db

create_factories:
	poetry run python setup.py create_factories

test:
	poetry run pytest 
