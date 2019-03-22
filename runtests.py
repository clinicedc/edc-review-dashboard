#!/usr/bin/env python
import django
import logging
import sys

from django.conf import settings
from django.test.runner import DiscoverRunner
from edc_test_utils import DefaultTestSettings
from os.path import abspath, dirname, join

app_name = 'edc_review_dashboard'
base_dir = dirname(abspath(__file__))

DEFAULT_SETTINGS = DefaultTestSettings(
    calling_file=__file__,
    BASE_DIR=base_dir,
    APP_NAME=app_name,
    ETC_DIR=join(base_dir, app_name, "tests", "etc"),
    EDC_BOOTSTRAP=3,
    INSTALLED_APPS=[
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'django_extensions',
        'django_crypto_fields.apps.AppConfig',
        'django_revision.apps.AppConfig',
        'edc_base.apps.AppConfig',
        'edc_device.apps.AppConfig',
        'edc_dashboard.apps.AppConfig',
        'edc_lab.apps.AppConfig',
        'edc_metadata_rules.apps.AppConfig',
        'edc_protocol.apps.AppConfig',
        'edc_reference.apps.AppConfig',
        'edc_registration.apps.AppConfig',
        'edc_timepoint.apps.AppConfig',
        'edc_model_admin.apps.AppConfig',
        # 'edc_navbar.apps.AppConfig',
        'edc_visit_schedule.apps.AppConfig',
        'edc_review_dashboard.apps.EdcAppointmentAppConfig',
        'edc_review_dashboard.apps.EdcFacilityAppConfig',
        'edc_review_dashboard.apps.EdcMetadataAppConfig',
        'edc_review_dashboard.apps.EdcVisitTrackingAppConfig',
        'edc_review_dashboard.apps.AppConfig',
    ],
    DASHBOARD_URL_NAMES={
        "subject_review_listboard_url": "dashboard_app:subject_review_listboard_url",
    },
    DASHBOARD_BASE_TEMPLATES={
        "subject_review_listboard_template": "edc_review_dashboard/subject_review_listboard.html",
    },
    add_dashboard_middleware=True,
    use_test_urls=True,
).settings


def main():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)
    django.setup()
    tags = [t.split('=')[1] for t in sys.argv if t.startswith('--tag')]
    failures = DiscoverRunner(
        failfast=True, tags=tags).run_tests([f'{app_name}.tests'])
    sys.exit(failures)


if __name__ == "__main__":
    logging.basicConfig()
    main()
