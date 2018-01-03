import random
import string

from django.conf import settings


SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)

#from shorterner.models import KirrURL

def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits): #def code_generator(size=6, chars="abcdefghiklmnoprstuvwyxz1234567890"):
	#new_code = ''
	#for _ in range(size):
	#	new_code += random.choice(chars)
	#return new_code 
	return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=SHORTCODE_MIN):
	new_code = code_generator(size=size)
	Klass = instance.__class__
	qs_exists = Klass.objects.filter(shortcode=new_code).exists()
	if qs_exists:
		return create_shortcode(size=size)
	return new_code

def soyadi_olustur(size=1, sayi=string.digits + string.ascii_lowercase):
	syd = "Kilic"
	#syd1 = syd.join(random.choice(sayi) for i in range(size))
	return syd

def soyad_koy(instance, soyadd="Kilic"):
	soyadd = "Kilic"
	Mirkan = instance.__class__
	qs_exists = Mirkan.objects.filter(soyad=soyadd).exists()
	if qs_exists:
		return soyad_koy()
	return soyadd