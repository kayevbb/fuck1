from django.contrib import admin

from .models import Pole, Comment, PoleImage, Reservation


class CommentInline(admin.TabularInline):
    model = Comment


class PoleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Pole, PoleAdmin)
admin.site.register(Comment)
admin.site.register(PoleImage)
admin.site.register(Reservation)