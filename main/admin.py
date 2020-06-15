from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Img, Comment, Classification, UserProfile


# Register your models here.
class adminIMG(admin.ModelAdmin):
    list_display = ('image', 'createTime', 'cmpScore', 'like', 'author','label')
    # fieldsets = (
    #     (None, {'fields': ('name', 'in_class')}),
    # )
    # filter_horizontal = ('in_class',)


admin.site.register(Img, adminIMG)


class adminCOMMENT(admin.ModelAdmin):
    list_display = ('author', 'img', 'createTime', 'content')


admin.site.register(Comment, adminCOMMENT)


# class adminCLASSIFICATION(admin.ModelAdmin):
#     list_display = ('name')


admin.site.register(Classification)

class adminUserProfile(admin.ModelAdmin):
    list_display = ('userProfile',)


admin.site.register(UserProfile, adminUserProfile)

