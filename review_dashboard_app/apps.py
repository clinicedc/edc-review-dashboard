from dateutil.relativedelta import FR, MO, SA, SU, TH, TU, WE
from django.apps import AppConfig as DjangoAppConfig
from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig
from edc_metadata.apps import AppConfig as BaseEdcMetadataAppConfig
from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig


class AppConfig(DjangoAppConfig):
    name = "review_dashboard_app"
    verbose_name = "review_dashboard_app"


class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
    visit_models = {
        "review_dashboard_app": ("subject_visit", "review_dashboard_app.subjectvisit")
    }


class EdcFacilityAppConfig(BaseEdcFacilityAppConfig):
    definitions = {
        "7-day-clinic": dict(
            days=[MO, TU, WE, TH, FR, SA, SU],
            slots=[100, 100, 100, 100, 100, 100, 100],
        ),
        "5-day-clinic": dict(days=[MO, TU, WE, TH, FR], slots=[100, 100, 100, 100, 100]),
    }


class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
    pass


class EdcMetadataAppConfig(BaseEdcMetadataAppConfig):
    reason_field = {"review_dashboard_app.subjectvisit": "reason"}
