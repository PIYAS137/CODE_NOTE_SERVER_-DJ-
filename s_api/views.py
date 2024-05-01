
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from s_api.models import StudentAuthCredential
from s_api.serializers import StudentAuthCredential_Serializer
from rest_framework.renderers import JSONRenderer

# Create your views here.
@csrf_exempt

# Sign Up User==========================>
def SignUpUser(req):
    if req.method == 'POST':
        try:
            data = json.loads(req.body)
        except json.JSONDecodeError:
            return JsonResponse({"error":"Invalid Json Format"})
        
        serializedData = StudentAuthCredential_Serializer(data=data)
        
        if serializedData.is_valid():
            s_id = serializedData.validated_data.get('s_id')
            if StudentAuthCredential.objects.filter(s_id=s_id).exists():
                return JsonResponse({"error":"Already Exists"},status=400)
            else:
                serializedData.save()
                return JsonResponse({"status":"Successfully SignUp"})
        else:
            return JsonResponse(serializedData.errors,status=400)
    else:
        return JsonResponse({"error":"Method Not Allowed"},status=405)


# Login User===================================
def LoginUser(req,pk):
    try:
        student = StudentAuthCredential.objects.get(s_id=pk)
        serializer = StudentAuthCredential_Serializer(student)
        jsonData = JSONRenderer().render(serializer.data)
        return HttpResponse(jsonData,content_type="application/json")
    except:
        return JsonResponse({"error":"invalid credentials"},status=401)
    


# Get All User=================================>
def GetAllUser(req):
    x = StudentAuthCredential.objects.all()
    ser = StudentAuthCredential_Serializer(x,many=True)
    json_Data = JSONRenderer().render(ser.data)
    return HttpResponse(json_Data,content_type="application/json")


