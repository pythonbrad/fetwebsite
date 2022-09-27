from django.shortcuts import render, redirect
from .models import ProgramGroup, Building
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
	return render(request, 'core/index.html')

def message_dean(request):
	return render(request, 'core/message_dean.html')

def about_us(request):
	return render(request, 'core/about_us.html')

def contact_us(request):
	buildings = Building.objects.all()
	return render(request, 'core/contact_us.html', {'buildings': buildings})

def departments_list(request):
	return render(request, 'core/departments_list.html')

def program_groups_list(request):
	return render(request, 'core/program_groups_list.html')

def program_group_detail(request, slug=None):
	if slug:
		program_group = get_object_or_404(ProgramGroup, slug=slug)
		return render(request, 'core/program_group_detail.html', {'program_group': program_group})
	else:
		return render(request, 'core/pre_eng_prog.html')

def department_detail(request, slug):
	return redirect('/')

def student_ressources(request):
	return render(request, 'core/student_ressources.html')
