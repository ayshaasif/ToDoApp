from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse,get_object_or_404
from .models import Reminder
from .forms import ReminderForm
from django.views import View


# Create your views here.
def home(request):
    return render(request,'todo/base.html',{})


def showReminders(request):
    objs = Reminder.objects.all()
    template_name = 'todo/display.html'
    search_input = request.GET.get('search') or ''

    context = {
         'reminders': objs,
         'search_input':search_input
    }
    if search_input:
        context['reminders'] = Reminder.objects.filter(Name__icontains=search_input)
    elif (search_input not in objs and search_input != ''):
        return HttpResponse('No such Reminder - try with some other key word')

    return render(request,template_name,context)



def createReminders(request):
         form = ReminderForm(request.POST or None)
         if request.method == 'POST':
             if form.is_valid():
                 form.save()
                 print(form.cleaned_data)
         form = ReminderForm()
         context = {
             'form':form
         }
         template_name = 'todo/forms.html'
         return render(request,template_name,context)



def filterReminder(request,post_id):
    object = Reminder.objects.filter(id=post_id)
    if len(object) == 0:
        return redirect('showReminder')
    print(object)
    context = {
        'reminders': object
    }
    template_name = 'todo/display.html'
    return render(request, template_name, context)


def deleteReminder(request):
    objects = Reminder.objects.all()
    if request.method == 'POST':  # <- Checking for method type
        id_list = request.POST.getlist('remind')
        print(id_list)
        # This will submit an array of the value attributes of all the
        # checkboxes that have been checked, that is an array of {{obj.id}}
        # Now all that is left is to iterate over the array fetch the
        # object with the ID and delete it.
        if len(id_list)>0:
            for rem in id_list:
                Reminder.objects.get(id = rem).delete()
            return redirect('showReminder')
    context = {
        'reminders': objects
    }
    template_name = 'todo/display.html'
    return render(request,template_name,context)


def updateReminder(request, pk):
       obj = Reminder.objects.get(id = pk)
       form = ReminderForm(instance=obj)
       if request.method == 'POST':
           form = ReminderForm(request.POST, instance=obj)
           if form.is_valid():
               form.save()
           return redirect('/todo/display')
       template_name = 'todo/forms.html'
       context = {
           'form':form
       }
       return render(request,template_name,context)







