install-gcloud-linux:
	sudo apt-get update && sudo apt-get install google-cloud-sdk google-cloud-sdk-app-engine-python
	gcloud init
upgrade-gcloud:
	gcloud components update
setup:
        mkdir -p lib
        pip-compile requirements.in
        python3 -m pip install -U --no-deps -r requirements.txt -t lib/
        rm -rf lib/gevent*
        rm -rf lib/gunicorn*
        rm -rf lib/zope*
        rm requirements.txt
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
