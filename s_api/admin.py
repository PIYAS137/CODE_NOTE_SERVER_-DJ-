from django.contrib import admin
from s_api.models import StudentAuthCredential
from s_api.models import CodeModel

# Register your models here.
class StudentAuthCredentialAdmin(admin.ModelAdmin):
    list_display=('s_id','s_secret')

class CodeModelAdmin(admin.ModelAdmin):
    list_display=('s_id','s_secret','title','code','date','course','c_id')

admin.site.register(StudentAuthCredential,StudentAuthCredentialAdmin)
admin.site.register(CodeModel,CodeModelAdmin)
