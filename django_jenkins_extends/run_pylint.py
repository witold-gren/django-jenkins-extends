# -*- coding: utf-8 -*-
import os
from django.conf import settings

from pylint import lint

from django_jenkins.tasks.run_pylint import ParseableTextReporter, \
    Reporter as ReporterJenkins


__author__ = 'witoldgren'


class Reporter(ReporterJenkins):
    # pylint --load-plugins pylint_django,pylint_celery [..other options..]

    def run(self, apps_locations, **options):
        args = []
        plugins_settings = getattr(settings, 'PYLINT_LOAD_PLUGIN', None)
        if plugins_settings is not None:
            args.append('--load-plugins=%s' % ', '.join(plugins_settings))

        output = open(os.path.join(options['output_dir'],'pylint.report'), 'w')

        args.append("--rcfile=%s" % self.get_config_path(options))

        if options['pylint_errors_only']:
            args += ['--errors-only']
        args += apps_locations

        lint.Run(args, reporter=ParseableTextReporter(
            output=output), exit=False)
