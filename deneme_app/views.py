from django.shortcuts import render
from django.http import HttpResponse
from deneme_app.models import User
# Create your views here.

def input(request):
    return HttpResponse("Http response ile yapıldı")

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'user': user_list}
    return render(request,'deneme_app/user.html',context=user_dict)
