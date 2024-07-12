import requests
from tkinter import *
from customtkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import datetime
import pytz
from geopy.geocoders import Nominatim
#loaction api use
answer=bool()
country_name=str()
city_name=str()
def current_location():
    global country_name
    global city_name
    global answer
    global search_textbox
    global search_button
    answer=messagebox.askyesno(title="current location",message="want to use current location")
    if answer==True:
        location_api_key = 'ipb_live_WMETLoquJHhNmq0AbMvqe5O68t5vHKPq0VasLK9y'

        api_endpoint = 'https://api.ipbase.com/v2/info'
        query_params = {'apiKey': location_api_key}
        print(query_params)

        response = requests.get(api_endpoint, params=query_params)


        if response.status_code == 200:
            data = response.json()

            try:
                location_data = data['data']['location']
                country_name = location_data['country']['name']
                city_name = location_data['city']['name']
                search_textbox.insert("1.0",city_name)
            except KeyError as e:
                print(f'Error: {e}')
            # Handle response data
        else:
            # Handle errors
            print(f'Error: {response.status_code} - {response.text}')

def current_weather():
    global canvas1,image_container,main_background,resized_main_background,final_main_background
    global country_name, country_name_new
    global city_name
    global Country_city_label
    global answer
    global search_textbox
    global temperature_label2
    global feels_like_temperature_image_label
    global min_temperature_image_label
    global max_temperature_image_label
    global Pressure_image_label
    global Humidity_image_label
    global Visibility_image_label
    global Wind_speed_image_label
    global Wind_degree_image_label
    global Clouds_image_label
    global Time_sunrise_image_Label
    global Time_sunset_image_Label
    global Time_Time_label
    if answer==True:
        api_key = '4CY6XJ7FVKS8Z3TF2PUHE97CA'
        location = city_name
        start_date = '-7days'
        end_date = 'now'
        unit_group = 'metric'

        url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?startdate={start_date}&enddate={end_date}&unitGroup={unit_group}&key={api_key}'

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temperature = data['days'][0]['temp']
            feels_like = data['days'][0]['feelslike']
            temp_min = data['days'][0]['tempmin']
            temp_max = data['days'][0]['tempmax']
            pressure = data['days'][0]['pressure']
            humidity = data['days'][0]['humidity']
            visibility = data['days'][0]['visibility']
            wind_speed = data['days'][0]['windspeed']
            wind_degree = data['days'][0]['winddir']
            clouds = data['days'][0]['cloudcover']
            sunrise = data['days'][0]['sunrise']
            sunset = data['days'][0]['sunset']
            timezone = data['timezone']
            new_timezone = pytz.timezone(timezone)
            current_time = datetime.datetime.now(new_timezone).time()
            formatted_time = str(current_time.strftime('%H:%M:%S'))
            if (formatted_time) < sunrise and (formatted_time) >= sunset:
                main_background = Image.open("night.jpg")
                resized_main_background = main_background.resize((2600, 1200))
                final_main_background = ImageTk.PhotoImage(resized_main_background)
                canvas1.itemconfig(image_container, image=final_main_background)
            elif (formatted_time) >= sunrise and (formatted_time) < ("16:00:00"):
                main_background = Image.open("morning_new.jpg")
                resized_main_background = main_background.resize((2600, 1200))
                final_main_background = ImageTk.PhotoImage(resized_main_background)
                canvas1.itemconfig(image_container, image=final_main_background)
            else:
                main_background = Image.open("evening.jpg")
                resized_main_background = main_background.resize((2600, 1200))
                final_main_background = ImageTk.PhotoImage(resized_main_background)
                canvas1.itemconfig(image_container, image=final_main_background)
            temperature_label2.config(text=temperature)
            feels_like_temperature_image_label.config(text=feels_like)
            min_temperature_image_label.config(text=temp_min)
            max_temperature_image_label.config(text=temp_max)
            Pressure_image_label.config(text=pressure)
            Humidity_image_label.config(text=humidity)
            Visibility_image_label.config(text=visibility)
            Wind_speed_image_label.config(text=wind_speed)
            Wind_degree_image_label.config(text=wind_degree)
            Clouds_image_label.config(text=clouds)
            Time_sunrise_image_Label.config(text=sunrise)
            Time_sunset_image_Label.config(text=sunset)
            Time_Time_label.config(text=formatted_time)
            Country_city_label.config(text=(city_name+","+country_name))
            # Process the data as needed
        else:
            print(f'Error: {response.status_code} - {response.text}')
    else:
        city_name=search_textbox.get("1.0",END)
        api_key = '4CY6XJ7FVKS8Z3TF2PUHE97CA'
        location = city_name
        start_date = '-7days'
        end_date = 'now'
        unit_group = 'metric'

        url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?startdate={start_date}&enddate={end_date}&unitGroup={unit_group}&key={api_key}'

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temperature = data['days'][0]['temp']
            feels_like = data['days'][0]['feelslike']
            temp_min = data['days'][0]['tempmin']
            temp_max = data['days'][0]['tempmax']
            pressure = data['days'][0]['pressure']
            humidity = data['days'][0]['humidity']
            visibility = data['days'][0]['visibility']
            wind_speed = data['days'][0]['windspeed']
            wind_degree = data['days'][0]['winddir']
            clouds = data['days'][0]['cloudcover']
            sunrise = data['days'][0]['sunrise']
            sunset = data['days'][0]['sunset']
            timezone = data['timezone']
            new_timezone = pytz.timezone(timezone)
            current_time = datetime.datetime.now(new_timezone).time()
            formatted_time = str(current_time.strftime('%H:%M:%S'))
            if (formatted_time) < sunrise and (formatted_time) >= sunset:
                main_background = Image.open("night.jpg")
                resized_main_background = main_background.resize((2600, 1200))
                final_main_background = ImageTk.PhotoImage(resized_main_background)
                canvas1.itemconfig(image_container, image=final_main_background)
            elif (formatted_time) >= sunrise and (formatted_time) < ("16:00:00"):
                main_background = Image.open("morning_new.jpg")
                resized_main_background = main_background.resize((2600, 1200))
                final_main_background = ImageTk.PhotoImage(resized_main_background)
                canvas1.itemconfig(image_container, image=final_main_background)
            else:
                main_background = Image.open("evening.jpg")
                resized_main_background = main_background.resize((2600, 1200))
                final_main_background = ImageTk.PhotoImage(resized_main_background)
                canvas1.itemconfig(image_container, image=final_main_background)


            geolocator = Nominatim(user_agent="my_geocoder")
            country_name = geolocator.geocode(city_name)

            if country_name:
                country_name_new= country_name.address.split(',')[-1].strip()
            else:
                pass

            temperature_label2.config(text=temperature)
            feels_like_temperature_image_label.config(text=feels_like)
            min_temperature_image_label.config(text=temp_min)
            max_temperature_image_label.config(text=temp_max)
            Pressure_image_label.config(text=pressure)
            Humidity_image_label.config(text=humidity)
            Visibility_image_label.config(text=visibility)
            Wind_speed_image_label.config(text=wind_speed)
            Wind_degree_image_label.config(text=wind_degree)
            Clouds_image_label.config(text=clouds)
            Time_sunrise_image_Label.config(text=sunrise)
            Time_sunset_image_Label.config(text=sunset)
            Time_Time_label.config(text=formatted_time)
            Country_city_label.config(text=(city_name + "," + str(country_name_new)))
            # Process the data as needed
        else:
            print(f'Error: {response.status_code} - {response.text}')



