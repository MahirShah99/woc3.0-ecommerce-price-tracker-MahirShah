from django.shortcuts import render
from django.http import HttpResponse
from .forms import EbayForm
from Scripts.selenium_ebay import webScrapEbay
from Scripts.send_email import send_email

# Create your views here.
def ebayscrap(request):
    form = EbayForm()
    
    if request.method == "POST":
        form = EbayForm(request.POST)

        if form.is_valid():
            url = form.cleaned_data['url']
            desired_price = form.cleaned_data['desired_price']
            email = form.cleaned_data['email']
            # print("Url:- ",url_get)
            # print("Price:- ", desired_price)
            # print("Email:- ", email)

            data = webScrapEbay(url, desired_price, email)

            if(data['status'] == True):
                send_email(data)
            
            form.save(commit=True)
            return render(request, 'result.html', context={"data": data})
        else:
            print("Error")
        
    return render(request, 'ebay/ebayscrap.html', {"form": form})