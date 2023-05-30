from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
  nationalities = [
    ('Za', 'Zambian'),
    ('MA', 'Malawian'),
    ('So', 'South African'),
    ('Zi', 'Zimbabwean'),
    ('Co', 'Congolis'),
    ('In', 'Indian'),
    ('Ch', 'Chinese'),
    ('Mo', 'Moroccan'),
    ('Bo', 'Botswanan'),
    ('Ni', 'Nigerian'),
  ]
  hostels = [
    ('Ka', 'Kalingalinga'),
    ('Ti', 'Tiyende Pamodzi'),
    ('So', 'Soweto'),
    ('Ka', 'Kafue'),
    ('Oc', 'October'),
    ('Za', 'Zambezi'),
    ('In', 'International'),
    ('Pr', 'President'),
    ('Kw', 'Kwacha'),
    ('Af', 'Africa'),
    ('VE', 'VET'),
    ('Le', 'Levy Mwanawasa'),
  ]
  schools = [
    ('Na', 'Natural Sciences'),
    ('Ag', 'Agricultural Sciences'),
    ('Mi', 'Mines'),
    ('Ed', 'Education'),
    ('Hu', 'Humaninities and Social Sciences'),
    ('En', 'Engineering'),
    ('Ve', 'Vetnery Medicine'),
    ('Co', 'Confucius Studies'),
    ('La', 'Law'),
  ]
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  phone_number = models.CharField(max_length=12)
  bio = models.CharField(max_length=150, help_text="Enter a brief description of yourself", null=True)
  # gender
  date_of_birth = models.DateField()
  nationality = models.CharField(max_length=2, choices=nationalities, default="Za")
  hostel = models.CharField(max_length=2, choices=hostels, default="Ka")
  school = models.CharField(max_length=2, choices=schools, default="Na")
  program = models.CharField(max_length=100)
  year = models.CharField(max_length=5)
  owner = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
  profile_photo = models.ImageField(default='default.jpg', blank=True, null=True, upload_to="profile_pictures/")
  # add in thumbnail later
  # add in author later

  def __str__(self):
        return self.first_name + " " + self.last_name
  