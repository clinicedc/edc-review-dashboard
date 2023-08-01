from edc_reference import site_reference_configs


def register_to_site_reference_configs():
    site_reference_configs.registry = {}
    site_reference_configs.register_from_visit_schedule(
        visit_models={"edc_appointment.appointment": "edc_visit_tracking.subjectvisit"}
    )

    site_reference_configs.add_fields_to_config(
        name="review_dashboard_app.CrfOne", fields=["f1"]
    )
    site_reference_configs.add_fields_to_config(
        name="review_dashboard_app.CrfTwo", fields=["f1"]
    )
    site_reference_configs.add_fields_to_config(
        name="review_dashboard_app.CrfThree", fields=["f1"]
    )
    site_reference_configs.add_fields_to_config(
        name="review_dashboard_app.CrfFour", fields=["f1"]
    )
    site_reference_configs.add_fields_to_config(
        name="review_dashboard_app.CrfFive", fields=["f1"]
    )
    site_reference_configs.add_fields_to_config(
        name="review_dashboard_app.CrfSix", fields=["f1"]
    )
    site_reference_configs.add_fields_to_config(
        name="review_dashboard_app.CrfSeven", fields=["f1"]
    )
