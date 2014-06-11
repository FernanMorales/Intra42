__author__ = 'tcollart'

from django import template
from datetime import datetime
from ldaplogin.Auth42 import auth42
import urllib
import ast

register = template.Library()

@register.filter
def outdated(value):
    now = datetime.date(datetime.now())
    if now < value:
        return True
    return False


@register.filter
def get_picture(value):
    ldap = auth42.Auth42()

    try:
        return ldap.ldap_get_picture(value)
    except TypeError:
        print value
    except AttributeError:
        print value

@register.filter
def get_pos(login):
    u = urllib.urlopen('https://dashboard.42.fr/crawler/pull/' + login)
    data = u.read()
    data = ast.literal_eval(data)
    if 'last_host' in data:
        data = data['last_host'][:-6]
    else:
        data = None
    return data
