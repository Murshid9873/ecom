from django.shortcuts import redirect


def auth_customer(func):
    def wrap(request, *args, **kwargs):
        if 'customer' in request.session:
            return redirect('customer:cushome')

        else:
            return func(request, *args, **kwargs)
    return wrap
