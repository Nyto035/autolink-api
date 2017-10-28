#!/usr/bin/env bash

cd {{install_dir}}
source {{venv_dir}}/bin/activate
source {{install_dir}}/env.sh

workers=$(expr $(nproc) + 1)

exec gunicorn --workers $workers --bind 127.0.0.1:{{integration_services_port}} integration_services.config.wsgi  --access-logfile {{log_dir}}/gunicorn.access.log --error-logfile {{log_dir}}/gunicorn.error.log --log-level info --timeout {{gunicorn_timeout}} --graceful-timeout {{gunicorn_graceful_timeout}}
