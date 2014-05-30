from django.contrib import admin
from models import *

admin.site.register((Category, SubCategory, Thread, Post, Comment))
