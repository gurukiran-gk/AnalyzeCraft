from django.shortcuts import render
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def homepage(request):
    return render(request, 'index.html')

def process_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        dataan = pd.read_csv(csv_file)
        num_rows, num_columns = dataan.shape
        column_names = dataan.columns.tolist()
        csv_details = {
            'num_rows': num_rows,
            'num_columns': num_columns,
            'column_names': column_names
        }
        return render(request, 'analyse.html',{'csv_details': csv_details})
    else:
        # Handle if no file is uploaded or method is not POST
        return render(request, 'index.html')
