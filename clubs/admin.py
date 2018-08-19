from django.contrib import admin
from .models import President,Etudiant,Club,SuperAdmin1,SuperAdmin2,UserProfile,Activity,Invitation

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'niveau', 'skills', 'site', 'tel')

    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-niveau', 'user')
        return queryset

    user_info.short_description = 'Info'


admin.site.register(UserProfile)
admin.site.register(Invitation)
 
admin.site.register(Etudiant)
admin.site.register(Club)
admin.site.register(Activity)
admin.site.register(SuperAdmin2)
# Register your models here.
