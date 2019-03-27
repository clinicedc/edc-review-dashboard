from django.contrib import admin
from django.urls import path

from .admin_site import dashboard_app_admin
from .views import SubjectReviewListboardView, SubjectDashboardView, HomeView

app_name = "dashboard_app"

urlpatterns = SubjectReviewListboardView.urls(
    app_name,
    label="subject_review_listboard")
urlpatterns += SubjectDashboardView.urls(
    app_name,
    label="subject_dashboard")

urlpatterns += [
    path("admin/", admin.site.urls),
    path("admin/", dashboard_app_admin.urls),
    path("", HomeView.as_view(), name="home_url"),
    path("", HomeView.as_view(), name="administration_url")]