# frontend design gui
main_window=CTk()
main_window.geometry("600x600")
#adding image to background

main_background=Image.open("nice_background.jpg")
resized_main_background=main_background.resize((2600,1200))
final_main_background=ImageTk.PhotoImage(resized_main_background)
canvas1 = Canvas(main_window, width=600,
                 height=600)

canvas1.pack(fill="both", expand=True)

# Display image
image_container=canvas1.create_image(0, 0, image=final_main_background,
                     anchor="nw")
main_window.title("Weather Dashboard")

search_textbox=CTkTextbox(master=main_window,
                          fg_color="white",
                          font=("Arial",25),height=15,width=600)



search=Image.open("search.png")
resized_search=search.resize((70,50))
new_search=ImageTk.PhotoImage(resized_search)
search_button=Button(main_window,
                     image=new_search,
                     bg="white",
                     activebackground="white",
                     text="Search",font=("Georgia",20,"bold"),
                     compound="left",
                     command=current_weather)
search_button.place(x=1600,y=37)
search_textbox.place(x=800,y=30)
location=Image.open("location (1).png")
resized_location=location.resize((70,50))
new_location=ImageTk.PhotoImage(resized_location)
location_button=Button(main_window,
                       command=current_location,
                       image=new_location,
                       bg="white",
                       activebackground="white"
                       )
