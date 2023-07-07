from django.db import models

# Create your models here.
class caditate_signup(models.Model):
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    #description = models.TextField()
    class Meta:
        db_table = "student_profiles"
    def __str__(self):
        return self.firstname


class Candidate(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    skills = models.CharField(max_length=200)
    jr_number = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    current_company = models.CharField(max_length=100)
    total_experience = models.FloatField()
    ctc = models.FloatField()
    expected_ctc = models.FloatField()
    offers_in_hand = models.IntegerField()
    notice_period = models.IntegerField()
    current_location = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    screening_status = models.CharField(max_length=100)
    screened_by = models.CharField(max_length=100)
    source_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Cse(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    skills = models.CharField(max_length=200)
    jr_number = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    current_company = models.CharField(max_length=100)
    total_experience = models.FloatField()
    ctc = models.FloatField()
    expected_ctc = models.FloatField()
    offers_in_hand = models.IntegerField()
    notice_period = models.IntegerField()
    current_location = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    screening_status = models.CharField(max_length=100)
    screened_by = models.CharField(max_length=100)
    source_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Civil(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    skills = models.CharField(max_length=200)
    jr_number = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    current_company = models.CharField(max_length=100)
    total_experience = models.FloatField()
    ctc = models.FloatField()
    expected_ctc = models.FloatField()
    offers_in_hand = models.IntegerField()
    notice_period = models.IntegerField()
    current_location = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    screening_status = models.CharField(max_length=100)
    screened_by = models.CharField(max_length=100)
    source_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Mechanical(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    skills = models.CharField(max_length=200)
    jr_number = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    current_company = models.CharField(max_length=100)
    total_experience = models.FloatField()
    ctc = models.FloatField()
    expected_ctc = models.FloatField()
    offers_in_hand = models.IntegerField()
    notice_period = models.IntegerField()
    current_location = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    screening_status = models.CharField(max_length=100)
    screened_by = models.CharField(max_length=100)
    source_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Eee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    skills = models.CharField(max_length=200)
    jr_number = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    current_company = models.CharField(max_length=100)
    total_experience = models.FloatField()
    ctc = models.FloatField()
    expected_ctc = models.FloatField()
    offers_in_hand = models.IntegerField()
    notice_period = models.IntegerField()
    current_location = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    screening_status = models.CharField(max_length=100)
    screened_by = models.CharField(max_length=100)
    source_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Ece(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    skills = models.CharField(max_length=200)
    jr_number = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    current_company = models.CharField(max_length=100)
    total_experience = models.FloatField()
    ctc = models.FloatField()
    expected_ctc = models.FloatField()
    offers_in_hand = models.IntegerField()
    notice_period = models.IntegerField()
    current_location = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    screening_status = models.CharField(max_length=100)
    screened_by = models.CharField(max_length=100)
    source_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')

    def get_file_url(self):
        return self.file.url

class profiles(models.Model):
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    #description = models.TextField()
    class Meta:
        db_table = "profiles"
    def __str__(self):
        return self.firstname


