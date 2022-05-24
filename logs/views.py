from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .models import *
from .logger import logger

@api_view(["GET"])
def log_queries(request):
    query_params = request.GET.dict()
    logger.debug(query_params)
    return Response(query_params)