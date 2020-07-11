from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

NID_regex = RegexValidator(regex=r'^(\d{14})$',
                           message="National ID must be entered exactly 14 digits.")

Mobile_regex = RegexValidator(regex=r'^(\d{11})$',
                              message="Mobile Number must be entered exactly 11 digits.")

DSL_regex = RegexValidator(regex=r'^(\d{10})$',
                           message="DSL Number must be entered exactly 10 digits.")


class Employee(models.Model):

    NID = models.CharField(validators=[NID_regex], max_length=14, unique=True)
    Name = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    Proof = models.FileField(upload_to='images')
    Birthdate = models.DateField()
    jobDesc = models.TextField(max_length=200)
    Mobile = models.CharField(
        validators=[Mobile_regex], max_length=11, unique=True)
    DSL = models.CharField(
        validators=[DSL_regex], max_length=10, blank=True, null=True)
    Avatar = models.FileField(upload_to='images')

    def __str__(self):
        return self.Name


class Requests(models.Model):
    Request = 'request'
    Complaint = 'complaint'

    Title = models.CharField(max_length=200)
    Desc = models.TextField(max_length=250)
    state_choices = [
        (Request, 'request'),
        (Complaint, 'complaint')
    ]
    Type = models.CharField(
        max_length=9, choices=state_choices, default=Request)
    created_date = models.DateTimeField(default=timezone.now)
    Replied = models.BooleanField(default=False, blank=True, null=True)
    Action = models.TextField(max_length=250, blank=True, null=True)
    Email = models.EmailField(blank=True, null=True)
    Mobile = models.CharField(validators=[Mobile_regex], max_length=11)

    def __str__(self):
        return self.Title


class Existence(models.Model):
    enter = 'enter'
    exitt = 'exit'

    Name = models.CharField(max_length=250)
    state_choices = [
        (enter, 'Enter'),
        (exitt, 'Exit')
    ]
    Type = models.CharField(max_length=5, choices=state_choices, default=enter)
    Timing = models.DateTimeField(default=timezone.now)
    NID = models.CharField(validators=[NID_regex], max_length=14)

    def __str__(self):
        return self.Name


class Admin(models.Model):

    NID = models.CharField(validators=[NID_regex], max_length=14, unique=True)
    Username = models.CharField(max_length=50, unique=True)
    Password = models.CharField(max_length=20)
    Name = models.CharField(max_length=150)
    Registered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Username


class Offer(models.Model):
    installment = 'تقسيط'
    cash = 'كاش'

    admin = models.ForeignKey(
        Admin, on_delete=models.CASCADE, related_name="offer_owner")
    Title = models.CharField(max_length=200)
    Desc = models.TextField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)
    state_choices = [
        (installment, 'تقسيط'),
        (cash, 'كاش')
    ]
    Installement = models.CharField(
        max_length=12, choices=state_choices, default=installment)
    Cost = models.FloatField(max_length=8)
    minPayment = models.FloatField(max_length=8, blank=True, null=True)
    Duration = models.IntegerField(blank=True, null=True)
    Avatar = models.FileField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.Title


class News(models.Model):

    admin = models.ForeignKey(
        Admin, on_delete=models.CASCADE, related_name="news_owner")
    Title = models.CharField(max_length=200)
    Desc = models.TextField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)
    Avatar = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.Title


class Owner(models.Model):

    Own = 'own'
    Rent = 'rent'
    NID = models.CharField(validators=[NID_regex], max_length=14, unique=True)
    Name = models.CharField(max_length=200)
    Proof = models.FileField(upload_to='images', null=True)
    Birthdate = models.DateField()
    Mobile = models.CharField(
        validators=[Mobile_regex], max_length=11, unique=True)
    DSL = models.CharField(
        validators=[DSL_regex], max_length=10, blank=True, null=True)
    Avatar = models.ImageField(upload_to='images', null=True)
    Notes = models.TextField(max_length=200, blank=True, null=True)
    state_choices = [
        (Own, 'own'),
        (Rent, 'rent')
    ]
    Type = models.CharField(
        max_length=12, choices=state_choices, default=Own)

    def __str__(self):
        return "Name : " + self.Name + ' , ' + "ID : " + str(self.id)


class Compound(models.Model):

    Name = models.CharField(max_length=100, unique=True)
    Number = models.IntegerField(unique=True, null=True)
    Address = models.CharField(max_length=200)
    Latitude = models.FloatField(max_length=10, unique=True)
    Longitude = models.FloatField(max_length=10, unique=True)
    Area = models.FloatField(max_length=8)
    Desc = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.Name


