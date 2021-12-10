from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView


# 基于Django的函数请求
def apple_django(request):
    d = request.resolver_match
    """
    ResolverMatch(func=apple.views.apple, args=(), kwargs={}, url_name=index, app_names=['apple'], 
    namespaces=['npc'], route=npc/)
    """
    print(d)
    return HttpResponse('apple django.....')


# 基于drf的函数请求
@api_view(['GET'])
def apple_drf(request):
    return Response('apple drf.....')


# 基于drf的class请求
class AppleViews(APIView):
    def get(self, request):
        d = request.resolver_match
        print(d)
        """
        ResolverMatch(func=apple.views.AppleViews, args=(), kwargs={}, url_name=apple_class, app_names=['apple'], 
        namespaces=['vip'], route=vip/apple_class/)
        """
        return Response('apple class get.....')

    def post(self, request):
        return Response('apple class post.....')
