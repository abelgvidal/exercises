build:
	docker build . -t checkout

test:
	docker run --rm -v $(CURDIR):/app -w /app checkout mamba /app --enable-coverage

coverage:
	docker run --rm -v $(CURDIR):/app -w /app checkout coverage report -m
