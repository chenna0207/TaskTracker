from django.contrib import admin
from .models import Project, UserProjectRole, Task

class UserProjectRoleInline(admin.TabularInline):
    model = UserProjectRole
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'owner')
    search_fields = ('name', 'owner__username')
    inlines = [UserProjectRoleInline]
    autocomplete_fields = ['owner']

@admin.register(UserProjectRole)
class UserProjectRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'role')
    search_fields = ('user__username', 'project__name', 'role')
    list_filter = ('role',)
    autocomplete_fields = ['user', 'project']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('description', 'due_date', 'status', 'owner', 'project', 'assigned_user')
    search_fields = ('description', 'owner__username', 'assigned_user__username', 'project__name')
    list_filter = ('status', 'project')
    autocomplete_fields = ['owner', 'project', 'assigned_user']
