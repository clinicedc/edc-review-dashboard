from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings


class AppConfig(DjangoAppConfig):
    name = "edc_review_dashboard"


if settings.APP_NAME == "edc_review_dashboard":

    from dateutil.relativedelta import SU, MO, TU, WE, TH, FR, SA
    from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig
    from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig
    from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
    from edc_metadata.apps import AppConfig as BaseEdcMetadataAppConfig
    from edc_appointment.appointment_config import AppointmentConfig

    class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
        visit_models = {
            "dashboard_app": ("subject_visit", "dashboard_app.subjectvisit")
        }

    class EdcFacilityAppConfig(BaseEdcFacilityAppConfig):
        definitions = {
            "7-day-clinic": dict(
                days=[MO, TU, WE, TH, FR, SA, SU],
                slots=[100, 100, 100, 100, 100, 100, 100],
            ),
            "5-day-clinic": dict(
                days=[MO, TU, WE, TH, FR], slots=[100, 100, 100, 100, 100]
            ),
        }

    class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
        pass

    #         configurations = [
    #             AppointmentConfig(
    #                 model="edc_appointment.appointment",
    #                 related_visit_model="dashboard_app.subjectvisit",
    #                 appt_type="hospital",
    #             )
    #         ]

    class EdcMetadataAppConfig(BaseEdcMetadataAppConfig):
        reason_field = {"dashboard_app.subjectvisit": "reason"}
