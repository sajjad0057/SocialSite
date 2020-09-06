from django.contrib import admin
from Login_App.models import UserProfile,Follow



# Change admin site fontend:
admin.site.site_header = "Social Site Administration"
admin.site.site_title = "Social Site Administration"
admin.site.index_title = 'Exclusice Social Site'

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Follow )