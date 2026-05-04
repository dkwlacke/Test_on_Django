from django.shortcuts import render
from .models import User


def all_db(request):
	value = ''
	obj_list = User.objects.values('name')

	return render(request, './sql_template.html', {'obj_list':obj_list, 'value':value})

def search(request):
	res = list()
	if request.method == "POST":
		name = request.POST.get('search')
		res = User.objects.filter(name__icontains=name)

	return render(request,"search.html", {'result': res})
