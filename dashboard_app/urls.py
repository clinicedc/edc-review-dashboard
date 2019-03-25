from django.contrib import admin
from django.urls import path
from edc_dashboard.url_config import UrlConfig

from .admin_site import dashboard_app_admin
from .views import SubjectReviewListboardView, SubjectDashboardView, HomeView

app_name = "dashboard_app"

subject_review_listboard_url_config = UrlConfig(
    url_name='subject_review_listboard_url',
    namespace=app_name,
    view_class=SubjectReviewListboardView,
    label='subject_review_listboard',
    identifier_label='subject_identifier',
    identifier_pattern="\w+",
)

subject_dashboard_url_config = UrlConfig(
    url_name='subject_dashboard_url',
    namespace=app_name,
    view_class=SubjectDashboardView,
    label='subject_dashboard',
    identifier_label='subject_identifier',
    identifier_pattern="\w+",
)

urlpatterns = subject_review_listboard_url_config.review_listboard_urls
urlpatterns += subject_dashboard_url_config.dashboard_urls


urlpatterns += [
    path("admin/", admin.site.urls),
    path("admin/", dashboard_app_admin.urls),
    path("", HomeView.as_view(), name="home_url"),
    path("", HomeView.as_view(), name="administration_url")]
