# to deploy code on Google App Engine:

```
cd deployment_tools/gae
make setup
mkdir apps
# symlink the apps that you want to deploy to GAE, for example:
ln -s ../../apps/_default apps/_default
make deploy email={your email} project={your project} version={vesion}
```