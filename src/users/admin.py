from django.contrib import admin
from django.contrib.auth import get_user_model


User = get_user_model()



class UserModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserModelAdmin)
