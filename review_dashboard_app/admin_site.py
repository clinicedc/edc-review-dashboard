from django.contrib.admin import AdminSite


class DashboardAppAdminSite(AdminSite):
    site_header = "DashboardApp"
    site_title = "DashboardApp"
    index_title = "DashboardApp Administration"
    site_url = "/administration/"


review_dashboard_app_admin = DashboardAppAdminSite(name="review_dashboard_app_admin")
