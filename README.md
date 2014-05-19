starstoloves vagrant environment
================================

* Vagrant environment for use with stars-to-loves
* Based on https://github.com/tdhooper/vagrant-django-template
* Includes extra dependencies:
** libspotify and pyspotify (http://pyspotify.mopidy.com)
** lfmh (https://bitbucket.org/hauzer/lfm/)

Setup
-----
    
    $ git clone git@github.com:tdhooper/starstoloves.git
    $ vagrant up
    $ vagrant ssh
      (then, within the SSH session:)
    ./manage.py runserver 0.0.0.0:8000

This will make the app accessible on the host machine as http://localhost:8111/ . The codebase is located on the host
machine, exported to the VM as a shared folder; code editing and Git operations will generally be done on the host.