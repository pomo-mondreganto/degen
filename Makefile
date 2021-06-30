.PHONY: setup
setup:
	python3 -m pip install -r cli/requirements.txt

.PHONY: gen
gen:
	python3 degen.py generate

.PHONY: start
start:
	docker-compose up --build -d

.PHONY: logs
logs:
	docker-compose logs -f

.PHONY: stop
stop:
	docker-compose down -v

.PHONY: all
all: setup gen start

.PHONY: clean
clean:
	rm -rf service/generated.py
	rm -f service/models.py
	rm -f service/requirements.txt
