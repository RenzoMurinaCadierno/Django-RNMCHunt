from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Product, Vote

def home(request):

    # get all Product objects from the DB
    products = Product.objects

    return render(request, 'products/home.html', {'products': products})

@login_required(login_url='/accounts/login')
def create(request):

    if request.method == 'POST':

        # Check if everything was submitted.
        # Imagesare stored in FILES dictionary, not in POST
        if request.POST['title'] and request.POST['body']\
            and request.POST['url'] and request.FILES['icon']\
            and request.FILES['image']:

            # Create a product object
            product = Product()

            product.title = request.POST['title']
            product.body = request.POST['body']

            # If the url already begins properly, set it.
            if request.POST['url'].startswith('http://') or\
                request.POST['url'].startswith('https://'):

                product.url = request.POST['url']

            # If it does not, prepend the beginning
            else:

                product.url = 'http://' + request.POST['url']

            product.image = request.FILES['image']
            product.icon = request.FILES['icon']

            # Add the current timezone to the created product
            product.pub_date = timezone.datetime.now()

            # Set the hunter to be the user that created this product
            product.hunter = request.user

            # insert the product to the database
            product.save()

            # redirect the user to the created product. Use its ID
            # to track it
            return redirect('/products/' + str(product.id))

        # Some field was not completed
        else:
            return render(
                request,
                'products/create.html',
                {'error': 'All fields are required.'}
            )
    else:
        return render(request, 'products/create.html')


def detail(request, product_id):

    # get the object with the pk coming from the url /products/1
    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'products/detail.html', {'product' : product})


@login_required(login_url='/accounts/login')
def upvote(request, product_id):

    if request.method == 'POST':

        products = Product.objects

        product = get_object_or_404(Product, pk=product_id)

        try:
            votes = Vote.objects.get(product=product, hunter=request.user)
            votes.delete()
            print('deleted',votes, 'req', request.user.username, 'hunter', votes.hunter.username)
            votes = None
            return render(request, 'products/home.html', {'products': products, 'votes': votes})

        except Vote.DoesNotExist:

            vote = Vote()
            vote.product=product
            vote.hunter=request.user
            vote.save()
            print('created',vote, 'req', request.user.username, 'hunter', vote.hunter.username)
            return render(request, 'products/home.html', {'products': products, 'votes': vote})
