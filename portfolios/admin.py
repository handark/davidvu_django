from portfolios.models import Company, Category, Image
from django.contrib import admin

class ImageInline(admin.TabularInline):
    model = Image
    extra = 3
    fields = ('name', 'image')

class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("company_name",)}
    
    fieldsets = [
        ('Company Information',         {'fields': ['company_name', 'slug', 'description', 'description_en', 'url', 'year', 'design', 'order']}),
        ('Category and date',         {'fields': ['category', 'pub_date']}),
    ]
    
    inlines = [ImageInline]

    list_display = ('company_name', 'pub_date')
    list_filter = ['pub_date', 'design']
    search_fields = ['company_name', 'design']
    date_hierarchy = 'pub_date'

admin.site.register(Company, CompanyAdmin)
admin.site.register(Category)