location_button.place(x=20,y=37)
location_label=CTkLabel(main_window,
                     text="Current Location",
                     font=("Georgia",10,"bold"),
                     fg_color="white",
                     text_color="black",
                     padx=5,
                     pady=5,
                     width=15,
                     height=1)
location_label.place(x=6,y=80)
temperature_background=Image.open("temperature_background.jpg")
resized_temperature_background=temperature_background.resize((300,190))
final_temperature_background=ImageTk.PhotoImage(resized_temperature_background)

temperature_frame=CTkFrame(main_window,
                           fg_color="white",
                           width=270,
                           height=200,
                           corner_radius=40,
                           border_width=2,
                           border_color="white",bg_color="black")

temperature_label1=Label(temperature_frame,
                         text="TEMPERATURE :",
                         font=("Georgia",25,"bold"),
                         bg="white")
temperature_label1.place(x=10,y=20)
temperature_frame.place(x=700,y=120)
temperature_textbox=CTkTextbox(temperature_frame,
                               width=250,
                               height=130)
temperature_textbox.place(x=10,y=55)
temperature_label2=Label(temperature_textbox,
                         image=final_temperature_background,
                         text="20",
                         font=("Georgia",45,"bold"),
                         fg="white",
                         compound="center")
temperature_label2.place(x=0,y=0)

#feels like temperature

feels_like_temperature_frame=CTkFrame(main_window,
                                corner_radius=40,
                                width=250,
                                height=200,
                                bg_color="black",
                                fg_color="white")
feels_like_temperature_frame.place(x=30,y=350)
feels_like_temperature_label=Label(feels_like_temperature_frame,
                                  text="Feel's Like: ",
                                  font=("Georgia",30,"bold"),
                                  width=10,
                                  height=1,
                                  fg="black",
                                  bg="white")
feels_like_temperature_label.place(x=15,y=15)
feels_like_temperature_background=Image.open("temperature_background.jpg")
resized_feels_like_temperature_background=feels_like_temperature_background.resize((270,190))
final_feels_like_temperature_background=ImageTk.PhotoImage(resized_feels_like_temperature_background)
feels_like_temperature_image_label=Label(feels_like_temperature_frame,
                                         image=final_feels_like_temperature_background,
                                         width=270,
                                         height=150,
                                         text="25",
                                         compound="center",font=("Georgia",40,"bold"),
                                         fg="white")
feels_like_temperature_image_label.place(x=18,y=70)
min_temperature_Frame=CTkFrame(main_window,
                                   corner_radius=50,
                                   fg_color="white",
                                   bg_color="black",
                                   width=300,
                                   height=200)
min_temperature_label=Label(min_temperature_Frame,
                            text="Min Temperature : ",
                            font=("Georgia",25,"bold"),
                            fg="black",
                            bg="white",
                            width=15)
min_temperature_label.place(x=30,y=30)
min_temperature_Frame.place(x=325,y=350)

min_temperature_background=Image.open("temperature_background.jpg")
resized_min_temperature_background=min_temperature_background.resize((300,170))
final_min_temperature_background=ImageTk.PhotoImage(resized_min_temperature_background)

min_temperature_image_label=Label(min_temperature_Frame,
                                  image=final_min_temperature_background,
                                  width=300,
                                  height=150,
                                  text="40",
                                  compound="center",
                                  font=("Georgia",40,"bold"),
                                  fg="white")

min_temperature_image_label.place(x=35,y=80)




max_temperature_Frame=CTkFrame(main_window,
                               corner_radius=50,
                               fg_color="white",
                               bg_color="black",
                               width=300,
                               height=200)
max_temperature_label=Label(max_temperature_Frame,
                            text="Max Temperature : ",
                            font=("Georgia",25,"bold"),
                            fg="black",
                            bg="white",
                            width=15)
max_temperature_label.place(x=30,y=30)
max_temperature_Frame.place(x=670 ,y=350)

