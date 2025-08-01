from django.http import HttpResponseRedirect
from django.urls import resolve, Resolver404

class IfRouteNotFoundMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        try:
            resolve(request.path)
        except Resolver404:
            return HttpResponseRedirect('/start/')
        return self.get_response(request)