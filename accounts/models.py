from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from autoslug import AutoSlugField
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

ACC_TYPE = (
	('buyer', 'Buyer'),
	('personal seller', 'Personal Seller'),
	('business', 'Business'),

)
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=300, null=True,  blank=True)
	quater = models.CharField(max_length=200, null=True,  blank=True)
	country = models.CharField(max_length=100, null=True,  blank=True)
	region = models.CharField(max_length=256, null=True,  blank=True)
	town = models.CharField(max_length=256, null=True,  blank=True)
	store_address = models.CharField(max_length=256, null=True,  blank=True)
	phone_number = models.IntegerField(null=True,  blank=True)
	profile_pic = models.ImageField(upload_to='profile_img', default='default.png')
	verified = models.BooleanField(default=False)
	account_type = models.CharField(max_length=256, choices=ACC_TYPE, null=True, blank=True)
	date_of_birth = models.DateField(default=now)
	sponsored = models.BooleanField(default=False)
	view_count = models.PositiveIntegerField(default=0)
	favourite = models.ManyToManyField(
        User, related_name='saved_user', blank=True)
	joined_on = models.DateTimeField(auto_now_add=True)
	
	@property
	def total_likes(self):
		return self.favourite.count()
		
	def __str__(self):
		return self.user.username + " profile"

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		image = Image.open(self.profile_pic.path)
		if image.height > 200 or image.width > 200:
			output_size = (300, 300)
			image.thumbnail(output_size)
			image.save(self.profile_pic.path)
	
	def get_absolute_url(self):
		return "/p/%i/" % self.id


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.userprofile.save()


@receiver(post_save, sender=User)
def save_emailaddress(sender, instance, **kwargs):
    instance.userprofile.save()

DOC = (
    ('passport', 'Passport'),
    ('national ID', 'National ID Card'),
    ('others', 'Others')
)

STA = (
    ('complete', 'complete'),
    ('in progress', 'in progress'),
    ('canceled', 'canceled')
)

class Verification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    document_type = models.CharField(
        max_length=50, choices=DOC, default='national ID')
    number = models.CharField(max_length=50)
    photo_back = models.ImageField(upload_to='verification')
    photo_front = models.ImageField(upload_to='verification')
    is_verified = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=STA)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + ' verification'