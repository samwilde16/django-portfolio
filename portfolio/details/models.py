from django.db import models

from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import FieldPanel

@register_setting
class SocialMediaSettings(BaseSetting):
    class Meta:
        verbose_name = 'Social media accounts'
    instagram = models.CharField(
        max_length=255, help_text='Your Instagram username, without the @')
    youtube = models.URLField(
        help_text='Your YouTube channel or user account URL')

    panels = [
        FieldPanel('instagram'),
        FieldPanel('youtube'),
    ]

@register_setting
class ContactInformation(BaseSetting):
    class Meta:
        verbose_name = 'Contact Information'
    mobile_number = models.CharField(
        max_length=255, help_text='Your mobile number beginning with 0')

    panels = [
        FieldPanel('mobile_number'),
    ]