from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .models import *

@api_view(["GET"])
def log_queries(request):
    query_params = request.GET.dict()
    return Response(query_params)