from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages 

from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm

def index(request):
    return render(request, 'landing.html')

def leads_list(request):
    leads = Lead.objects.all()

    return render(request, 'leads/leads_list.html', {'title': 'Home', "leads": leads})


def lead_detail(request, pk):
    lead = get_object_or_404(Lead, id=pk)
    return render(request, 'leads/lead_detail.html',
                             {'title': 'Lead Detail', 'lead': lead})


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