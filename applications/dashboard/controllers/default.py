import os

def index():
    apps = filter(lambda p: os.path.isdir(os.path.join('applications',p)), os.listdir('applications'))
    return dict(apps=apps)
