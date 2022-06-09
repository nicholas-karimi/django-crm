from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages 
from django.views.generic import (TemplateView, UpdateView, 
                                    CreateView ,ListView, DetailView, DeleteView)

from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm, RegistrationForm


# clas based views 
#CRUD+L -> Create, Retrieve, Update, and Delete + List
class RegistrationView(CreateView):
    template_name = 'registration/signup.html'
    form_class = RegistrationForm

    def get_success_url(self) -> str:
        return reverse('login')

class IndexPageList(TemplateView):
    template_name = 'landing.html'

def index(request):
    return render(request, 'landing.html')

class LeadListView(ListView):
    template_name = 'leads/leads_list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads' #-> customize context instad of 
                                        #using default object_list provided by the ListView()

def leads_list(request):
    leads = Lead.objects.all()

    return render(request, 'leads/leads_list.html', {'title': 'Home', "leads": leads})

class leadDetailView(DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'

def lead_detail(request, pk):
    lead = get_object_or_404(Lead, id=pk)
    return render(request, 'leads/lead_detail.html',
                             {'title': 'Lead Detail', 'lead': lead})


class LeadCreateView(CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self) -> str:
        return reverse('leads:leads')

    def form_valid(self, form):
        # send mail on lead creation

        send_mail(
            subject= " A lead has been created!",
            message=" Visit the site to see the new lead",
            from_email="lead@crmpro.com",
            recipient_list=["nicholaskarimi.dev@gmail.com"]
        )
        return super(LeadCreateView, self).form_valid(form)

def lead_create(request):

    # print(request.POST)
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            # new_lead = form.save()
            # print("The form is valid")
            # print(form.cleaned_data)
            form.save()
            messages.success(request, "Lead created successfully!")
            return redirect('leads:leads')
    context = {
        "title": 'Add Lead',
        "form": form
    }
    return render(request, 'leads/lead_create.html', context)

class LeadUpdateView(UpdateView):
    template_name = 'leads/update_lead.html'
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self) -> str:
        return reverse('leads:leads')


# using ModelForm
def lead_update(request, pk):
    lead = get_object_or_404(Lead, id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('leads:leads')


    context = {
        "title": "Update Lead",
        "lead": lead,
        "form": form
    }
    return render(request, "leads/update_lead.html", context)

class LeadDeleteView(DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self) -> str:
        return reverse('leads:leads')

def delete_lead(request, pk):
    lead = get_object_or_404(Lead, id=pk)
    lead.delete()
    messages.success(request, "Lead deleted successfully!")
    return redirect('leads:leads')

# def lead_update(request, lead_id):
#     lead = get_object_or_404(Lead, id=lead_id)
#     form =  LeadForm()
#     if request.method == 'POST':
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             # update
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age 
#             lead.save()

#     context = {
#         "title": "Update Lead",
#         "lead": lead,
#         "form": form
#     }
#     return render(request, "leads/update_lead.html", context)


# def lead_create(request):
    
#     # print(request.POST)
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             # new_lead = form.save()
#             print("The form is valid")
#             print(form.cleaned_data)
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()

#             new_lead = Lead.objects.create(
#                 first_name = first_name,
#                 last_name = last_name,
#                 age = age,
#                 agent = agent
#             )
#             print("The lead has been created")
#             messages.success(request, "Lead created successfully!")
#             return redirect('leads:leads')
#     context = {
#         "title": 'Add Lead',
#         "form": form
#     }