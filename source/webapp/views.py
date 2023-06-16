from django.shortcuts import render, redirect


from .models import Cat


def welcome(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        cat = Cat.objects.create(name=name)
        return redirect('cat_info', cat_id=cat.id)
    return render(request, 'welcome.html')


def cat_info(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'feed':
            if cat.hunger < 100:
                cat.hunger += 15
                cat.happiness += 5
                if cat.hunger > 100:
                    cat.happiness -= 30
                    cat.hunger = 100
        elif action == 'play':
            if cat.hunger > 0:
                cat.happiness += 15
                cat.hunger -= 10
                if cat.hunger <= 0:
                    cat.happiness = 0
                elif cat.hunger > 0 >= cat.happiness:
                    cat.happiness = 1
        elif action == 'sleep':
            if cat.hunger > 0:
                cat.happiness -= 5
                if cat.happiness <= 0:
                    cat.happiness = 1
        cat.save()
    return render(request, 'cat_info.html', {'cat': cat})
