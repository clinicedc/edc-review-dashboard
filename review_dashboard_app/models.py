import uuid

from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from edc_consent.field_mixins import PersonalFieldsMixin
from edc_consent.field_mixins.identity_fields_mixin import IdentityFieldsMixin
from edc_consent.model_mixins import ConsentModelMixin
from edc_constants.choices import YES_NO
from edc_crf.model_mixins import CrfModelMixin
from edc_identifier.managers import SubjectIdentifierManager
from edc_identifier.model_mixins import UniqueSubjectIdentifierFieldMixin
from edc_lab.model_mixins import RequisitionModelMixin
from edc_model.models import BaseUuidModel
from edc_offstudy.model_mixins import OffstudyModelMixin
from edc_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin
from edc_sites.models import SiteModelMixin
from edc_visit_schedule.model_mixins import OffScheduleModelMixin, OnScheduleModelMixin
from edc_visit_tracking.models import SubjectVisit


class BasicModel(SiteModelMixin, BaseUuidModel):
    f1 = models.CharField(max_length=10)
    f2 = models.CharField(max_length=10)
    f3 = models.CharField(max_length=10, null=True, blank=False)
    f4 = models.CharField(max_length=10, null=True, blank=False)
    f5 = models.CharField(max_length=10)
    f5_other = models.CharField(max_length=10, null=True)
    subject_identifier = models.CharField(max_length=25, default="12345")


class OnSchedule(SiteModelMixin, OnScheduleModelMixin, BaseUuidModel):
    pass


class OffSchedule(SiteModelMixin, OffScheduleModelMixin, BaseUuidModel):
    pass


class SubjectOffstudy(OffstudyModelMixin, BaseUuidModel):
    class Meta(OffstudyModelMixin.Meta):
        pass


class DeathReport(UniqueSubjectIdentifierFieldMixin, SiteModelMixin, BaseUuidModel):
    objects = SubjectIdentifierManager()

    def natural_key(self):
        return (self.subject_identifier,)


class SubjectConsent(
    ConsentModelMixin,
    PersonalFieldsMixin,
    IdentityFieldsMixin,
    UniqueSubjectIdentifierFieldMixin,
    UpdatesOrCreatesRegistrationModelMixin,
    SiteModelMixin,
    BaseUuidModel,
):
    objects = SubjectIdentifierManager()

    def natural_key(self):
        return (self.subject_identifier,)


class SubjectRequisition(RequisitionModelMixin, BaseUuidModel):
    subject_visit = models.ForeignKey(SubjectVisit, on_delete=PROTECT)

    requisition_datetime = models.DateTimeField(null=True)

    is_drawn = models.CharField(max_length=25, choices=YES_NO, null=True)

    reason_not_drawn = models.CharField(max_length=25, null=True)


class BaseCrfModel(SiteModelMixin, models.Model):
    subject_identifier = models.CharField(max_length=25)

    subject_visit = models.ForeignKey(SubjectVisit, on_delete=CASCADE)

    f1 = models.CharField(max_length=50, default=uuid.uuid4)

    @property
    def related_visit(self):
        return getattr(self, self.related_visit_model_attr())

    @classmethod
    def related_visit_model_attr(cls):
        return "subject_visit"

    def save(self, *args, **kwargs):
        self.subject_identifier = self.subject_visit.subject_identifier
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class CrfOne(BaseCrfModel, CrfModelMixin, BaseUuidModel):
    pass


class CrfTwo(BaseCrfModel, CrfModelMixin, BaseUuidModel):
    pass


class CrfThree(BaseCrfModel, CrfModelMixin, BaseUuidModel):
    pass


class CrfFour(BaseCrfModel, CrfModelMixin, BaseUuidModel):
    pass


class CrfFive(BaseCrfModel, CrfModelMixin, BaseUuidModel):
    pass


class CrfSix(BaseCrfModel, CrfModelMixin, BaseUuidModel):
    pass


class CrfSeven(BaseCrfModel, CrfModelMixin, BaseUuidModel):
    pass


class RedirectModel(BaseUuidModel):
    subject_identifier = models.CharField(max_length=25)


class RedirectNextModel(BaseUuidModel):
    subject_identifier = models.CharField(max_length=25)
