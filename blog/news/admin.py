from django.contrib import admin
from .models import News, Category, Tag, Comments
from django_summernote.admin import SummernoteModelAdmin


class NewsAdmin(SummernoteModelAdmin):
    list_display = ('title', 'user', 'created')
    list_editable = ('user', )  # можно в админке менять автора статьи
    list_filter = ('user', 'created')  # появился боковой фильтр по автору и дате
    search_fields = ('title', 'user__username')  # строка поиска
    summer_note_fields = ('text_min', 'text')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'new', 'created', 'moderation')


admin.site.register(News, NewsAdmin)
admin.site.register(Comments, CommentAdmin)
admin.site.register(Category)
admin.site.register(Tag)
