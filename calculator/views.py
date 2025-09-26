import math
from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm

def calculator_view(request):
    result, error = None, None
    notes = []

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            if a < 1:
                notes.append("A is less than 1 (too small).")
            if b == 0:
                notes.append("B is 0 and will not affect the result.")

            if c < 0:
                error = "C cannot be negative."
            else:
                c3 = c ** 3
                sqrt_c3 = math.sqrt(c3)
                if c3 > 1000:
                    tmp = sqrt_c3 * 10
                else:
                    if a == 0:
                        error = "Cannot divide by zero because A is 0."
                        tmp = None
                    else:
                        tmp = sqrt_c3 / a
                if error is None:
                    result = tmp + b
        else:
            error = "Please enter numeric values for A, B, and C."
    else:
        form = InputForm()

    return render(request, 'calculator/result.html',
                  {'form': form, 'result': result, 'error': error, 'notes': notes})

def health(request):
    return HttpResponse("ok")
