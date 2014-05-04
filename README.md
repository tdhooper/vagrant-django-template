stars-to-loves-vagrant-environment
==================================

* Vagrant environment for use with stars-to-loves
* Based on https://github.com/tdhooper/vagrant-django-template
* Includes extra dependencies:
** libspotify and pyspotify (from http://pyspotify.mopidy.com/en/latest/installation/)

Setup
-----
Install Django 1.5 on your host machine. (Be sure to explicitly uninstall earlier versions first, or use a virtualenv -
having earlier versions around seems to cause pre-1.4-style settings.py and urls.py files to be generated alongside the
new ones.)

To start a new project, run the following commands:

    django-admin.py startproject --template https://github.com/tdhooper/vagrant-django-template/zipball/stars-to-loves-vagrant-environment --name=Vagrantfile vagrant-environment
    cd vagrant-environment
    vagrant up
    vagrant ssh
      (then, within the SSH session:)
    ./manage.py runserver 0.0.0.0:8000

This will make the app accessible on the host machine as http://localhost:8111/ . The codebase is located on the host
machine, exported to the VM as a shared folder; code editing and Git operations will generally be done on the host.

Using with stars-to-loves
-------------------------
To install the stars-to-loves app:

    cd varant-environment/vagrant-environment/apps/
    git clone git@github.com:tdhooper/stars-to-loves.git starstoloves