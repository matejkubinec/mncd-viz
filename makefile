.PHONY: dev
dev: activate
	fastapi dev app

.PHONY: run
run:
	. .venv/bin/activate
	fastapi run app

.PHONY: image
image:
	docker build -t matejkubinec/mncd-viz .

.PHONY: activate
activate:
	. .venv/bin/activate

.PHONY: venv
venv:
	python3 -m venv .venv

.PHONY: deps
deps: activate
	pip install -r requirements.txt

