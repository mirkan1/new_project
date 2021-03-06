from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from .utils import create_shortcode

def validate_url(value):
	url_validator = URLValidator()
	value_1_invalid = False
	value_2_invalid = False
	try:
		url_validator(value)
	except:
		value_1_invalid = True

	value_2_url = "http://" + value
	try:
		url_validator(value_2_url)
	except:
		value_2_invalid = True
		
	if value_1_invalid == False and value_2_invalid == False:
		raise forms.ValidationError("gecersiz haci ('https://' yok)")
	return value

def validate_dot_com(value):
	if not 'com' in value:
		raise forms.ValidationError('.com yok ama heci')
	return value

# def validate_http(value, *args, **kwargs):
# 	if not "http://www." in value:
# 		create_shortcode(value)
# 	return create_shortcode(value)