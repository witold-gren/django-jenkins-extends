jenkins_django_extends
======================


Replacement for pylint used in django_jenkins. This plugin allows you to use plugin pylint.

Quick start
-----------
1. First install django_jenkins_extends:

	```
	pip install git+git://github.com/witold-gren/django-jenkins-extends
	```

2. Second install pylint plugin:

	```
	pip install pylint-django pylint-celery
	```

3. Add "PYLINT_LOAD_PLUGIN" to your settings like this:

	```
    PYLINT_LOAD_PLUGIN = (
        'pylint_django',
        'pylint_celery'
    )
	```

4. Replace django task jenkins 'django_jenkins.tasks.run_pylint' to 'jenkins_django_extends.run_pylint':

	```
    JENKINS_TASKS = (
    	...
    	# 'django_jenkins.tasks.run_pylint'
    	'django_jenkins_extends.run_pylint'
    	...
    )
	```