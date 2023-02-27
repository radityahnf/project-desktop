
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.backends import UserModel
from models import Profile, API



import json

# Create your views here.

# Authentication
@csrf_exempt
def register(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        
        username = data["username"]
        password1 = data["password1"]
        password2 = data["password2"]
        
        username = data["username"]
        
        if UserModel.objects.filter(username=username).exists():
            return JsonResponse({"status": "duplicate"}, status=401)

        if password1 != password2:
            return JsonResponse({"status": "pass failed"}, status=401)

        createUser = UserModel.objects.create_user(
        username = username, 
        password = password1,
        )

        createUser.save()
        newUser = Profile.objects.create(
        user = createUser, 
        username = username
        )

        newUser.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)





# CRUD

@csrf_exempt
def add(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        
        name = data["name"]
        description = data["description"]
        link_website = data["link_website"]
        id = data["id"]
        try:
            API.objects.get(name=name, link_website=link_website)
            return JsonResponse({"status": "dup"}, status=401)
        except:
            addAPI = API.objects.create(
            name = name, 
            description = description,
            link_website = link_website
            )

            addAPI.save()

        
            return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def delete(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        
        name = data["name"]

        link_website = data["link_website"]
        id = data["id"]

        API.objects.delete(name=name, link_website=link_website, id=id)
        
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def update(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        
        name = data["name"]

        description = data["description"]
        id = data["id"]

        data = API.objects.get(id=id)

        data.name = name
        data.description = description

        data.save()
        
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

def show_json(request):
    data = serializers.serialize('json', API.objects.all())
    return HttpResponse(data, content_type="application/json")