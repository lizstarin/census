from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from models import ZipCode, HousingUnits

def index(request):
	zip_codes = ZipCode.objects.order_by('value')
	zips = {}
	zips_list = []

	for zip_code in zip_codes:
		housing_units = HousingUnits.objects.get(id=zip_code.id)
		zips[zip_code.value] = {"total": housing_units.total, "occupied": housing_units.occupied, "vacant": housing_units.vacant}

	print(zips)

	template = loader.get_template('map/index.html')
	context = RequestContext(request, {
		'zips': zips
	})
	return HttpResponse(template.render(context))


