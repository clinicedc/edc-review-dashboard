from django.contrib import admin
from edc_model_admin.dashboard import (
    ModelAdminCrfDashboardMixin,
    ModelAdminSubjectDashboardMixin,
)

from .admin_site import review_dashboard_app_admin
from .models import (
    CrfFive,
    CrfFour,
    CrfOne,
    CrfSix,
    CrfThree,
    CrfTwo,
    OffSchedule,
    OnSchedule,
    SubjectConsent,
    SubjectRequisition,
    SubjectVisit,
)


@admin.register(OnSchedule, site=review_dashboard_app_admin)
class OnScheduleAdmin(ModelAdminSubjectDashboardMixin, admin.ModelAdmin):
    pass


@admin.register(OffSchedule, site=review_dashboard_app_admin)
class OffScheduleAdmin(ModelAdminSubjectDashboardMixin, admin.ModelAdmin):
    pass


@admin.register(SubjectConsent, site=review_dashboard_app_admin)
class SubjectConsentAdmin(ModelAdminSubjectDashboardMixin, admin.ModelAdmin):
    pass


@admin.register(SubjectVisit, site=review_dashboard_app_admin)
class SubjectVisitAdmin(ModelAdminSubjectDashboardMixin, admin.ModelAdmin):
    pass


@admin.register(CrfOne, site=review_dashboard_app_admin)
class CrfOneAdmin(ModelAdminCrfDashboardMixin, admin.ModelAdmin):
    show_save_next = True
    show_cancel = True


@admin.register(CrfTwo, site=review_dashboard_app_admin)
class CrfTwoAdmin(ModelAdminCrfDashboardMixin, admin.ModelAdmin):
    show_save_next = True
    show_cancel = True


@admin.register(CrfThree, site=review_dashboard_app_admin)
class CrfThreeAdmin(ModelAdminCrfDashboardMixin, admin.ModelAdmin):
    pass


@admin.register(SubjectRequisition, site=review_dashboard_app_admin)
class SubjectRequisitionAdmin(ModelAdminCrfDashboardMixin, admin.ModelAdmin):
    show_save_next = True
    show_cancel = True


@admin.register(CrfFour, site=review_dashboard_app_admin)
class CrfFourAdmin(ModelAdminCrfDashboardMixin, admin.ModelAdmin):
    show_save_next = True
    show_cancel = True


@admin.register(CrfFive, site=review_dashboard_app_admin)
class CrfFiveAdmin(ModelAdminCrfDashboardMixin, admin.ModelAdmin):
    show_save_next = True
    show_cancel = True


@admin.register(CrfSix, site=review_dashboard_app_admin)
class CrfSixAdmin(ModelAdminCrfDashboardMixin, admin.ModelAdmin):
    show_save_next = True
    show_cancel = True
