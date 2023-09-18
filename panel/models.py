from django.db import models

# Model for Users
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200) 

    def __str__(self):
        return self.username

# Model for Program Category
class ProgramCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'ProgramCategories'

    def __str__(self):
        return self.category_name

# Model for Training Programs
class TrainingProgram(models.Model):
    program_id = models.AutoField(primary_key=True)
    program_name = models.CharField(max_length=200)
    category = models.ForeignKey(ProgramCategory, on_delete=models.CASCADE)
    duration = models.IntegerField()  # Duration in days
    description = models.CharField(max_length=250)
    def __str__(self):
        return self.program_name

# Model for Trainers
class Trainer(models.Model):
    trainer_id = models.AutoField(primary_key=True)
    trainer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    expertise = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='trainer_profiles/')

    def __str__(self):
        return self.trainer_name

# Model for Companies
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=200)
    company_location = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    company_type = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='company_profiles/')

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.company_name

# Model for Requests
class Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    training_program = models.ForeignKey(TrainingProgram, on_delete=models.CASCADE)
    trainer = models.ManyToManyField(Trainer)
    date_of_training = models.DateField()
    




