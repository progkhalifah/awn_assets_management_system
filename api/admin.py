from django.contrib import admin

from api.models import *

admin.site.site_title = 'AWN Dashboard'
admin.site.site_header = 'AWN Dashboard Admin'
admin.site.index_title = 'AWN'


@admin.register(TblCustomUser)
class TblCustomUserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "company", "department", "signature_file", "assets", )
    search_fields = ("first_name", "last_name", "company", "department", "assets",)
    list_filter = ("first_name", "last_name", "company", "department", "assets",)
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']

    # ordering = ['']

@admin.register(TblCategories)
class TblCategoriesAdmin(admin.ModelAdmin):
    list_display = ["name_category"]
    search_fields = ["name_category"]
    list_filter = ["name_category"]
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']

    # ordering = ['']

@admin.register(TblBrandCategories)
class TblBrandCategoriessAdmin(admin.ModelAdmin):
    list_display = ["name_brand_category"]
    search_fields = ["name_brand_category"]
    list_filter = ["name_brand_category"]
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']

    # ordering = ['']



@admin.register(TblCompany)
class TblCompanyAdmin(admin.ModelAdmin):
    list_display = ["name_company"]
    search_fields = ["name_company"]
    list_filter = ["name_company"]
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']

    # ordering = ['']

@admin.register(TblDepartment)
class TblDepartmentAdmin(admin.ModelAdmin):
    list_display = ["name_department"]
    search_fields = ["name_department"]
    list_filter = ["name_department"]
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']

    # ordering = ['']

@admin.register(TblAssetsManagement)
class TblAssetsManagementAdmin(admin.ModelAdmin):
    list_display = ("asset_number", "name_brand_category", "name_asset", "serial_asset", "use_it_by", "did_i_check_it",)
    search_fields = ("name_asset", "serial_asset", "asset_number",)
    list_filter = ("name_brand_category", "serial_asset", "asset_number",)
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']

    # ordering = ['']

@admin.register(TblAssetsImages)
class TblAssetsImagesAdmin(admin.ModelAdmin):
    list_display = ("assets_title_image", "images_assets")
    search_fields = ("assets_title_image", "images_assets")
    list_filter = ("assets_title_image", "images_assets")
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']

    # ordering = ['']
