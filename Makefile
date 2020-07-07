help:
	@echo "Usage:"
	@echo "    make build-image                             Build the server image."
	@echo "    make venv-instructions                       Run the server image in a docker container."
	@echo "    make all                                     Build and run the image/container."


# Docker WGDash server
build-image:
	docker build -t wgdash .

run-wgdash:
	docker run -v ~/.env:/WGDash/.env -p 5000:5000 wgdash

all: build-image run-wgdash
