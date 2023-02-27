
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.backends import UserModel
from backend.models import Profile, Item
from django.contrib.auth import authenticate, login as auth_login



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


@csrf_exempt
def register_dummy():
    
        
        
        username = "aaa"
        password1 = "adit"
        password2 = "adit"
        
        
        
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

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Redirect to a success page.
            return JsonResponse({
                "status": True,
                "message": "Successfully Logged In!"
                # Insert any extra data if you want to pass data to Flutter
                }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Failed to Login, Account Disabled."
                }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Failed to Login, check your email/password."
            }, status=401)

# CRUD

@csrf_exempt
def add(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        
        title = data["title"]
        description = data["description"]
        image_link = data["image_link"]
        
        try:
            Item.objects.get(title=title, image_link=image_link)
            return JsonResponse({"status": "dup"}, status=401)
        except:
            addItem = Item.objects.create(
            title = title, 
            description = description,
            image_link = image_link
            )

            addItem.save()

        
            return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def favorite(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        print(data)

        title = data["title"]
        description = data["description"]
        image_link = data["imageLink"]
        

        item = Item.objects.get(title=title, image_link=image_link, description = description)
        print(item.favorite)
        item.favorite = not item.favorite
        print(item.favorite)
        item.save()
        
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
    data = serializers.serialize('json', Item.objects.all())
    return HttpResponse(data, content_type="application/json")