# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Menu(models.Model):
    range = models.TextField()
    date = models.TextField()
    restaurant = models.TextField(blank=True, null=True)
    menu_division = models.TextField(blank=True, null=True)
    menu_content = models.TextField(blank=True, null=True)
    etc_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'


class Noti(models.Model):
    major_code = models.IntegerField(primary_key=True)
    num = models.IntegerField()
    title = models.TextField(blank=True, null=True)
    writer = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    img_url = models.TextField(blank=True, null=True)
    file_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'noti'
        unique_together = (('major_code', 'num'),)


class Schedule(models.Model):
    year = models.TextField()
    month = models.IntegerField()
    date = models.TextField()
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedule'
