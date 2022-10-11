from django import template

register = template.Library()

@register.filter(name='sum')
def sum_tags(a):
    pass