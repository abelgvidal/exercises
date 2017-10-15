build:
	docker build . -t checkout

test:
	docker run --rm -v $(CURDIR):/app -w /app/checkout checkout mamba /app/spec --enable-coverage

coverage:
	docker run --rm -v $(CURDIR):/app -w /app/checkout checkout coverage report -m