max_temperature_background=Image.open("temperature_background.jpg")
resized_max_temperature_background=max_temperature_background.resize((300,170))
final_max_temperature_background=ImageTk.PhotoImage(resized_max_temperature_background)
max_temperature_image_label=Label(max_temperature_Frame,
                                  image=final_max_temperature_background,
                                  width=300,
                                  height=150,
                                  text="40",
                                  compound="center",
                                  font=("Georgia",40,"bold"),
                                  fg="white")

max_temperature_image_label.place(x=35,y=80)

Pressure_Frame=CTkFrame(main_window,
                       corner_radius=50,
                       fg_color="white",
                       bg_color="black",
                       width=200,
                       height=200)
Pressure_Frame.place(x=1015 ,y=350)
Pressure_label=Label(Pressure_Frame,
                    text="Pressure : ",
                    font=("Georgia",25,"bold"),
                    fg="black",
                    bg="white",
                    width=10)
Pressure_label.place(x=17,y=30)
Pressure_background=Image.open("temperature_background.jpg")
resized_Pressure_background=Pressure_background.resize((200,160))
final_Pressure_background=ImageTk.PhotoImage(resized_Pressure_background)

Pressure_image_label=Label(Pressure_Frame,
                          image=final_Pressure_background,
                          width=200,
                          height=140,
                          text="1018",
                          compound="center",
                          font=("Georgia",40,"bold"),
                          fg="white")

Pressure_image_label.place(x=25,y=80)


Humidity_Frame=CTkFrame(main_window,
                       corner_radius=50,
                       fg_color="white",
                       bg_color="black",
                       width=200,
                       height=200)
Humidity_Frame.place(x=1270 ,y=350)
Humidity_label=Label(Humidity_Frame,
                    text="Humidity : ",
                    font=("Georgia",25,"bold"),
                    fg="black",
                    bg="white",
                    width=10)
Humidity_label.place(x=17,y=30)
Humidity_background=Image.open("temperature_background.jpg")
resized_Humidity_background=Humidity_background.resize((200,160))
final_Humidity_background=ImageTk.PhotoImage(resized_Humidity_background)

Humidity_image_label=Label(Humidity_Frame,
                          image=final_Humidity_background,
                          width=200,
                          height=140,
                          text="1018",
                          compound="center",
                          font=("Georgia",40,"bold"),
                          fg="white")

Humidity_image_label.place(x=25,y=80)

Visibility_Frame=CTkFrame(main_window,
                       corner_radius=50,
                       fg_color="white",
                       bg_color="black",
                       width=200,
                       height=200)
Visibility_Frame.place(x=40 ,y=575)
Visibility_label=Label(Visibility_Frame,
                    text="Visibility : ",
                    font=("Georgia",25,"bold"),
                    fg="black",
                    bg="white",
                    width=10)
Visibility_label.place(x=17,y=30)
Visibility_background=Image.open("temperature_background.jpg")
resized_Visibility_background=Visibility_background.resize((200,160))
final_Visibility_background=ImageTk.PhotoImage(resized_Visibility_background)

Visibility_image_label=Label(Visibility_Frame,
                          image=final_Visibility_background,
                          width=200,
                          height=140,
                          text="1018",
                          compound="center",
                          font=("Georgia",40,"bold"),
                          fg="white")

Visibility_image_label.place(x=25,y=80)

Wind_Frame=CTkFrame(main_window,
                   corner_radius=50,
                   fg_color="white",
                   bg_color="black",
                   width=600,
                   height=200)

Wind_Frame.place(x=285,y=575)
Wind_label=Label(Wind_Frame,
                text="Wind ",
                font=("Georgia",40,"bold"),
                fg="black",
                bg="white",
                width=15)
Wind_label.place(x=85,y=5)
Wind_speed_label=Label(Wind_Frame,
                text="Speed :",
                font=("Georgia",30,"bold"),
                fg="black",
                bg="white",
                width=15)
Wind_speed_label.place(x=-30,y=60)
Wind_speed_background=Image.open("temperature_background.jpg")
resized_Wind_speed_background=Wind_speed_background.resize((250,160))
final_Wind_speed_background=ImageTk.PhotoImage(resized_Wind_speed_background)

Wind_speed_image_label=Label(Wind_Frame,
                          image=final_Wind_speed_background,
                          width=250,
                          height=100,
                          text="1018",
                          compound="center",
                          font=("Georgia",40,"bold"),
                          fg="white")

Wind_speed_image_label.place(x=35,y=130)

