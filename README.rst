|pypi| |actions| |codecov| |downloads|

Edc Review Dashboard
====================

An alternative dashboard of a subject's visits, CRFs and Requisitions.


Declare in your app:


.. code-block:: python

    class SubjectReviewListboardView(Base):

        listboard_model = 'ambition_subject.subjectvisit'
        model_wrapper_cls = SubjectVisitModelWrapper
        navbar_name = 'ambition_dashboard'

Add URLs:

.. code-block:: python

	urlpatterns = ....

    review_listboard_url_config = UrlConfig(
        url_name='subject_listboard_url',
        view_class=SubjectListboardView,
        label='subject_listboard',
        identifier_label='subject_identifier',
        identifier_pattern=subject_identifier)
    urlpatterns += review_listboard_url_config.review_listboard_urls



.. |pypi| image:: https://img.shields.io/pypi/v/edc-review-dashboard.svg
    :target: https://pypi.python.org/pypi/edc-review-dashboard

.. |actions| image:: https://github.com/clinicedc/edc-review-dashboard/workflows/build/badge.svg?branch=develop
  :target: https://github.com/clinicedc/edc-review-dashboard/actions?query=workflow:build

.. |codecov| image:: https://codecov.io/gh/clinicedc/edc-review-dashboard/branch/develop/graph/badge.svg
  :target: https://codecov.io/gh/clinicedc/edc-review-dashboard

.. |downloads| image:: https://pepy.tech/badge/edc-review-dashboard
   :target: https://pepy.tech/project/edc-review-dashboard
