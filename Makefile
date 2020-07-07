help:
	@echo "Usage:"
	@echo "    make build-image                             Build the server image."
	@echo "    make venv-instructions                       Run the server image in a docker container."
	@echo "    make all                                     Build and run the image/container."


# Docker wgdash server
build-image:
	docker build -t wgdash .

run-wgdash:
	docker run --name wgdash \
		-v `pwd`/.env:/wgdash/.env \
		-p 5000:5000

all: build-image run-wgdash 
