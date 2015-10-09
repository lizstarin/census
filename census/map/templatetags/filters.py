from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(a, b):
	return a * b

@register.filter(name='divide')
def divide(a, b):
	if b == 0:
		return 0
	return a / float(b)

@register.filter(name='round')
def round(a):
	return round(a, 2)