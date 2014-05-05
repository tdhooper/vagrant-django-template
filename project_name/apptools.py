from django.conf.urls import include, url
import os
import glob
import imp

def _has_urls(app):
    try:
        app_info = imp.find_module(app)
        app_module = imp.load_module(app, *app_info)
        imp.find_module('urls', app_module.__path__)
        return True
    except ImportError:
        return False

def get_app_urls():
    apps = [ app for app in [ os.path.basename(f) for f in glob.glob(os.path.dirname(__file__)+"/apps/*") ] if _has_urls(app) ]
    app_urls = [ url(r'^$', include(app + '.urls')) for app in apps ]
    return app_urls

def get_app_static_dirs():
    dirs = [ f for f in glob.glob(os.path.dirname(__file__)+"/apps/*/static") ]
    print dirs
    return dirs