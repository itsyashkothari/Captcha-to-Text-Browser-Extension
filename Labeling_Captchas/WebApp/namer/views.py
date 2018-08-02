from django.shortcuts import render
from django.template import loader
from django.contrib.auth.models import User
from .models import Image,Profile
from django.http import HttpResponse
import os
from os import listdir
from os.path import isfile, join
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views import generic
import numpy as np
import re
from django.shortcuts import redirect,reverse
from django.contrib.auth import authenticate, login
# Create your views here.
def search2(request):
	return render(request, 'namer/love.html',)
def search(request):
	# Activating Profile of User
	player, created = Profile.objects.get_or_create(user=request.user)
	# checks if input value is valid
	checker = re.compile("^[.a-zA-Z0-9]$")
	print(request.user)
	print("search")
	if request.method == 'POST':
		val = request.POST.get('val')
		fn = request.POST.get('fn')
		print(fn +" is " +val)
		if checker.match(val):
			#Get the object by file name
			temp = Image.objects.get(file_name = fn)
			#Change the values
			temp.checked = True
			temp.value = val
			temp.solved_by = request.user
			print(temp.value)
			#Save the object
			temp.save(update_fields = ['value','checked','solved_by'])
			#Update and save the user count 
			request.user.profile.solved = request.user.profile.solved + 1
			request.user.profile.save()
			print('changed')
		else:
			print("not changed")
	'''	
#  	Set every image variable to default	
	t2 = Image.objects.filter(checked = True)
	for lw in t2:
		lw.value = 'yash'
		lw.checked = False
		lw.save(update_fields = ['value','checked'])
	'''
	
	notCheckedImages = Image.objects.filter(checked = False)
	if len(notCheckedImages)<22:
		render(request, 'namer/love.html')
	print(request.user.profile.solved)
	score ={}
	messages = ""
	if request.user.profile.solved >1:
		messages = "Yash loves you the most! Only you "+request.user.username +" <3"
	lq = len(Image.objects.filter(value = 'yash'))
	print(lq)
	lo = User.objects.all()[1:]
	for l in lo:
#		Set user count to 0
#		l.profile.solved = 0
#		l.profile.save(update_fields=['solved'])
		score[l.username]=l.profile.solved

	link = notCheckedImages[0].file_name
	context = {'piclink':link,'total':len(Image.objects.all()),'score':score,'msg' :messages,'not_done':	len(notCheckedImages)}
	return render(request, 'namer/form.html',context)
