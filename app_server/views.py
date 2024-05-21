from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import VillageMap
from django.db import connection

def get_village_maps(request):
    with connection.cursor() as cursor:
        sql = "SELECT gid, survey_no, ST_AsText(st_transform(geom, 4326)) FROM dagdagad.survey_georeferenced"
        cursor.execute(sql)
        rows = cursor.fetchall()
    
    # Process rows if needed
    data = [{'gid': row[0], 'survey_no': row[1], 'geom': row[2]} for row in rows]
    
    return JsonResponse(data, safe=False)

def geojson_list(request):
    village_maps = VillageMap.objects.all()
    
    features = []
    for village_map in village_maps:
        feature = {
            "type": "Feature",
            "geometry": GEOSGeometry(village_map.geom).json,
            "properties": {
                "gid": village_map.gid,
                "survey_no": village_map.survey_no,
                # Add other properties as needed
            }
        }
        features.append(feature)
    
    geojson_data = {
        "type": "FeatureCollection",
        "features": features
    }
    
    return JsonResponse(geojson_data)

def index(request):
    return HttpResponse("Welcome to Telengana Server!")