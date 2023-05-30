from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
  nationalities = [
    ('Zambian', 'Zambian'),
    ('Malawian', 'Malawian'),
    ('South African', 'South African'),
    ('Zimbabwean', 'Zimbabwean'),
    ('Congolis', 'Congolis'),
    ('Indian', 'Indian'),
    ('Chinese', 'Chinese'),
    ('Moroccan', 'Moroccan'),
    ('Botswanan', 'Botswanan'),
    ('Nigerian', 'Nigerian'),
  ]
  hostels = [
    ('Kalingalinga', 'Kalingalinga'),
    ('Tiyende Pamodzi', 'Tiyende Pamodzi'),
    ('Soweto', 'Soweto'),
    ('Kafue', 'Kafue'),
    ('October', 'October'),
    ('Zambezi', 'Zambezi'),
    ('International', 'International'),
    ('President', 'President'),
    ('Kwacha', 'Kwacha'),
    ('Africa', 'Africa'),
    ('VET', 'VET'),
    ('Levy Mwanawas', 'Levy Mwanawasa'),
  ]
  schools = [
    ('Natural Sciences', 'Natural Sciences'),
    ('Agricultural Sciences', 'Agricultural Sciences'),
    ('Mines', 'Mines'),
    ('Education', 'Education'),
    ('Humaninities and Social Sciences', 'Humaninities and Social Sciences'),
    ('Engineering', 'Engineering'),
    ('Vetnery Medicine', 'Vetnery Medicine'),
    ('Confucius Studies', 'Confucius Studies'),
    ('Law', 'Law'),
  ]
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  phone_number = models.CharField(max_length=12)
  bio = models.CharField(max_length=150, help_text="Enter a brief description of yourself", null=True)
  # gender
  date_of_birth = models.DateField()
  nationality = models.CharField(max_length=50, choices=nationalities, default="Za")
  hostel = models.CharField(max_length=50, choices=hostels, default="Ka")
  school = models.CharField(max_length=50, choices=schools, default="Na")
  program = models.CharField(max_length=100)
  year = models.CharField(max_length=5)
  owner = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
  profile_photo = models.ImageField(default='default.jpg', blank=True, null=True, upload_to="profile_pictures/")
  # add in thumbnail later
  # add in author later

  def __str__(self):
        return self.first_name + " " + self.last_name
  