from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError


class TblCategories(models.Model):
    name_category = models.CharField(verbose_name=_('Name Category'), max_length=250)

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

class TblBrandCategories(models.Model):
    name_brand_category = models.CharField(verbose_name=_('Name Brand'), max_length=250)

    def __str__(self):
        return self.name_brand_category

    class Meta:
        verbose_name = _('Brand Category')
        verbose_name_plural = _('Brand Categories')


class TblCompany(models.Model):
    name_company = models.CharField(verbose_name=_('Name Company'), max_length=250)

    def __str__(self):
        return self.name_company

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')


class TblDepartment(models.Model):
    name_department = models.CharField(verbose_name=_('Name Department'), max_length=250)

    def __str__(self):
        return self.name_department

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')


RAM_SIZE_CHOICES = [
    ('4', '4'),
    ('8', '8'),
    ('16', '16'),
    ('32', '32'),
]

Hard_Disk_Type_CHOICES = [
    ('HDD', 'HDD'),
    ('SSD', 'SSD'),
]

Capacity_Hard_Disk_CHOICES = [
    ('250GB', '250GB'),
    ('500GB', '500GB'),
    ('1TB', '1TB'),
]



class TblAssetsManagement(models.Model):
    asset_number = models.IntegerField(verbose_name=_('Asset Number'), null=False, blank=False)
    name_asset = models.CharField(verbose_name=_('Name Asset'), max_length=250, null=False, blank=False)
    name_brand_category = models.ForeignKey(TblBrandCategories, on_delete=models.CASCADE, verbose_name=_("Name Brand Category"), null=True, blank=True)
    description_asset = models.TextField()
    serial_asset = models.TextField(max_length=250, verbose_name=_('Serial Asset'), null=False, blank=False)
    image_property = models.ImageField(upload_to="images/assets_awn", verbose_name=_('Image Property'), null=False, blank=False)
    name_category = models.ForeignKey(TblCategories, on_delete=models.CASCADE, verbose_name=_("Name Category"), null=False, blank=False)
    ram_size = models.CharField(max_length=10, choices=RAM_SIZE_CHOICES, verbose_name=_("RAM Size"), null=True, blank=True)
    hard_disk_type = models.CharField(max_length=10, choices=Hard_Disk_Type_CHOICES, verbose_name=_("Hard Disk Type"), null=True, blank=True)
    capacity_hard_disk = models.CharField(max_length=10, choices=Capacity_Hard_Disk_CHOICES, verbose_name=_("Capacity Hard Disk Type"), null=True, blank=True)
    use_it_by = models.CharField(max_length=250, verbose_name=_("Use it by"), null=False, blank=False)
    status_asset = models.CharField(verbose_name=_('Status Asset'), max_length=250, null=False, blank=False)
    did_i_check_it = models.BooleanField(default=False, verbose_name=_("Did I check it"), null=False, blank=False)
    date_take = models.DateField(verbose_name=_("Date Take"), null=False, blank=False)
    returned_take = models.DateField(verbose_name=_("Date Returned"), null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.asset_number} - {self.serial_asset} - {self.name_brand_category}"

    class Meta:
        verbose_name = _('Asset Management')
        verbose_name_plural = _('Assets Management')


def validate_pdf(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError(_('Only PDF files are allowed....................'))


class TblCustomUser(AbstractUser):
    phone_number = models.IntegerField(verbose_name=_('Phone Number'), null=True, blank=False)
    company = models.ForeignKey(TblCompany, related_name="user_company", on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(TblDepartment, related_name="user_department", on_delete=models.CASCADE, null=True, blank=False)
    signature_file = models.FileField(upload_to='signatures/', validators=[validate_pdf], null=True, blank=False)
    assets = models.ForeignKey(TblAssetsManagement, related_name="user_assets_management", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class TblAssetsImages(models.Model):
    assets_title_image = models.ForeignKey(TblAssetsManagement, related_name='images_assets', on_delete=models.CASCADE)
    images_assets = models.FileField(upload_to="images/assets_awn", verbose_name=_('Images Assets'))

    class Meta:
        verbose_name = _('Asset Image')
        verbose_name_plural = _('Asset Images')

