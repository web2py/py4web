install-gcloud-linux:
	sudo apt-get update && sudo apt-get install google-cloud-sdk google-cloud-sdk-app-engine-python
	gcloud init
upgrade-gcloud:
	gcloud components update
setup:
	mkdir -p lib
	python3 -m pip install --upgrade py4web -t lib/
deploy:
	gcloud config set app/promote_by_default false
	gcloud config list
	gcloud app deploy app.yaml
