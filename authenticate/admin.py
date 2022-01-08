from django.contrib import admin
from authenticate.models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','pk', 'gender', 'designation')
    search_fields = ('user__email', 'user__username', 'age', 'designation', 'group')
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    date_hierarchy = 'user__date_joined'
    order_by = '-user__date_joined'

    def get_queryset(self, request):
        queryset = super(ProfileAdmin, self).get_queryset(request)
        return queryset.order_by('-user__date_joined')
