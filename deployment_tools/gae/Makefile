install-gcloud-linux:
	sudo apt-get update && sudo apt-get install google-cloud-sdk google-cloud-sdk-app-engine-python
	gcloud init
upgrade-gcloud:
	gcloud components update
setup:
	cat ../../requirements.txt \
	| grep -v gevent \
	| grep -v tornado \
	| grep -v gunicorn \
	| grep -v memcache > requirements.txt
	echo mysqlclient >> requirements.txt
	mkdir -p lib
	# python3 -m pip install -U --no-deps py4web -t lib/
	cp -r ../../py4web lib/
deploy:
	gcloud config set account ${email}
	gcloud config set project ${project}
	gcloud config set app/promote_by_default false
	gcloud config list
	gcloud app deploy --version ${version} app.yaml
deploy-production:
	gcloud config set account ${email}
	gcloud config set project ${project}
	gcloud config set app/promote_by_default true
	gcloud config list
	gcloud app deploy --version ${version} app.yaml
