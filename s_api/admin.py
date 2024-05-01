from django.contrib import admin
from s_api.models import StudentAuthCredential

# Register your models here.
class StudentAuthCredentialAdmin(admin.ModelAdmin):
    list_display=('s_id','s_secret')
admin.site.register(StudentAuthCredential,StudentAuthCredentialAdmin)
