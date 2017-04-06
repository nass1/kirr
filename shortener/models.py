# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .utils import code_genrator, create_shortcode


class KirrURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = code_genrator(self)
        super (KirrURL, self).save(*args, **kwargs)


    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

