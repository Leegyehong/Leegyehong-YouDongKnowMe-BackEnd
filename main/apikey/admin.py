from django.contrib import admin
from .models import ApiKey
import datetime

from .src.auth.jwt_auth import createJwtTokenWithInfo
# Register your models here.

class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'apikey']
    readonly_fields = ('apikey',)
    
    def save_model(self, request, obj, form, change):
        user_info={
            'name' : obj.name,
            'email' : obj.email
        }
        
        if not obj.apikey:
            api_key = createJwtTokenWithInfo(user_info)
            obj.apikey = api_key
        super(ApiKeyAdmin, self).save_model(request, obj, form, change)
admin.site.register(ApiKey, ApiKeyAdmin)