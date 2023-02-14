from django_countries import countries

def get_region_from_country(country):
    region = None
    country_code = country.code
    if country_code in countries.EU:
        region = 'Europe'
    elif country_code in countries.AS or country_code in countries.OC or country_code in countries.ME:
        region = 'Asia'
    elif country_code in countries.US:
        region = 'US'
    # Add other regions here...
    return region
