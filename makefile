dev:
	. .venv/bin/activate
	fastapi dev app

run:
	. .venv/bin/activate
	fastapi run app

image:
	docker build -t matejkubinec/mncd-viz .

venv:
	python3 -m venv .venv
