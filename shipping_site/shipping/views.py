from django.shortcuts import render, get_object_or_404, redirect
from .models import ShippingDetail
from django.contrib import messages



def home(request):
    if request.method == 'POST':
        code = request.POST.get('code', '').strip()
        try:
            shipping_detail = ShippingDetail.objects.get(code__iexact=code)
            request.session['shipping_code'] = code
            return redirect('home')
        except ShippingDetail.DoesNotExist:
            request.session['error_message'] = "Shipping code does not exist. Please check and try again."
            return redirect('home')

    code = request.session.get('shipping_code', None)
    error_message = request.session.pop('error_message', None)
    shipping_detail = ShippingDetail.objects.filter(code__iexact=code).first() if code else None

    return render(request, 'shipping/index.html', {'shipping_detail': shipping_detail, 'error_message': error_message})