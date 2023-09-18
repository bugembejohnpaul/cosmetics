from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage


# Create your views here.
def dashboard(request):
    context={
        "programs_count": TrainingProgram.objects.count(),
        "clients_count": Company.objects.count(),
        "trainers_count": Trainer.objects.count(),
        "training_request_count": Request.objects.count(),
    }
    return render(request, 'panel/dashboard.html', context)

# view for displaying registered clients/companies
def view_client(request):
    context={
        "clients": Company.objects.all()
    }
    return render(request, 'panel/company.html',context)

# view for adding a client or company
def add_client(request):
    if request.method == "POST":
        company_name = request.POST.get("company_name")
        company_location = request.POST.get("company_location")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        company_type = request.POST.get("company_type")

        profile_image = request.FILES.get('profile_image')

        client = Company.objects.create(
            company_name = company_name,
            company_location = company_location,
            phone_number = phone_number,
            email = email,
            company_type = company_type,
        )
        if profile_image:
            fs = FileSystemStorage()
            image_filename = fs.save(profile_image.name, profile_image)
            client.profile_image = image_filename

        client.save()
        messages.success(request,"Client registered successfully")
        return redirect("add_client")
    else:
        # add_company code 
        return render(request, 'panel/addclient.html')

#view for deleting a client
def delete_client(request):
    if request.method == "POST":
        company_id = request.POST.get("company_id") 
        this_client = Company.objects.filter(pk=company_id)

        this_client.delete()
        messages.success(request,"Client deleted successfully")
        return redirect("view_client")

# view for editing added client
def edit_client(request):
    if request.method == "POST":
        company_id = request.POST.get("company_id")
        company_name = request.POST.get("company_name")
        company_location = request.POST.get("company_location")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        company_type = request.POST.get("company_type")

        this_client = Company.objects.get(pk=company_id)

        if this_client:
            this_client.company_name = company_name
            this_client.company_location = company_location
            this_client.email = email
            this_client.phone_number = phone_number
            this_client.company_type = company_type
            this_client.save()
            messages.success(request,"Client edited successfully")
            return redirect("view_client")
        else:
            messages.success(request,"Client not edited")
            return redirect("view_client")

# view for adding a category
def add_programcategory(request):
    if request.method == "POST":
        category_name = request.POST.get("category_name")
        this_category = ProgramCategory.objects.filter(category_name=category_name)

        if this_category:
            messages.error(request,"Category already exists")
            return redirect("add_programcategory")
        
        else:
            program_category = ProgramCategory.objects.create(category_name=category_name)
            program_category.save
            messages.success(request, "Category has successfully been added")
            return redirect("add_programcategory")
    else:
        # add_programcategory Code
        context={
            "categories": ProgramCategory.objects.all()
        }
        return render(request, 'panel/program_category.html', context)

#view for deleting a category
def delete_category(request):
    if request.method == "POST":
        cat_id = request.POST.get("cat_id") 
        this_category = ProgramCategory.objects.filter(category_id=cat_id)

        this_category.delete()
        messages.success(request,"Category deleted successfully")
        return redirect("add_programcategory")

#view for editing category name
def edit_category(request):
    if request.method == "POST":
        cat_id = request.POST.get("cat_id")
        category_name = request.POST.get("category_name")

        this_category = ProgramCategory.objects.get(category_id=cat_id)
        this_category.category_name = category_name
        this_category.save()
        messages.success(request,"Category edited successfully")
        return redirect("add_programcategory")

# view for add a training program
def add_training_program(request):
    if request.method == "POST":
        program_name = request.POST.get("program_name")
        category_id = request.POST.get("category")  # Get the ID of the selected category
        duration = request.POST.get("duration")
        description = request.POST.get("description")

        try:
            # Try to get the ProgramCategory instance by its ID
            category = ProgramCategory.objects.get(pk=category_id)
        except ProgramCategory.DoesNotExist:
            category = None

        if category:
            program = TrainingProgram.objects.create(
                program_name=program_name,
                category=category,
                duration=duration,
                description=description,
            )
            program.save()
            messages.success(request, "Training program added successfully")
            return redirect("add_training_program")
        else:
            messages.error(request, "Invalid category selected")
            return redirect("add_training_program")

    else:
        # Load the categories for the form
        context = {
            "categories": ProgramCategory.objects.all()
        }
        return render(request, 'panel/add_training_program.html', context)


# view for training programs
def training_programs(request):
    context={
        "programs": TrainingProgram.objects.all(),
        "categories": ProgramCategory.objects.all()
    }
    return render(request, 'panel/training_program.html', context) 

# view for deleting a training program
def delete_program(request):
    if request.method == "POST":
        program_id = request.POST.get("program_id") 
        this_program = TrainingProgram.objects.filter(pk=program_id)

        this_program.delete()
        messages.success(request,"Training Program deleted successfully")
        return redirect("training_programs")

#view for editing a training program
def edit_program(request):
    if request.method == "POST":
        program_id = request.POST.get("program_id")
        program_name = request.POST.get("program_name")
        category = request.POST.get("category")
        duration = request.POST.get("duration")
        description = request.POST.get("description")

        this_program = TrainingProgram.objects.get(pk=program_id)
        category = ProgramCategory.objects.get(pk=category)
        if this_program:
            this_program.program_name = program_name
            this_program.category = category
            this_program.duration = duration
            this_program.description = description
            this_program.save()
            messages.success(request,"Training Program edited successfully")
            return redirect("training_programs")
        else:
            messages.success(request,"Training Program not edited")
            return redirect("training_programs")

def add_trainer(request):
    if request.method == "POST":
        trainer_name = request.POST.get("trainer_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        expertise = request.POST.get("expertise")

        profile_image = request.FILES.get('profile_image')

        trainer = Trainer.objects.create(
            trainer_name = trainer_name,
            email = email,
            phone_number = phone_number,
            expertise = expertise,
        )
        if profile_image:
            fs = FileSystemStorage()
            image_filename = fs.save(profile_image.name, profile_image)
            trainer.profile_image = image_filename

        trainer.save()
        messages.success(request,"Trainer registered successfully")
        return redirect("add_trainer")
    else:
        # trainers Code
        return render(request, 'panel/addtrainers.html')

# view for trainers
def trainers(request):
    context={
        "trainers": Trainer.objects.all()

    }
    return render(request, "panel/trainers.html", context)


#view for deleting a trainer
def delete_trainer(request):
    if request.method == "POST":
        trainer_id = request.POST.get("trainer_is") 
        this_trainer = Trainer.objects.filter(pk=trainer_id)

        this_trainer.delete()
        messages.success(request,"Trainer deleted successfully")
        return redirect("trainers")


#view for editing a trainer
def edit_trainer(request):
    if request.method == "POST":
        trainer_id = request.POST.get("trainer_id")
        trainer_name = request.POST.get("trainer_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        expertise = request.POST.get("expertise")

        this_trainer = Trainer.objects.get(pk=trainer_id)
        if this_trainer:
            this_trainer.trainer_name = trainer_name
            this_trainer.email = email
            this_trainer.phone_number = phone_number
            this_trainer.expertise = expertise
            this_trainer.save()
            messages.success(request,"Trainer edited successfully")
            return redirect("trainers")
        else:
            messages.success(request,"Trainer not edited")
            return redirect("trainers")

# view for displaying training requests
def trainers_requests(request):
    if request.method == "GET":
        return render(request, 'panel/trainers_requests.html')
    else:
        # trainers Code
        return render(request, 'panel/trainers_requests.html')