import csv
import matplotlib.pyplot as plt

def read_csv(file_path):
    file_path=("C:/Users/Brenda/Desktop/matplotlib/data.csv")
    
    
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile,delimiter=",")
        header=next (reader)
        data=[]
        for row in reader:
            iterable=zip(header,row)
            diccionario={key:value for key,value in iterable}
            data.append(diccionario)
        return data
if __name__=="__main__":
    data=read_csv("C:/Users/Brenda/Desktop/matplotlib/data.csv")
    

Colombia=data[42]        

poblaciones=[]
for key in ['2022 Population','2020 Population','2015 Population','2010 Population','2000 Population','1990 Population','1980 Population','1970 Population']:
    poblaciones.append(int(Colombia[key]))
print(poblaciones)

def generate_bar_chart(labels,values):
    fig, ax=plt.subplots()
    ax.bar(labels,values)
    plt.show()

if __name__=="__main__":
    labels=['2022 Population','2020 Population','2015 Population','2010 Population','2000 Population','1990 Population','1980 Population','1970 Population']
    values= poblaciones
    generate_bar_chart(labels,values)