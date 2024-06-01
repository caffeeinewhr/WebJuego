# middleware.py
from django.utils.deprecation import MiddlewareMixin

class CrossOriginIsolationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['Cross-Origin-Opener-Policy'] = 'same-origin'
        response['Cross-Origin-Embedder-Policy'] = 'require-corp'
        return response

class CrossOriginResourcePolicyMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if 'webgato.onrender.com' in request.get_host():
            response['Cross-Origin-Resource-Policy'] = 'same-site'
        else:
            response['Cross-Origin-Resource-Policy'] = 'cross-origin'
        return response