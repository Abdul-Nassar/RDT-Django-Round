#!/bin/bash
 
NAME="GeEMS"                                  # Name of the application
DJANGODIR=/home/RDT/RTD-Django             # Django project directory
NUM_WORKERS=8                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=geems_project.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=geems_project.wsgi                     # WSGI module name
USER=webuser
GROUP=webapps
TIMEOUT=120
THREADS=8

 
# Activate the virtual environment
cd $DJANGODIR
source ../bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
 
 
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ../bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
#  --threads $THREADS \
  --log-level=debug \
  --worker-class="gevent" \
  --worker-connections=10000 \
  --user=$USER --group=$GROUP \
  --timeout=$TIMEOUT \
  --log-file=-
