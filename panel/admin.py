from django.contrib import admin
from .models import Trainer,Company,ProgramCategory,TrainingProgram,Request
admin.site.register(Trainer)
admin.site.register(Company)
admin.site.register(ProgramCategory)
admin.site.register(TrainingProgram)
admin.site.register(Request)

