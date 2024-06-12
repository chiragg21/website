from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .models import Fashion

import joblib
import numpy as np
import pandas as pd
k=joblib.load("colors_info.pkl")
#print(k['center_col'])
colors = pd.read_csv("ColorCodes.csv")
X = colors.copy()
X.drop(columns=['Color'],inplace=True)

clusters = k['clusters']
center_col = k['center_col']
centroids = k['centroids']


def get_colors(col):
    rgbval = [X.iloc[i] for i in range(colors.shape[0]) if colors['Color'][i].lower() == col.lower()]
    distances = []
    for i in range(10):
        distances.append(np.linalg.norm(centroids[i] - rgbval, axis=1))
        
    return list(clusters[center_col[np.argmin(distances)]])

def myapp(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('myfirst.htm')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.htm')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.htm')
  return HttpResponse(template.render())

def fashion_table(request):
    # Fetch all records from the Fashion model
    records = Fashion.objects.all()

    # Pass the records to the template context
    context = {
        'records': records
    }

    return render(request, 'fashion_table.html', context)

def process_input(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        # Call your ML model function with user_input
        # output = predict_output(user_input)
        # For demonstration purposes, let's assume the output is:

        output=get_colors(user_input)
        records = Fashion.objects.filter( Colour__in=output)

       # output = ['Result 1', 'Result 2', 'Result 3']
        return render(request, 'fashion_table.html', {'records': records})
    return render(request, 'input.html')

