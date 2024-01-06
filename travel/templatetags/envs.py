import json
import os
from django import template
from environments import env

register = template.Library()

@register.simple_tag
def get_env(key):
    return env(key)

'''
@register.filter(name="split")
def split(value):
    list = json.loads(value)
    return list[0]
'''

@register.filter(name="len_likes")
def len_like(value):
    if value == '':
        return 0
    
    if '' in value.split(","):
        return len(value.split(","))-1
    else:
        return len(value.split(","))

@register.filter(name="contain_like")
def contain_like(value):
    return value.split(",")

@register.filter(name="string")
def string(value):
    return str(value)

