from django.contrib import admin
from main.models import (
    Tag,
    Achievement, 
    Project, 
    Institution,
    Skill,
    Education,
    Staff,
    Student,
    Recruiter
)
# Register your models here.

# admin.site.register(Tag)
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = ('title',)
    search_fields = ('title',)
    readonly_fields = ('id',)
    # readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):

    list_display = ('title',)
    search_fields = ('title',)
    readonly_fields = ('id',)
    # readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# admin.site.register(Project)
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = ('addedBy', 'title', 'domain', 'field', 'dateCreated', 'pk')
    search_fields = ('addedBy__email', 'addedBy__username', 'title', 'domain', 'field')
    readonly_fields = ('dateCreated', )

    filter_horizontal = ()
    list_filter = ('title', 'field', 'domain',)
    fieldsets = ()

    date_hierarchy = 'dateCreated'
    order_by = '-dateCreated'

# admin.site.register(Achievement)
@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):

    list_display = ('addedBy', 'dateCreated', 'title', 'technical', 'approved')
    search_fields = ('addedBy__email', 'addedBy__username', 'title', 'techincal', 'institution', 'approvedBy__email', 'approvedBy__username')
    readonly_fields = ('dateCreated',)

    filter_horizontal = ()
    list_filter = ('title', 'approved', 'technical')
    fieldsets = ()

    date_hierarchy = 'dateCreated'
    order_by = '-dateCreated'

    def get_queryset(self, request):
        queryset = super(AchievementAdmin, self).get_queryset(request)
        return queryset.order_by('-dateCreated')

admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Recruiter)