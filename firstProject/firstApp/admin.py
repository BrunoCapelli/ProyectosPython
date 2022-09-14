from django.contrib import admin
from .models import Article, Categoria
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ("cratead_at", "updated_at")
 

admin.site.register(Article, ArticleAdmin)
admin.site.register(Categoria)

admin.site.site_header = 'Primer Backend'
admin.site.site_title = 'Primer Backend'
admin.site.index_title = "Administrar"