Wind_degree_label=Label(Wind_Frame,
                text="Degree :",
                font=("Georgia",30,"bold"),
                fg="black",
                bg="white",
                width=15)
Wind_degree_label.place(x=350,y=60)
Wind_degree_background=Image.open("temperature_background.jpg")
resized_Wind_degree_background=Wind_degree_background.resize((250,160))
final_Wind_degree_background=ImageTk.PhotoImage(resized_Wind_degree_background)

Wind_degree_image_label=Label(Wind_Frame,
                          image=final_Wind_degree_background,
                          width=250,
                          height=100,
                          text="1018",
                          compound="center",
                          font=("Georgia",40,"bold"),
                          fg="white")

Wind_degree_image_label.place(x=450,y=130)

Clouds_Frame=CTkFrame(main_window,
                       corner_radius=50,
                       fg_color="white",
                       bg_color="black",
                       width=200,
                       height=200)
Clouds_Frame.place(x=930 ,y=575)
Clouds_label=Label(Clouds_Frame,
                    text="Clouds : ",
                    font=("Georgia",25,"bold"),
                    fg="black",
                    bg="white",
                    width=10)
Clouds_label.place(x=17,y=30)
Clouds_background=Image.open("temperature_background.jpg")
resized_Clouds_background=Clouds_background.resize((200,160))
final_Clouds_background=ImageTk.PhotoImage(resized_Clouds_background)

Clouds_image_label=Label(Clouds_Frame,
                          image=final_Clouds_background,
                          width=200,
                          height=140,
                          text="1018",
                          compound="center",
                          font=("Georgia",40,"bold"),
                          fg="white")
Clouds_image_label.place(x=25,y=80)


Country_city_background=Image.open("temperature_background.jpg")
resized_Country_city_background=Country_city_background.resize((650,300))
final_Country_city_background=ImageTk.PhotoImage(resized_Country_city_background)

Country_city_label=Label(main_window,
                 image=final_Country_city_background,
                 text="Country,City",
                 font=("Times new roman",30,"bold"),
                 fg="white",
                 compound="center",
                 width=600,
                 height=100)
Country_city_label.place(x=250,y=10)
Time_Frame=CTkFrame(main_window,
                    fg_color="white",
                    width=600,
                    height=200,
                    corner_radius=50,
                    bg_color="black")
Time_background=Image.open("temperature_background.jpg")
resized_Time_background=Time_background.resize((600,300))
final_Time_background=ImageTk.PhotoImage(resized_Time_background)


Time_Time_label=Label(Time_Frame,
                      image=final_Time_background,
                      width=350,
                      height=80,
                      text="3:00",
                      compound="center",
                      font=("Georgia",40,"bold"),
                      fg="white")
Time_Frame.place(x=30,y=125)
Time_Time_label.place(x=200,y=10)
Time_sunrise_Label=Label(Time_Frame,
                         text="Sunrise :",
                         fg="black",
                         width=10,
                         height=1,
                         font=("Georgia",30,"bold"),
                         bg="white")
Time_sunrise_Label.place(x=30,y=100)
Time_sunrise_background=Image.open("temperature_background.jpg")
resized_Time_sunrise_background=Time_sunrise_background.resize((300,100))
final_Time_sunrise_background=ImageTk.PhotoImage(resized_Time_sunrise_background)
Time_sunrise_image_Label=Label(Time_Frame,
                               image=final_Time_sunrise_background,
                               width=300,
                               height=80,
                               text="2:00",
                               font=("Georgia",40,"bold"),
                               fg="white",
                               compound="center")
Time_sunrise_image_Label.place(x=30,y=155)


Time_sunset_Label=Label(Time_Frame,
                         text="Sunset :",
                         fg="black",
                         width=10,
                         height=1,
                         font=("Georgia",30,"bold"),
                         bg="white")
Time_sunset_Label.place(x=430,y=100)
Time_sunset_background=Image.open("temperature_background.jpg")
resized_Time_sunset_background=Time_sunset_background.resize((300,100))
final_Time_sunset_background=ImageTk.PhotoImage(resized_Time_sunset_background)
Time_sunset_image_Label=Label(Time_Frame,
                               image=final_Time_sunset_background,
                               width=300,
                               height=80,
                               text="2:00",
                               font=("",40,"bold"),
                               fg="white",
                               compound="center")
Time_sunset_image_Label.place(x=400,y=155)
main_window.mainloop()