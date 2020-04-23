from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    # phone_number = models.CharField(max_length=10, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    email = models.EmailField(max_length=150)
    signup_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Reservation(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    num = models.CharField(max_length=255, blank=True)
    date = models.DateField()
    time = models.TimeField()
    guests = models.SmallIntegerField()
    requests = models.TextField()


    def __str__(self):
        return self.name