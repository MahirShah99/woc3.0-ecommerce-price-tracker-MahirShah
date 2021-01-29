from django.shortcuts import render
from django.http import HttpResponse
from .forms import AmazonForm
from Scripts.selenium_amazon import webScrapAmazon
from Scripts.send_email import send_email

# Create your views here.
def amazonscrap(request):
    form = AmazonForm()
    
    if request.method == "POST":
        form = AmazonForm(request.POST)

        if form.is_valid():
            url = form.cleaned_data['url']
            desired_price = form.cleaned_data['desired_price']
            email = form.cleaned_data['email']
            # print("Url:- ",url_get)
            # print("Price:- ", desired_price)
            # print("Email:- ", email)

            data = webScrapAmazon(url, desired_price, email)

            if(data['status'] == True):
                send_email(data)
            
            form.save(commit=True)
            return render(request, 'result.html', context={"data": data})
        else:
            print("Error")
        
    return render(request, 'amazon/amazonscrap.html', {"form": form})