from dateutil.relativedelta import FR, MO, SA, SU, TH, TU, WE
from django.apps import AppConfig as DjangoAppConfig
from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig
from edc_metadata.apps import AppConfig as BaseEdcMetadataAppConfig


class AppConfig(DjangoAppConfig):
    name = "review_dashboard_app"
    verbose_name = "review_dashboard_app"


class EdcFacilityAppConfig(BaseEdcFacilityAppConfig):
    definitions = {
        "7-day-clinic": dict(
            days=[MO, TU, WE, TH, FR, SA, SU],
            slots=[100, 100, 100, 100, 100, 100, 100],
        ),
        "5-day-clinic": dict(days=[MO, TU, WE, TH, FR], slots=[100, 100, 100, 100, 100]),
    }


class EdcMetadataAppConfig(BaseEdcMetadataAppConfig):
    reason_field = {"review_dashboard_app.subjectvisit": "reason"}
