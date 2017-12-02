run:
	docker run -it --rm -v ${CURDIR}/demo:/app -w /app -p 3000:3000 rails ./bin/rails s -b 0.0.0.0
build:
	docker build -t rails .
