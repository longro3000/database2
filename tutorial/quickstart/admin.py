# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
# Register your models here.
from django.contrib.auth.models import Champion, Item

admin.site.register(Champion)
admin.site.register(Item)