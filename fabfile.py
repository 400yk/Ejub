from __future__ import with_statement
from fabric.api import *
import os

 env.roledefs = {
         'production'    :    ['youngwide@youngwide.webfactional.com'],
         }

 @roles('production')
 def deploy():
     project_dir = '/home/youngwide/webapps/ejub'
             django_dir = project_dir + '/ejub'
                 with prefix('source /home/youngwide/webapps/ejub_site/bin/activate'):
                     with cd(django_dir):
                        run('git fetch')
                        run('git pull origin master')
                        run('pip install -r requirements.txt')
                        run('python manage.py syncdb')
                        run('python manage.py migrate')
                        run('python manage.py collectstatic --noinput')
                    with cd(project_dir):
                        run('./apache2/bin/restart')
