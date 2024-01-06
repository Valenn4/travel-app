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
    return len(value.split(","))-1

@register.filter(name="contain_like")
def contain_like(value):
    list = value[1:-2]
    return list.split(",")

