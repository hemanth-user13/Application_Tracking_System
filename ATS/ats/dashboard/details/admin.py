from django.contrib import admin

# Register your models here.
from .models import UploadedFile
admin.site.register(UploadedFile)
from .models import caditate_signup
admin.site.register(caditate_signup)
#
from .models import Candidate
admin.site.register(Candidate)
from .models import Cse
admin.site.register(Cse)
from .models import Civil
admin.site.register(Civil)
from .models import Mechanical
admin.site.register(Mechanical)
from .models import Eee
admin.site.register(Eee)
from .models import Ece
admin.site.register(Ece)
from .models import profiles
admin.site.register(profiles)