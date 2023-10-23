from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def calculator(request):
    context = {}
    if request.method == 'POST':
        operation = request.POST.get('operation')
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 /num2
            else:
                result = 'Cannot divide by zero'
        context['result'] = result

    return render(request, 'calculator.html', context)

