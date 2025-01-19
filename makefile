.PHONY: dev
dev: activate
	fastapi dev app

.PHONY: run
run:
	. .venv/bin/activate
	fastapi run app

.PHONY: image
docker-image:
	docker build -t matejkubinec/mncd-viz .

.PHONY: docker-run
docker-run: docker-image
	docker run -p 5050:5050 --rm matejkubinec/mncd-viz

.PHONY: activate
activate:
	. .venv/bin/activate

.PHONY: venv
venv:
	python3 -m venv .venv

.PHONY: deps
deps: activate
	pip install -r requirements.txt

