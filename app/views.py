from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from .forms import ContactUsForm


def lessons(request):
    lessons_list = Lessons.objects.all()
    return render(request, 'index.html', {"lessons": lessons_list})


def class_details(request, id):
    class_item = Classes.objects.get(id=id)
    lesson = Lessons.objects.filter(cls_id=class_item.id).first()
    return render(request, 'learn-more.html', {"class_item": class_item, 'lesson': lesson})


def test(request):
    return render(request, 'test.html')

def contact_us(request):
    form = ContactUsForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,'Ձեր հարցումն հաջողությամբ ուղարկվել է')
            return redirect('contact_us')
        else:
            messages.error(request, 'Տեղի է ունեցել սխալ, փորձե՜ք, կրկին')
            return redirect('contact_us')
    return render(request, 'contacts.html')


# def gallery(request):
#
#     images = Gallery.objects.all().order_by('-id')
#     return render(request, 'gallery.html', {"images": images})
#
#
# def about_us(request):
#     abouts = AboutUs.objects.last()
#     lessons = Lessons.objects.filter(show_in_about_us=True)
#     return render(request, 'about.html', {"abouts": abouts, "lessons": lessons})