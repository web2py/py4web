# To deploy code on Google App Engine:

```
cd deployment_tools/gae
make setup
mkdir apps
touch apps/__init__.py
# symlink the apps that you want to deploy to GAE, for example:
ln -s ../../apps/_default apps/_default
```

Then, you can either do:

```
make deploy email={your email} project={your project} version={vesion}
```

or if you have a gcloud configuration already configured, 

```
gcloud app deploy
```
