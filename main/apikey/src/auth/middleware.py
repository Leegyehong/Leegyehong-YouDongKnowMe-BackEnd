from django.http import JsonResponse
import re

from .jwt_auth import verifyJwtToken


class KeyAuthorize:
    
    def __init__(self, get_response):
        
        self.get_response= get_response
        self.admin_urls = ['^/admin.*$']
        self.admin_pattern = re.compile('|'.join(self.admin_urls),re.MULTILINE)
    
    
    def __call__(self, request):
        
        response = self.get_response(request)
        path = request.path_info
        if re.search(self.admin_pattern, path):
            return response
        api_key = request.GET.get('api_key')
        if api_key:
            isKey = verifyJwtToken('access', api_key)
            print(isKey)
            if not isKey[0]:
                return JsonResponse(isKey[1],status=401)
            else: 
                return response
        else:
            return JsonResponse({'info': 'no api_key'},status=401)
        
        
        