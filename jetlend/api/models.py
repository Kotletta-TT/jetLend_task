from django.contrib.auth.models import AbstractUser
from django.db import models, transaction
from django.db.models import Choices, signals
from django.dispatch import receiver


class Investor(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)


class Qualification(models.Model):
    NEW = 'Start'
    LV1 = 'Level 1'
    LV2 = 'Level 2'
    CNF = 'Confirm'
    FAL = 'Failure'
    STATUS = (
        (NEW, 'New'),
        (LV1, 'Level 1'),
        (LV2, 'Level 2'),
        (CNF, 'Confirm'),
        (FAL, 'Failure'),
    )
    investor = models.OneToOneField(Investor, on_delete=models.CASCADE)
    status = models.CharField(max_length=7, choices=STATUS, default=NEW)
    rules = models.BooleanField(default=False)


class Passport(models.Model):
    investor = models.OneToOneField(Investor, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic_name = models.CharField(max_length=50)
    serial_number = models.IntegerField()
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=250)
    date_of_issue = models.DateField()
    issued_by = models.CharField(max_length=400)
    code_unit = models.IntegerField()
    place_residence = models.TextField()
    photo_main_page = models.ImageField(upload_to='passports/')
    photo_reg_page = models.ImageField(upload_to='passports/')

    class Meta:
        verbose_name = 'Паспорт'
        verbose_name_plural = 'Паспорта'


class Document(models.Model):
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE, related_name='docs', null=True)
    title = models.CharField(max_length=30)
    file = models.FileField(upload_to='documents/')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


@receiver(signals.post_save, sender=Investor)
def create_qualification(sender, instance, created, **kwargs):
    Qualification.objects.get_or_create(investor_id=instance.pk)


@receiver(signals.post_save, sender=Passport)
def change_status(sender, instance, created, **kwargs):
    qualification = Qualification.objects.get(investor_id=instance.investor)
    qualification.status = 'Level 1'
    qualification.save()
