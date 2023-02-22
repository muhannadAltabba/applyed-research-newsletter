from django.contrib import admin
from .models import Article, Contributor, Section, Domain, Publisher



admin.site.site_header = 'Newsletter administration'

# Register your models here.
class ContributorAdmin(admin.ModelAdmin):
    list_display = ('name', 'section', 'phone', 'email')
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'abstruct_problem', 'abstruct_contribution', 'domain', 'contributor_name', 'views','publication_date', 'created_at', 'lead', 'article_file')
class DomainAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','photo')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Section)
admin.site.register(Publisher)
admin.site.register(Domain, DomainAdmin)


