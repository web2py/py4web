# To deploy code on Google App Engine:

## Setup your deployment folder

```
mkdir my-py4web-gae
cp -r /path/to/py4web/deployment_tools/gae/* my-py4web-gae
cd my-py4web-gae
make install-gcloud-linux
make upgrade-gcloud
make setup
# copy the apps that you want to deploy to GAE, for example:
cp -r /path/to/py4web/apps/_default apps/_default
(cp -r /path/to/py4web/apps/myapp apps/myapp)
# you may need to to symlink or copy the service folder (optional)
cp -r /path/to/py4web/apps/.service apps/
```

## Deploy from the deployment folder

```
make deploy email={your email} project={your project} version={vesion}
```

If you have a gcloud configuration already set you can just do

```
gcloud app deploy
```
