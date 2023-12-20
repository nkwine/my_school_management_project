from django.contrib import admin
from.models import User,secretary,student,teacher,management,dos,bursar
# Register your models here.

admin.site.register(User)
admin.site.register(teacher)
admin.site.register(secretary)
admin.site.register(student)
admin.site.register(dos)
admin.site.register(bursar)
admin.site.register(management)