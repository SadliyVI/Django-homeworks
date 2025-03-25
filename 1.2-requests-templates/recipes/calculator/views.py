from django.shortcuts import render
from django.http import  HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def get_recipe_list(request):
    context = {
        'recipes_list': DATA
    }
    return render(request,'my_recipes.html', context )

def get_recipe(request):
    context = {}
    ingredients = []
    recipe_name = ''
    count = int(request.GET.get('count', 1))
    path = (request.path).strip('/')
    for el in DATA:
        if path == (el.lower()):
            for key,value in DATA[el].items():
                value = value * count
                ingredients.append((key,value))
                recipe_name = el.title()
    context = {
        'ingredients': ingredients,
        'recipe_name': recipe_name

    }
    # return render(request, f'{recipe_name.lower()}.html', context)
    return render(request, 'index.html', context)


