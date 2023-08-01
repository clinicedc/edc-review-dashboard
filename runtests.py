#!/usr/bin/env python
import logging
import sys
from os.path import abspath, dirname, join

import django
from django.conf import settings
from django.test.runner import DiscoverRunner
from edc_constants.constants import IGNORE
from edc_test_utils import DefaultTestSettings

app_name = "edc_review_dashboard"
base_dir = dirname(abspath(__file__))

DEFAULT_SETTINGS = DefaultTestSettings(
    calling_file=__file__,
    BASE_DIR=base_dir,
    APP_NAME=app_name,
    ETC_DIR=join(base_dir, app_name, "tests", "etc"),
    EDC_BOOTSTRAP=3,
    SUBJECT_VISIT_MODEL="edc_visit_tracking.subjectvisit",
    SUBJECT_REQUISITION_MODEL="review_dashboard_app.subjectrequisition",
    EDC_NAVBAR_DEFAULT=app_name,
    EDC_NAVBAR_VERIFY_ON_LOAD=IGNORE,
    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django.contrib.sites",
        "django_extensions",
        "multisite",
        "django_crypto_fields.apps.AppConfig",
        "django_revision.apps.AppConfig",
        "edc_auth.apps.AppConfig",
        "edc_action_item.apps.AppConfig",
        "edc_appointment.apps.AppConfig",
        "edc_consent.apps.AppConfig",
        "edc_crf.apps.AppConfig",
        "edc_dashboard.apps.AppConfig",
        "edc_data_manager.apps.AppConfig",
        "edc_device.apps.AppConfig",
        "edc_export.apps.AppConfig",
        "edc_identifier.apps.AppConfig",
        "edc_lab.apps.AppConfig",
        "edc_list_data.apps.AppConfig",
        "edc_lab_dashboard.apps.AppConfig",
        "edc_locator.apps.AppConfig",
        "edc_model_admin.apps.AppConfig",
        "edc_navbar.apps.AppConfig",
        "edc_notification.apps.AppConfig",
        "edc_prn.apps.AppConfig",
        "edc_protocol.apps.AppConfig",
        "edc_reference.apps.AppConfig",
        "edc_registration.apps.AppConfig",
        "edc_sites.apps.AppConfig",
        "edc_subject_dashboard.apps.AppConfig",
        "edc_timepoint.apps.AppConfig",
        "edc_visit_schedule.apps.AppConfig",
        "edc_visit_tracking.apps.AppConfig",
        "edc_listboard.apps.AppConfig",
        "edc_review_dashboard.apps.AppConfig",
        "review_dashboard_app.apps.EdcFacilityAppConfig",
        "review_dashboard_app.apps.EdcMetadataAppConfig",
        "review_dashboard_app.apps.AppConfig",
    ],
    DASHBOARD_URL_NAMES={},
    DASHBOARD_BASE_TEMPLATES={
        "edc_base_template": "edc_dashboard/base.html",
        "listboard_base_template": "edc_dashboard/base.html",
        "dashboard_base_template": "edc_dashboard/base.html",
        "subject_review_listboard_template": (
            "edc_review_dashboard/subject_review_listboard.html"
        ),
        "subject_dashboard_template": "edc_subject_dashboard/dashboard.html",
    },
    add_dashboard_middleware=True,
    add_lab_dashboard_middleware=True,
    use_test_urls=True,
).settings


def main():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)
    django.setup()
    tags = [t.split("=")[1] for t in sys.argv if t.startswith("--tag")]
    failures = DiscoverRunner(failfast=False, tags=tags).run_tests([f"{app_name}.tests"])
    sys.exit(failures)


if __name__ == "__main__":
    logging.basicConfig()
    main()
