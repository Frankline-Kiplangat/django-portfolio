# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def about_me(request):
    return render(request, 'about.html')


