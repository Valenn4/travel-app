import json
import os
from django import template
from environments import env

register = template.Library()

@register.simple_tag
def get_env(key):
    return env(key)

@register.simple_tag
def split(value):
    list = json.loads(value)
    return list[0]