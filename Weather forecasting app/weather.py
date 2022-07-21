import tkinter as tk
import requests
from PIL import Image,ImageTk

root = tk.Tk()
root.title("Weather Forecasting App")
root.geometry("600x500")

#api key : 35b33af119cb023cd10104cfd3f0d71f
#api url :  https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

def format_response(weather):
    try:
        city=weather['name']
        condition=weather['weather'][0]['description']
        temp=weather['main']['temp']
        final_str='City:%s\nCondition:%s\nTemprature:%s'%(city,condition,temp)
    except:
        final_str='Error Occurred!'
    return final_str

def get_weather(city):
    weather_key='35b33af119cb023cd10104cfd3f0d71f'
    weather_url='https://api.openweathermap.org/data/2.5/weather'
    parameters={'APPID':weather_key,'q':city,'units':'imperial'}
    response=requests.get(weather_url,parameters)
    #print(response.json())
    weather=response.json()

    result['text']=format_response(weather)

    icon_name=weather['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon):
    size=int(second_frame.winfo_height()*0.25)
    img=ImageTk.PhotoImage(Image.open('./images/'+icon+'.png').resize((size,size)))
    weather_icon.delete('all')
    weather_icon.create_image(0,0,anchor='nw',image=img)
    weather_icon.image=img

img=Image.open('./w_image.png')
img=img.resize((600,500),Image.ANTIALIAS)
img_photo=ImageTk.PhotoImage(img)

w_image_lbl=tk.Label(root,image=img_photo)
w_image_lbl.place(x=0,y=0,width=600,height=500)

heading_title=tk.Label(w_image_lbl,text='Weather View Around The World',fg='red',bg='sky blue',font=('times new roman',20,'bold'))
heading_title.place(x=100,y=18)

first_frame=tk.Frame(w_image_lbl,bg="#42c2f4",bd=5)
first_frame.place(x=100,y=60,width=450,height=50)

text_box=tk.Entry(first_frame,font=('times new roman',25),width=15)
text_box.grid(row=0,column=0,sticky='w')

button=tk.Button(first_frame,text='Search Weather',fg='green',font=('times new roman',16,'bold'),command=lambda:get_weather(text_box.get()))
button.grid(row=0,column=1,padx=10)

second_frame=tk.Frame(w_image_lbl,bg="#42c2f4",bd=5)
second_frame.place(x=100,y=130,width=450,height=300)

result=tk.Label(second_frame,font=40,bg='white',justify='left',anchor='nw')
result.place(relwidth=1,relheight=1)

weather_icon=tk.Canvas(result,bg='white',bd=0,highlightthickness=0)
weather_icon.place(relx=0.75,rely=0,relwidth=1,relheight=0.5)

root.mainloop()