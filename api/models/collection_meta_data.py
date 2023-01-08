from django.db import models


class CollectionMetaData(models.Model):
    """This is where we store metadata related to file downloads"""
    filename = models.CharField(max_length=255)
    date_downloaded = models.DateTimeField(auto_add_now=True)