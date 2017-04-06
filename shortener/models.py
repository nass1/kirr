# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import random
import string

def code_genrator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



class KirrURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        print ("something")
        self.shortcode = code_genrator()
        super (KirrURL, self).save(*args, **kwargs)


    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

