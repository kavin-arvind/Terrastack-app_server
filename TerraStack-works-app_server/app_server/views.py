from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import VillageMap
from django.db import connection
from django.middleware.gzip import GZipMiddleware

@GZipMiddleware
def get_village_maps(request):
    village_name = request.GET.get('village_name', 'dagdagad')
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT gid, survey_tag, survey_tag_gid, description, varp,  ST_AsText(st_transform(geom, 4326)) FROM {village_name}.table_with_survey_tags;"
            cursor.execute(sql)
            rows = cursor.fetchall()
    
    except:
        print("error")
        return None
    
    # Process rows if needed
    data = [{'gid': row[0], 'survey_tag': row[1], 'survey_tag_gid':row[2], 'description':row[3], 'varp':row[4], 'geom': row[5]} for row in rows]
    
    return JsonResponse(data, safe=False)

def geojson_list(request):
    # village_maps = VillageMap.objects.all()
    
    # features = []
    # for village_map in village_maps:
    #     feature = {
    #         "type": "Feature",
    #         "geometry": GEOSGeometry(village_map.geom).json,
    #         "properties": {
    #             "gid": village_map.gid,
    #             "survey_no": village_map.survey_no,
    #             # Add other properties as needed
    #         }
    #     }
    #     features.append(feature)
    
    # geojson_data = {
    #     "type": "FeatureCollection",
    #     "features": features
    # }
    
    # return JsonResponse(geojson_data)
    return HttpResponse("geojson directory.. try village-maps/")

def index(request):
    return HttpResponse("Welcome to Telengana Server!")