from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from listings.models import Band
from listings.models import Title
from listings.forms import BandForm, ListingForm, ContactUsForm
from django.shortcuts import redirect

def band_list(request):
    bands = Band.objects.all()
    return render(request,
            'listings/band_list.html',
            {'bands': bands})

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request,
            'listings/band_detail.html',
            {'band': band})

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # create a new 'band' and save it to the database
            band = form.save()
            # redirect to the detail page of the band we just created
            # we can provide the url pattern arguments as arguments to redirect function
            return redirect('band-detail', band.id)
    else:
        form = BandForm()

    return render(request,
            'listings/band_create.html',
            {'form': form})

def band_update(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # update the existing 'Band' in the database
            form.save()
            # redirect to the detail page of the 'Band' we just upodate
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band) # prepopulate the form with an existing band

    return render(request,
            'listings/band_update.html',
            {'form': form})

def band_delete(request, id):
    band = Band.objects.get(id=id) # we need this for both GET and POST

    if request.method == 'POST':
        # delete the band from the database
        band.delete()
        # redirect to the band list
        return redirect('band-list')
    # no need for a 'else' here. If it's a GET request, just continue

    return render(request,
            'listings/band_delete.html',
            {'band': band})

"""

    the code for the listings start from here.
    And the codes are basically the same as the band program

"""
def listings(request):
    titles = Title.objects.all()
    return render(request,
            'listings/listings.html',
            {'titles': titles})

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            title = form.save()
            return redirect('listing-detail', title.id)
    else:
        form = ListingForm()

    return render(request,
            'listings/listing_create.html',
            {'form': form})

def listing_detail(request, id):
    title = Title.objects.get(id=id)
    return render(request,
            'listings/listing_detail.html',
            {'title': title})

def listing_update(request, id):
    title = Title.objects.get(id=id)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=title)
        if form.is_valid():
            form.save()
            return redirect('lsitings-detail', title.id)
    else:
        form = ListingForm(instance=title)

    return render(request,
            'listings/listing_update.html',
            {'form': form})

def listing_delete(request, id):
    title = Title.objects.get(id=id)

    if request.method == 'POST':
        title.delete()
        return redirect('listings')

    return render(request,
            'listings/listing_delete.html',
            {'title': title})

def contact(request):
    if request.method == 'POST':
        # create an instance of our form, and fill it with the POST data
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject = f'Message from {form.cleaned_data["name"] or "anonymous"} via MerchEx Contact Us form',
                message = form.cleaned_data['message'],
                from_email = form.cleaned_data['email'],
                recipient_list = ['admin@merchex.xyz'],
            )
            # retrieve the email from the query parameters and pass it to the template.
            email = form.cleaned_data['email']
            # Redirect the user to the email-sent page,
            #including the user's email address as a query parameter in the URL.
            return redirect(f'email-sent?email={email}')
        # if the form is not valid, we let execution continue to the return
        # statement below, and display the form again (with errors).

    else:
        # this must be a GET request, so create an empty form
        form = ContactUsForm() # instantiate a new form here
    return render(request,
            'listings/contact.html',
            {'form': form}) # pass that form to the template

def email_sent(request):

    email = request.GET.get('email', 'No email provided')
    return render(request,
            'listings/email_sent.html',
            {'email': email})

def about(request):
    return render(request, 'listings/about.html')
