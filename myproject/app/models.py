from django.db import models


class ModelA(models.Model):
    a_one = models.CharField(max_length=255)
    a_two = models.CharField(max_length=255)
    a_three = models.CharField(max_length=255)


class ModelB(models.Model):
    b_one = models.CharField(max_length=255)
    b_two = models.CharField(max_length=255)
    b_three = models.CharField(max_length=255)


class ModelC(models.Model):
    c_one = models.CharField(max_length=255)
    c_two = models.CharField(max_length=255)
    c_three = models.CharField(max_length=255)
    