import requests, json

api_key = "d49dfea7da9a0f6ebe26f462168918246eba6087"
url = "http://api.census.gov/data/2010/sf1?key=" + api_key + "&get=H0030001,H0030002,H0030003,NAME&for=zip+code+tabulation+area:*&in=state:36"

string_data = eval(requests.get(url).text) # for purposes of this exercise, assume that a call to census.gov is safe to eval--obviously bad practice normally
string_data.pop(0)
data = [[int(l[0]), int(l[1]), int(l[2]), int(l[5])] for l in string_data]

f = open('map/fixtures/housing_fixture.json', 'w+')
fixture_json = []

for i, l in enumerate(data, start=1):
	fixture_json.append({
			"model": "map.zipcode",
			"pk": i,
			"fields": {
				"value": l[3]
			}
		})

	fixture_json.append({
			"model": "map.housingunits",
			"pk": i,
			"zipcode_id": i,
			"fields": {
				"total": l[0],
				"occupied": l[1],
				"vacant": l[2]
			}
		})

f.write(json.dumps(fixture_json))
f.close()

