build:
	docker build . -t checkout

run:
	docker run --rm -v $(CURDIR):/app -w /app/checkout checkout python3 -m checkout

test:
	docker run --rm -v $(CURDIR):/app -w /app/checkout checkout mamba /app/spec --enable-coverage

coverage:
	docker run --rm -v $(CURDIR):/app -w /app/checkout checkout coverage report -m
