setup:
	mkdir -p lib
	python3 -m pip install -U --no-deps -r gae-requirements.txt -t lib/
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