class Block(models.Model):

    compound = models.ForeignKey(
        Compound, on_delete=models.CASCADE, related_name="compound_block")
    Number = models.IntegerField(unique=True, null=True)
    Area = models.FloatField(max_length=8)
    Desc = models.TextField(max_length=300, blank=True, null=True)
    towersNumber = models.IntegerField(blank=True, null=True)

    class Meta:
        unique_together = ['compound', 'Number']

    def __str__(self):
        return "Compound : " + self.compound.Name + " Block : " + str(self.id)


class Tower(models.Model):

    Residential = 'residential'
    Commercial = 'commercial'

    block = models.ForeignKey(
        Block, on_delete=models.CASCADE, related_name="block_tower")
    Name = models.CharField(max_length=100, blank=True, null=True)
    Number = models.IntegerField(unique=True, null=True)
    Area = models.FloatField(max_length=8)
    flatsNumber = models.IntegerField(null=True)
    Cost = models.FloatField(max_length=8)
    Notes = models.TextField(max_length=200, null=True)
    floorsNumber = models.IntegerField()
    storesNumber = models.IntegerField()
    Number = models.IntegerField(default=2)
    state_choices = [
        (Residential, 'Residential'),
        (Commercial, 'Commercial')
    ]
    Type = models.CharField(
        max_length=12, choices=state_choices, default=Residential)
    owner = models.ForeignKey(
        Owner, on_delete=models.CASCADE, related_name="owner_tower", null=True)

    class Meta:
        unique_together = ['block', 'Number']

    def __str__(self):
        return "Block : " + str(self.block.Number) + " Tower : " + str(self.Number)


class Flat(models.Model):

    owner = models.ForeignKey(
        Owner, on_delete=models.CASCADE, related_name="owner_flat", null=True)
    tower = models.ForeignKey(
        Tower, on_delete=models.CASCADE, related_name="tower_flat")
    Number = models.IntegerField(unique=True, default=2)
    floorNumber = models.IntegerField()
    Area = models.FloatField(max_length=8)
    Inhabited = models.BooleanField(default=False)

    class Meta:
        unique_together = ['Number', 'tower']

    def __str__(self):
        return "Owner : " + self.owner.Name + " Tower : " + str(self.tower.id) + " Flat : " + str(self.Number)


class Store(models.Model):

    Gym = 'gym'
    Restaurant = 'restaurant'
    Cafe = 'cafe'
    Shop = 'shop'
    Mall = 'mall'

    tower = models.ForeignKey(
        Tower, on_delete=models.CASCADE, related_name="tower_store")
    Number = models.IntegerField(unique=True, null=True)
    floorNumber = models.IntegerField(null=True)
    Name = models.CharField(max_length=100)
    Desc = models.TextField(max_length=300)
    state_choices = [
        (Shop, 'shop'),
        (Restaurant, 'restaurant'),
        (Cafe, 'cafe'),
        (Gym, 'gym'),
        (Mall, 'mall')
    ]
    Type = models.CharField(
        max_length=12, choices=state_choices, default='shop')
    owners = models.ManyToManyField(
        Owner,
        through='ownershipStore'
    )

    class Meta:
        unique_together = ['tower', 'Number']

    def __str__(self):
        return self.Name


class ownershipStore(models.Model):

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['owner', 'store']

    def __str__(self):
        return "Owner : " + self.owner.Name + " Store : " + self.store.Name


class Family(models.Model):

    Wife = 'wife'
    Son = 'son'
    Daughter = 'daughter'
    Cousin = 'cousin'
    Husband = 'husband'
    Friend = 'friend'
    Father = 'father'
    Mother = 'mother'
    Brother = 'brother'
    Sister = 'sister'
    Uncle = 'uncle'
    Aunt = 'aunt'

    owner = models.ForeignKey(
        Owner, on_delete=models.CASCADE, related_name="delete_family")
    Name = models.CharField(max_length=150)
    Birthdate = models.DateField()
    relation_choices = [
        (Wife, 'Wife'),
        (Son, 'Son'),
        (Daughter, 'Daughter'),
        (Cousin, 'Cousin'),
        (Husband, 'Husband'),
        (Friend, 'friend'),
        (Father, 'father'),
        (Mother, 'mother'),
        (Uncle, 'uncle'),
        (Aunt, 'aunt'),
        (Brother, 'brother'),
        (Sister, 'sister')
    ]
    Relationship = models.CharField(
        max_length=9, choices=relation_choices, default=Wife)
    Proof = models.FileField(upload_to='images', null=True)
    NID = models.CharField(
        validators=[NID_regex], max_length=14, unique=True, null=True)

    class Meta:
        unique_together = ['owner', 'NID']

    def __str__(self):
        return self.Name
