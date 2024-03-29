from edc_navbar import Navbar, NavbarItem, site_navbars

navbar = Navbar(name="edc_review_dashboard")

navbar_item = NavbarItem(
    name="subject_review",
    label="Review",
    title="Subject Review",
    codename="edc_review_dashboard.view_subject_review_listboard",
    url_name="subject_review_listboard_url",
)


navbar.register(navbar_item)

site_navbars.register(navbar)
