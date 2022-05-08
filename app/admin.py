from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.utils.safestring import mark_safe
from .models import *

try:
    admin.site.unregister(User)
    admin.site.unregister(Group)
except:
    pass


@admin.register(Lessons)
class LessonAdmin(admin.ModelAdmin):

    list_display = ['title']


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ContactUs._meta.fields]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Classes)
#
# @admin.register(Gallery)
# class GalleryAdmin(admin.ModelAdmin):
#     def get_image(self, object):
#         return mark_safe('<img src="{}" height="100px" width="100px" />'.format(object.image.url))
#
#     get_image.short_description = "Նկար"
#
#     list_display = ['get_image']
#
#
# @admin.register(AboutUs)
# class AboutUsAdmin(SingleModelAdmin):
#     pass
#


