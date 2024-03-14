import io
from django.http import HttpResponse
from django.shortcuts import render
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

csv_file = None


def homepage(request):
    return render(request, 'index.html')

from django.shortcuts import render
import pandas as pd

from django.shortcuts import render, redirect
import pandas as pd

def process_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        dataan = pd.read_csv(csv_file)
        json_data = dataan.to_json(orient='records')  # Convert DataFrame to JSON
        request.session['json_data'] = json_data   # Store JSON data in session
        num_rows, num_columns = dataan.shape
        column_names = dataan.columns.tolist()
        csv_details = {
                'num_rows': num_rows,
                'num_columns': num_columns,
                'column_names': column_names,
                'flag': 1
        }
        return render(request, 'analyse.html', {'csv_details': csv_details})
    else :
        return render(request, 'index.html')
        
def fun_0001(request):
    rows = int(request.POST.get('functionInput1', 0))
    json_data = request.session.get('json_data')
    if json_data:
        json_io = io.StringIO(json_data)
        data = pd.read_json(json_io)
        csv_file = data.to_csv(index=False)
        if csv_file:
            df = pd.read_csv(io.StringIO(csv_file))
            df_head = df.head(rows)
            df_html = df_head.to_html()
            csv_details = {
                'df_html': df_html,
                'flag': 0
            }
            return render(request, 'analyse.html', {'csv_details': csv_details})
        else:
            return HttpResponse("No CSV data found in the session.")
    else:
        return HttpResponse("No JSON data found in the session.")

def fun_0002(request):
    rows = int(request.POST.get('functionInput1', 0))
    json_data = request.session.get('json_data')
    if json_data:
        json_io = io.StringIO(json_data)
        data = pd.read_json(json_io)
        csv_file = data.to_csv(index=False)
        if csv_file:
            df = pd.read_csv(io.StringIO(csv_file))
            df_tail = df.tail(rows)
            df_html = df_tail.to_html()
            csv_details = {
                'df_html': df_html,
                'flag': 0
            }
            return render(request, 'analyse.html', {'csv_details': csv_details})
        else:
            return HttpResponse("No CSV data found in the session.")
    else:
        return HttpResponse("No JSON data found in the session.")
    

def fun_0003(request):
    column = request.POST.get('functionInput1', 0)
    keyword = request.POST.get('functionInput2', 0)
    json_data = request.session.get('json_data')
    if json_data:
        json_io = io.StringIO(json_data)
        data = pd.read_json(json_io)
        csv_file = data.to_csv(index=False)
        if csv_file:
            df = pd.read_csv(io.StringIO(csv_file))
            df[column] = df[column].fillna('')

            if df[column].dtype == 'object':
                mask = df[column].str.lower().str.contains(str(keyword).lower(), na=False)
            else:
                mask = df[column] == float(keyword)

            filtered_df = df[mask]
            df_html = filtered_df.to_html()
            csv_details = {
                'df_html': df_html,
                'flag': 0
            }
            return render(request, 'analyse.html', {'csv_details': csv_details})
        else:
            return HttpResponse("No CSV data found in the session.")
    else:
        return HttpResponse("No JSON data found in the session.")
    
def fun_0004(request):
    column = request.POST.get('functionInput1', 0)
    keyword = request.POST.get('functionInput2', 0)
    ineq = request.POST.get('functionInput3', 0)

    json_data = request.session.get('json_data')
    if json_data:
        json_io = io.StringIO(json_data)
        data = pd.read_json(json_io)
        csv_file = data.to_csv(index=False)
        if csv_file:
            df = pd.read_csv(io.StringIO(csv_file))
            df[column] = df[column].fillna('')
            df[column] = pd.to_numeric(df[column], errors='coerce')
            numeric_mask = np.isfinite(df[column])
            
            if ineq == "greater_than":
                mask = (df[column] > float(keyword)) & numeric_mask
            elif ineq == "lesser_than":
                mask = (df[column] < float(keyword)) & numeric_mask
            elif ineq == "equal_to":
                mask = (df[column] == float(keyword)) & numeric_mask
            elif ineq == "not_equal_to":
                mask = (df[column] != float(keyword)) & numeric_mask

            filtered_df = df[mask]
            df_html = filtered_df.to_html()
            csv_details = {
                'df_html': df_html,
                'flag': 0
            }
            return render(request, 'analyse.html', {'csv_details': csv_details})
        else:
            return HttpResponse("No CSV data found in the session.")
    else:
        return HttpResponse("No JSON data found in the session.")
    

def fun_0005(request):
    coloumn = request.POST.get('functionInput1', 0)
    title = request.POST.get('functionInput2', 0)
    json_data = request.session.get('json_data')
    if json_data:
        json_io = io.StringIO(json_data)
        data = pd.read_json(json_io)
        csv_file = data.to_csv(index=False)
        if csv_file:
            df = pd.read_csv(io.StringIO(csv_file))
            
            plt.figure(figsize = (10,6))
            plt.bar(df[coloumn].value_counts().index, df[coloumn].value_counts())
            plt.title(title)
            plt.show()

            #df_html = df_head.to_html()
            csv_details = {
                'df_html': "Start Exploring other function..",
                'flag': 0
            }
            return render(request, 'analyse.html', {'csv_details': csv_details})
        else:
            return HttpResponse("No CSV data found in the session.")
    else:
        return HttpResponse("No JSON data found in the session.")


def fun_0006(request):
    X = request.POST.get('functionInput1', 0)
    Y = request.POST.get('functionInput2', 0)
    json_data = request.session.get('json_data')
    if json_data:
        json_io = io.StringIO(json_data)
        data = pd.read_json(json_io)
        csv_file = data.to_csv(index=False)
        if csv_file:
            df = pd.read_csv(io.StringIO(csv_file))
            
            plt.figure(figsize=(10, 6))
            sns.lineplot(data=df, x=X, y=Y)
            plt.title('Line Plot')
            plt.xlabel(X)
            plt.ylabel(Y)
            plt.grid(True)
            plt.show()

            #df_html = df_head.to_html()
            csv_details = {
                'df_html': "Start Exploring other function..",
                'flag': 0
            }
            return render(request, 'analyse.html', {'csv_details': csv_details})
        else:
            return HttpResponse("No CSV data found in the session.")
    else:
        return HttpResponse("No JSON data found in the session.")


def fun_0007(request):
    X = request.POST.get('functionInput1', 0)
    json_data = request.session.get('json_data')
    if json_data:
        json_io = io.StringIO(json_data)
        data = pd.read_json(json_io)
        csv_file = data.to_csv(index=False)
        if csv_file:
            df = pd.read_csv(io.StringIO(csv_file))
            
            type_counts = df[X].value_counts()

            # Step 3: Plot the pie chart
            plt.figure(figsize=(8, 8))
            plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=140)
            plt.title('Distribution of Types')
            plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.show()

            #df_html = df_head.to_html()
            csv_details = {
                'df_html': "Start Exploring other function..",
                'flag': 0
            }
            return render(request, 'analyse.html', {'csv_details': csv_details})
        else:
            return HttpResponse("No CSV data found in the session.")
    else:
        return HttpResponse("No JSON data found in the session.")
