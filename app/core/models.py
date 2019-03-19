# import uuid
# import os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                       PermissionsMixin
from django.conf import settings


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        # Creates and saves a new user
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        # Creates and saves a new super user.
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class gender(models.Model):
    gender = models.CharField(max_length=25)

    def __str__(self):
        return self.gender


class race(models.Model):
    race = models.CharField(max_length=50)

    def __str__(self):
        return self.race


class ethnicity(models.Model):
    ethnicity = models.CharField(max_length=100)

    def __str__(self):
        return self.ethnicity


class education(models.Model):
    education = models.CharField(max_length=100)

    def __str__(self):
        return self.education


class religion(models.Model):
    religion = models.CharField(max_length=100)

    def __str__(self):
        return self.religion


class politics(models.Model):
    politics = models.CharField(max_length=100)

    def __str__(self):
        return self.politics


class polideology(models.Model):
    politicalideology = models.CharField(max_length=100)

    def __str__(self):
        return self.politicalideology


class age(models.Model):
    age = models.CharField(max_length=25)

    def __str__(self):
        return self.age


class income(models.Model):
    income = models.CharField(max_length=25)

    def __str__(self):
        return self.income


class usregion(models.Model):
    usregion = models.CharField(max_length=100)

    def __str__(self):
        return self.usregion


class usstates(models.Model):
    usstate = models.CharField(max_length=50)

    def __str__(self):
        return self.usstate


class User(AbstractBaseUser, PermissionsMixin):
    # Custom user model that supports using email instead of username.
    email = models.EmailField(max_length=255,
                              unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    profile_locked = models.BooleanField(default=0)
    profile_pic = models.ImageField(upload_to='profile_pics',
                                    blank=True)
    gender = models.ForeignKey(gender,
                               null=True,
                               default=None,
                               on_delete=models.CASCADE)
    race = models.ForeignKey(race,
                             null=True,
                             default=None,
                             on_delete=models.CASCADE)
    ethnicity = models.ForeignKey(ethnicity,
                                  null=True,
                                  default=None,
                                  on_delete=models.CASCADE)
    education = models.ForeignKey(education,
                                  null=True,
                                  default=None,
                                  on_delete=models.CASCADE)
    religion = models.ForeignKey(religion,
                                 null=True,
                                 default=None,
                                 on_delete=models.CASCADE)
    politics = models.ForeignKey(politics,
                                 null=True,
                                 default=None,
                                 on_delete=models.CASCADE)
    age = models.ForeignKey(age,
                            null=True,
                            default=None,
                            on_delete=models.CASCADE)
    income = models.ForeignKey(income,
                               null=True,
                               default=None,
                               on_delete=models.CASCADE)
    politicalideology = models.ForeignKey(polideology,
                                          null=True,
                                          default=None,
                                          on_delete=models.CASCADE)
    usregion = models.ForeignKey(usregion,
                                 null=True,
                                 default=None,
                                 on_delete=models.CASCADE)
    usstate = models.ForeignKey(usstates,
                                null=True,
                                default=None,
                                on_delete=models.CASCADE)

    objects = UserManager()

    USERNAME_FIELD = 'email'

class category(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    category = models.CharField(max_length=256)

    def __str__(self):
        return self.category


class subcategory(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    subcategory = models.CharField(max_length=256)

    def __str__(self):
        return self.subcategory


class questions(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(subcategory, on_delete=models.CASCADE)
    question_name = models.CharField(max_length=256)
    question = models.TextField()
    can_change_answer = models.BooleanField(default=True)
    choice_a = models.CharField(max_length=32, default="Yes")
    choice_b = models.CharField(max_length=32, default="No")

    def __str__(self):
        return self.question_name


class answers(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    question = models.ForeignKey(questions, on_delete=models.CASCADE)
    answer_date_time = models.DateTimeField(auto_now_add=True)  # changed to auto_now_add.
    answer = models.CharField(max_length=32)

    class Meta:
        unique_together = (('id', 'user', 'question', 'answer_date_time'),)

    def __str__(self):
        return self.answer