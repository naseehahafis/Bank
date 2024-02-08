from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import JsonResponse
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('new_page')
        else:
            messages.info(request,"Invalid credentials")
            # return redirect('/')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')
                print("created")
        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        # Redirect to login page after successful registration
        return redirect('/')
    return render(request, 'register.html')

def new_page(request):
    # Handle form submission here
    if request.method == 'POST':
        # Process the form data
        # Display success message
        message = "Application accepted"
        return render(request, 'new_page.html', {'message': message})
    else:
        return render(request, 'new_page.html')
def wikipedia(request, district):
    # Your view logic here
    return render(request, 'wikipedia.html', {'district': district})
# In your views.py file


def get_branches(request):
    if request.method == 'GET' and 'district' in request.GET:
        district = request.GET['district']
        print(district)
        # Example: Retrieve branches from database based on the selected district
        if district == 'Kasaragod':
            branches = ['Kanhangad', 'Nileshwar', 'Manjeshwar']
        elif district == 'Kannur':
            branches = ['Karivellur', 'Thalipparamba', 'Talacheri']
        elif district == 'Calicut':
            branches = ['Koyilandi','Mukkam','xyz']
        elif district == 'Wayanad':
            branches = ['Kalpatta','Manathavadi','dca']
        elif district == 'Idukki':
            branches = ['Peerumedu','Munnar','sda']
        else:
            branches = []  # Default empty list if district not found

        # Return branches as JSON response
        return JsonResponse({'branches': branches})
    else:
        # Handle invalid or missing parameters
        return JsonResponse({'error': 'Invalid request'})




