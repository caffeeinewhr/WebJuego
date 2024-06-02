# middleware.py
from django.utils.deprecation import MiddlewareMixin

class SetMimeTypeMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.path.endswith('.pck'):
            response['Content-Type'] = 'application/octet-stream'
        elif request.path.endswith('.wasm'):
            response['Content-Type'] = 'application/wasm'
        return response
