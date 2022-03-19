from django.shortcuts import render

# Create your views here.
def service(req):
      context ={'service':'active'}

      return render(req, 'service/service.html',context)