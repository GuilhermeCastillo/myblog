from django.contrib import admin
from articles.models import Article, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("tag", "date", "author", "title", "content", "photo")
    search_fields = ("title",)


admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
