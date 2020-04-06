# Deployment to Appengine Standard Python 3.7

## Setting up for deployment

    make setup
    mkdir apps
    cp -r {apps you want} apps/

## Deployment

    make deploy email={email} project={project} version={version}