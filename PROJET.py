 
##Géodésique vers géocentrique 

def transformation_cor_Geodisiques_Geocentriques(Lambda,Phi,h,a,b):
            Lambda=degree2radians(Lambda)
            Phi=degree2radians(Phi)
            e=sqrt(1-(b/a)**2)
            N=a/(sqrt(1-(e*sin(Phi))**2))
            x=(N+h)*cos(Phi)*cos(Lambda)
            y=(N+h)*cos(Phi)*sin(Lambda)
            z=(N*(1-(e)**2)+h)*sin(Phi)
            return x,y,z
        
        
def   Geodesiques_vers_geocentriques():
    
    global Mafenetre1,entry4,entry2,entry3,entry5,entry6,canvas1
    
    Mafenetre1 = Tk()
    Mafenetre1.geometry('900x350')
    Mafenetre1.title('Geodesiques_vers_geocentriques')
    Mafenetre1.iconbitmap('Ressources/favicon.ico')
    
    canvas1 = Canvas(Mafenetre1, width = 600, height = 500,relief = 'groove')
    canvas1.pack()
    canvas1.create_line(300, 35, 300, 220, dash=(4, 2))
    canvas1.create_line(305, 35, 305, 220, dash=(4, 2))
    
    label1 = Label(Mafenetre1, text='Transformation entre systemes de coordonnees:\n Géodésiques vers Géocentriques')
    label1.config(font=('Broadway', 18 ,'bold'),fg='#8B4513')
    canvas1.create_window(200, 25, window=label1)
    
   
    label2 = Label(Mafenetre1, text='La hauteur ellipsoidale h (m) :')
    label2.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas1.create_window(1, 60, window=label2)

    entry2 = Entry(Mafenetre1) 
    canvas1.create_window(200, 60, window=entry2)

    label4 = Label(Mafenetre1, text='Demi-grand axe a (m) :')
    label4.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas1.create_window(1, 90, window=label4)

    entry4 = Entry(Mafenetre1) 
    canvas1.create_window(200, 90, window=entry4)

    label5 = Label(Mafenetre1, text='Demi-petit axe b (m) :')
    label5.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas1.create_window(0, 120, window=label5)
    
    entry5 = Entry(Mafenetre1) 
    canvas1.create_window(200, 120, window=entry5)

    label3 = Label(Mafenetre1, text='La longitude Lambda (°) :')
    label3.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas1.create_window(1, 150, window=label3)

    entry3 = Entry(Mafenetre1) 
    canvas1.create_window(200, 150, window=entry3)

    label6 = Label(Mafenetre1, text='La latitude Phi (°) :')
    label6.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas1.create_window(1, 180, window=label6)

    entry6 = Entry(Mafenetre1) 
    canvas1.create_window(200, 180, window=entry6)

    button3 = Button(Mafenetre1,text='Transformer', command=g1et_coordonnees_geocentriques ,bg='#8B795E',fg='#FDFEFE', font=('Arial', 9, 'bold'))
    canvas1.create_window(200, 210, window=button3)
    
    Btn2 = Button(Mafenetre1, text = "Choisissez un datum",command=ellipsoide1,bg='#8B795E',fg='#FDFEFE',font=('Arial', 9, 'bold'))
    canvas1.create_window(30, 210, window=Btn2)

    Btn3= Button(Mafenetre1, text = 'show map', command =openweb3 ,bg='#8B795E',fg='#FDFEFE', font=('Arial', 9, 'bold'))
    canvas1.create_window(1, 240, window=Btn3)

    Btn4= Button(Mafenetre1, text = 'localisation', command =geocoder1 ,bg='#8B795E',fg='#FDFEFE', font=('Arial', 9, 'bold'))
    canvas1.create_window(100, 240, window=Btn4)

    Btn5= Button(Mafenetre1, text = 'visualisation 3D', command =map3d1 ,bg='#8B795E',fg='#FDFEFE', font=('Arial', 9, 'bold'))
    canvas1.create_window(200, 240, window=Btn5)

    Mafenetre1.mainloop()
    
    
   
def ellipsoide1():
    
    class Test:
        
      def __init__(self, tk0):
        self.var = StringVar()
        fontCombo = ("Ink Free", 16, "bold")
        self.data = ("Maupertuis (1738)","Plessis (1817)","Everest (1830)","Everest 1830 Modified (1967)","Airy (1830)","Bessel (1841)","Clarke (1866)","Clarke (1878)","Clarke (1880)","Helmert (1906)","Hayford (1910)","International (1924)","Krassovsky (1940)","WGS66 (1966)","Australian National (1966)","New International (1967)","GRS-67 (1967)","South American (1969)","WGS-72 (1972)","GRS-80 (1979)","WGS-84 (1984)","IERS (1989)","IERS (2003)")
        self.cb = Combobox(tk0, values=self.data,font = fontCombo)
        self.cb.place(x=50, y=50)
        self.b1 = Button(tk0, text="Réactualiser", command=lambda:[self.select(),tk0.destroy()],bg='#8B795E',fg='#FDFEFE',font=('Arial', 9, 'bold')).place(x=160, y=110)

      def set_text(Entry,text):   
        Entry.delete(0,END)
        Entry.insert(0,text)
        return
    
      def select(self):
        value = self.cb.get()
        ent_a=entry4
        ent_b=entry5
        if value=="Maupertuis (1738)" :
            set_text(ent_a,6397300)
            set_text(ent_b,6363806.283)
        
        elif value=="Plessis (1817)" :
            set_text(ent_a,6376523.0)
            set_text(ent_b,6355862.9333)
        
        elif value=="Everest (1830)" :
            set_text(ent_a,6377299.365)
            set_text(ent_b,6356098.359)
        
        elif value=="Everest 1830 Modified (1967)" :
            set_text(ent_a,6377304.063)
            set_text(ent_b,6356103.0390)
        
        elif value=="Everest 1830 (1967 Definition)" :
            set_text(ent_a,6377298.556)
            set_text(ent_b,6356097.550)
        
        elif value=="Airy (1830)" :
            set_text(ent_a,6377563.396)
            set_text(ent_b,6356256.909)
        
        elif value=="Bessel (1841)" :
            set_text(ent_a,6377397.155)
            set_text(ent_b,6356078.963)
        
        elif value=="Clarke (1866)" :
            set_text(ent_a,6378206.4)
            set_text(ent_b,6356583.8)
        
        elif value=="Clarke (1878)" :
            set_text(ent_a,6378190)
            set_text(ent_b,6356456)
        
        elif value=="Clarke (1880)" :
            set_text(ent_a,6378249.145)
            set_text(ent_b,6356514.870)

        elif value=="Helmert (1906)" :
            set_text(ent_a,6378200)
            set_text(ent_b,6356818.17)
        
        elif value=="Hayford (1910)" :
            set_text(ent_a,6378388)
            set_text(ent_b,6356911.946)
        
        elif value=="International (1924)" :
            set_text(ent_a,6378245)
            set_text(ent_b,6356911.946)
        
        elif value=="Krassovsky (1940)" :
            set_text(ent_a,6378245)
            set_text(ent_b,6356863.019)
        
        elif value=="WGS66 (1966)" :
            set_text(ent_a,6378145)
            set_text(ent_b,6356759.769)
        
        elif value=="Australian National (1966)" :
            set_text(ent_a,6378160)
            set_text(ent_b,6356774.719)
        elif value=="New International (1967)" :
            set_text(ent_a,6378157.5)
            set_text(ent_b,6356772.2)
    
        elif value=="GRS-67 (1967)" :
            set_text(ent_a,6378160)
            set_text(ent_b,6356774.516)
        
        elif value=="South American (1969)" :
            set_text(ent_a,6378160)
            set_text(ent_b,6356774.719)

        elif value=="WGS-72 (1972)" :
            set_text(ent_a,6378135)
            set_text(ent_b,6356750.52)
        
        elif value=="GRS-80 (1979)" :
            set_text(ent_a,6378137)
            set_text(ent_b,6356752.3141)
        
        elif value=="WGS-84 (1984)" :
            set_text(ent_a,6378137)
            set_text(ent_b,6356752.3142)
        
        elif value=="IERS (1989)" :
            set_text(ent_a,6378136)
            set_text(ent_b,6356751.302)

        elif value=="IERS (2003)" :
            set_text(ent_a,6378136.6)
            set_text(ent_b,6356751.9)
        else:
            messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")  
            
    tk0 = Tk()
    tk0.geometry("378x170")
    tk0.title("Chose_datum")
    tk0.iconbitmap('Ressources/favicon.ico')
    tt = Test(tk0)
    tk0.mainloop()

    
def g1et_coordonnees_geocentriques():
  
    global entry3,entry4,entry5,entry2,entry6,canvas1,Mafenetre1
    
    try:
        Lambda,Phi,h,a,b=float(entry3.get()),float(entry6.get()),float(entry2.get()),float(entry4.get()),float(entry5.get())

        label7 = Label(Mafenetre1 ,text= 'x(m) :')
        label7.config(font=('Arial', 10))
        canvas1.create_window(350, 60, window=label7)
    
        label9 = Label(Mafenetre1 , text= 'y(m) :',font=('Arial', 10))
        canvas1.create_window(350,100, window=label9)
    
        label11 = Label(Mafenetre1 , text= 'z(m) :',font=('Arial', 10))
        canvas1.create_window(350, 140, window=label11)
    
        if b<=a and 0<a and 0<b:
            if Phi<=90 and -90<=Phi:
                 if Lambda<=180 and -180<=Lambda:
                    
                     x,y,z=transformation_cor_Geodisiques_Geocentriques(Lambda,Phi,h,a,b)
                     label8 = Label(Mafenetre1, text= "{:011.5f}".format(x) ,font=('Arial', 10, 'bold'))
                     canvas1.create_window(450, 60, window=label8)
                     label10 = Label(Mafenetre1, text= "{:011.5f}".format(y) ,font=('Arial', 10, 'bold'))
                     canvas1.create_window(450, 100, window=label10)
                     label12 = Label(Mafenetre1, text= "{:011.5f}".format(z) ,font=('Arial', 10, 'bold'))
                     canvas1.create_window(450, 140, window=label12)


                     coords = (Phi,Lambda)
                     map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=5)

                     coords = [Phi,Lambda]
                     folium.Marker(location=coords, popup = "").add_to(map)
                     map.save('indexx.html')
                    
                    
                 else:
                   messagebox.showerror('domain error ',""" verifier lamda""")
            else:
               messagebox.showerror('domain error ',""" verifier phi """)
        else:
            messagebox.showerror('domain error ',""" saisir a et b correctement""")
        
            
    except ValueError:
                messagebox.showerror('domain error',"""vous devez remplir toutes les cases """)

def geocoder1():
        global entry2,entry3,entry4,entry5,entry6,canvas1,Mafenetre1
        try:
                Lambda,Phi = float(entry3.get()),float(entry6.get())
                geolocator = Nominatim(user_agent="geoapiExercises")
                Latitude = str(Phi)
                Longitude = str(Lambda)
                location = geolocator.reverse((Latitude+","+Longitude),language='en')
                address = location.raw['address']
                label13 = Label(Mafenetre1 , text= 'country :',font=('Arial', 10))
                canvas1.create_window(350, 180, window=label13)
            
                label14 = Label(Mafenetre1, text=address.get('country', '') ,font=('Arial', 10, 'bold'))
                canvas1.create_window(450, 180, window=label14,tags="label")
                
        except ValueError:
                messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez""")

        except AttributeError:
                 messagebox.showerror('error',"""on n'a pas pus localiser ce pays!""")


def map3d1():
            global entry2,entry3,entry4,entry5,entry6,canvas1,Mafenetre1
            try:
                Lambda,Phi,h,a,b=float(entry3.get()),float(entry6.get()),float(entry2.get()),float(entry4.get()),float(entry5.get())
           
                if b<=a and 0<a and 0<b:
                  if Phi<=90 and -90<=Phi:
                     if Lambda<=180 and -180<=Lambda:
                        
                         x,y,z=transformation_cor_Geodisiques_Geocentriques(Lambda,Phi,h,a,b)
                         phi = np.linspace(0, 2*pi)
                         theta = np.linspace(-pi/2, pi/2)
                         phi, theta=np.meshgrid(phi, theta)
                         X = cos(theta) * sin(phi) * a
                         Y = cos(theta) * cos(phi) * a
                         Z = sin(theta)*b
                         fig = go.Figure(data=[go.Surface(x = X, y = Y, z=Z)])
                         fig.update_layout(width=900, height=900);
                         fig.update_traces(contours_z=dict(show=True, usecolormap=True,highlightcolor="limegreen", project_z=False))
                         xdata =np.linspace(x,x,1)
                         ydata = np.linspace(y,y,1)
                         zdata = np.linspace(z,z,1)
                         fig.add_scatter3d(x=xdata, y=ydata, z=zdata, mode='markers')
                         fig.show()
                        
                     else:
                       messagebox.showerror('domain error ',""" verifier lamda""")
                  else:
                   messagebox.showerror('domain error ',""" verifier phi """)
                else:
                 messagebox.showerror('domain error ',""" saisir a et b correctement""")
        
            
            except ValueError:
                messagebox.showerror('domain error',"""vous devez remplir toutes les cases """)
            

## geocentrique vers geodesique

def Transformation_coor_Geocentriques_Geodesiques(x,y,z,a,b,eps):
    
    e=sqrt(1-(b/a)**2)

    if x==0 and y==0 :
            Laambda=0
            h=abs(z)-b
            if z<0:
                phi1=-pi/2
                phi1=phi1*180/pi
            elif z==0:
                phi1=0
            else :
                phi1=pi/2
                phi1=phi1*180/pi
    else :
            if x>0:
                Laambda=atan(y/x)
            elif x<0 and y>=0 :
                Laambda=atan(y/x) + pi
            elif y<0 and x<0 :
                Laambda=atan(y/x) - pi
            elif y>0 and x==0 :
                Laambda=pi/2
            elif y<0 and x==0 :
                Laambda=-pi/2
            Laambda=Laambda*180/pi 
            h=0
            phi=atan(z/((1-e**2)*sqrt(x**2+y**2)))
            N=a/sqrt(1-(e*sin(phi))**2)
            phi1=atan((z+ N*e**2*sin(phi))/sqrt(x**2+y**2))
            N=a/sqrt(1-(e*sin(phi1))**2)
            while abs(phi1-phi)>eps :
                phi=phi1
                phi1=atan((z+ N*e**2*sin(phi))/sqrt(x**2+y**2))
                N=a/sqrt(1-(e*sin(phi1))**2)
            if phi1 == pi/2 or phi == -pi/2 :
                h=(z/sin(phi1))-N*(1-e**2)
            else:
                h=sqrt(x**2+y**2)/cos(phi1)-N
            phi1=phi1*180/pi      

    return Laambda,phi1,h

def  geocentriques_vers_Geodesiques():
    
    global entry2_1,entry2_2,entry2_3,entry2_4,entry2_5,canvas2,Mafenetre2,entry2_6
    
    Mafenetre2 = Tk()
    Mafenetre2.geometry('900x350')
    Mafenetre2.iconbitmap('Ressources/favicon.ico')
    Mafenetre2.title('Geocentriques_vers_Geodesiques')

    canvas2 = Canvas(Mafenetre2, width = 600, height = 500, relief = 'groove')
    canvas2.pack()
    
    canvas2.create_line(300, 35, 300, 220, dash=(4, 2))
    canvas2.create_line(305, 35, 305, 220, dash=(4, 2))
    
    label1= Label(Mafenetre2, text='Transformation entre coordonnees:\n Géocentriques vers Géodesiques')
    label1.config(font=('Broadway', 18  ,'bold'),fg='#8B4513')
    canvas2.create_window(200, 25, window=label1)

    label2 = Label(Mafenetre2, text='x(m) :')
    label2.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas2.create_window(1, 60, window=label2)

    entry2_1 = Entry(Mafenetre2) 
    canvas2.create_window(200, 60, window=entry2_1)

    label3 = Label(Mafenetre2, text='y(m) :')
    label3.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas2.create_window(1, 90, window=label3)

    entry2_2 = Entry(Mafenetre2) 
    canvas2.create_window(200, 90, window=entry2_2)

    label4 = Label(Mafenetre2, text='z(m) :')
    label4.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas2.create_window(1, 120, window=label4)

    entry2_3 = Entry(Mafenetre2) 
    canvas2.create_window(200, 120, window=entry2_3)

    label5 = Label(Mafenetre2, text='Demi-grand axe a (m) :')
    label5.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas2.create_window(1, 150, window=label5)

    entry2_4 = Entry(Mafenetre2) 
    canvas2.create_window(200, 150, window=entry2_4)

    label6 = Label(Mafenetre2, text='Demi-petit axe b (m) :')
    label6.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas2.create_window(1, 180, window=label6)

    entry2_5 = Entry(Mafenetre2) 
    canvas2.create_window(200, 180, window=entry2_5)

    label7 = Label(Mafenetre2, text='Epsilon :')
    label7.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas2.create_window(1,210, window=label7)

    entry2_6 = Entry(Mafenetre2) 
    canvas2.create_window(200, 210, window=entry2_6)

    Button3 = Button(Mafenetre2,text='Transformer', command = g2et_coordonnees_Geodesiques ,bg='#8B795E',fg='#FDFEFE', font=('Arial', 9, 'bold'))
    canvas2.create_window(200, 240, window=Button3)
    
    Btn2 = Button(Mafenetre2, text = "Choisissez un datum",command = ellipsoide,bg='#8B795E',fg='#FDFEFE',font=('Arial', 9, 'bold'))
    canvas2.create_window(30, 240, window=Btn2)

    Btn3= Button(Mafenetre2, text = 'show map', command = openweb3 ,bg='#8B795E',fg='#FDFEFE', font=('Arial', 9, 'bold'))
    canvas2.create_window(1, 270, window=Btn3)

    Btn4= Button(Mafenetre2, text = 'localisation', command = geocoder2 ,bg='#8B795E',fg='#FDFEFE', font=('Arial', 9, 'bold'))
    canvas2.create_window(100, 270, window=Btn4)

    Btn5= Button(Mafenetre2, text = 'visualisation 3D', command =map3d2 ,bg='#8B795E',fg='#FDFEFE', font=('Arial', 9, 'bold'))
    canvas2.create_window(200, 270, window=Btn5)
    
    Mafenetre2.mainloop()




def ellipsoide():
    
    class Test:
        
      def __init__(self, tk0):
        self.var = StringVar()
        fontCombo = ("Ink Free", 16, "bold")
        self.data = ("Maupertuis (1738)","Plessis (1817)","Everest (1830)","Everest 1830 Modified (1967)","Airy (1830)","Bessel (1841)","Clarke (1866)","Clarke (1878)","Clarke (1880)","Helmert (1906)","Hayford (1910)","International (1924)","Krassovsky (1940)","WGS66 (1966)","Australian National (1966)","New International (1967)","GRS-67 (1967)","South American (1969)","WGS-72 (1972)","GRS-80 (1979)","WGS-84 (1984)","IERS (1989)","IERS (2003)")
        self.cb = Combobox(tk0, values=self.data,font = fontCombo)
        self.cb.place(x=50, y=50)
        self.b1 = Button(tk0, text="Réactualiser", command=lambda:[self.select(),tk0.destroy()],bg='#8B795E',fg='#FDFEFE',font=('Arial', 9, 'bold')).place(x=160, y=110)

      def set_text(Entry,text):   
        Entry.delete(0,END)
        Entry.insert(0,text)
        return
    
      def select(self):
        value = self.cb.get()
        ent_a=entry2_4
        ent_b=entry2_5
        if value=="Maupertuis (1738)" :
            set_text(ent_a,6397300)
            set_text(ent_b,6363806.283)
        
        elif value=="Plessis (1817)" :
            set_text(ent_a,6376523.0)
            set_text(ent_b,6355862.9333)
        
        elif value=="Everest (1830)" :
            set_text(ent_a,6377299.365)
            set_text(ent_b,6356098.359)
        
        elif value=="Everest 1830 Modified (1967)" :
            set_text(ent_a,6377304.063)
            set_text(ent_b,6356103.0390)
        
        elif value=="Everest 1830 (1967 Definition)" :
            set_text(ent_a,6377298.556)
            set_text(ent_b,6356097.550)
        
        elif value=="Airy (1830)" :
            set_text(ent_a,6377563.396)
            set_text(ent_b,6356256.909)
        
        elif value=="Bessel (1841)" :
            set_text(ent_a,6377397.155)
            set_text(ent_b,6356078.963)
        
        elif value=="Clarke (1866)" :
            set_text(ent_a,6378206.4)
            set_text(ent_b,6356583.8)
        
        elif value=="Clarke (1878)" :
            set_text(ent_a,6378190)
            set_text(ent_b,6356456)
        
        elif value=="Clarke (1880)" :
            set_text(ent_a,6378249.145)
            set_text(ent_b,6356514.870)

        elif value=="Helmert (1906)" :
            set_text(ent_a,6378200)
            set_text(ent_b,6356818.17)
        
        elif value=="Hayford (1910)" :
            set_text(ent_a,6378388)
            set_text(ent_b,6356911.946)
        
        elif value=="International (1924)" :
            set_text(ent_a,6378245)
            set_text(ent_b,6356911.946)
        
        elif value=="Krassovsky (1940)" :
            set_text(ent_a,6378245)
            set_text(ent_b,6356863.019)
        
        elif value=="WGS66 (1966)" :
            set_text(ent_a,6378145)
            set_text(ent_b,6356759.769)
             
        elif value=="Australian National (1966)" :
            set_text(ent_a,6378160)
            set_text(ent_b,6356774.719)
        
        elif value=="New International (1967)" :
            set_text(ent_a,6378157.5)
            set_text(ent_b,6356772.2)
    
        elif value=="GRS-67 (1967)" :
            set_text(ent_a,6378160)
            set_text(ent_b,6356774.516)
        
        elif value=="South American (1969)" :
            set_text(ent_a,6378160)
            set_text(ent_b,6356774.719)

        elif value=="WGS-72 (1972)" :
            set_text(ent_a,6378135)
            set_text(ent_b,6356750.52)
        
        elif value=="GRS-80 (1979)" :
            set_text(ent_a,6378137)
            set_text(ent_b,6356752.3141)
        
        elif value=="WGS-84 (1984)" :
            set_text(ent_a,6378137)
            set_text(ent_b,6356752.3142)
        
        elif value=="IERS (1989)" :
            set_text(ent_a,6378136)
            set_text(ent_b,6356751.302)

        elif value=="IERS (2003)" :
            set_text(ent_a,6378136.6)
            set_text(ent_b,6356751.9)
        else:
          messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")  
    tk0 = Tk()
    tk0.geometry("378x170")
    tk0.title("Chose_ellipsoid")
    tk0.iconbitmap('Ressources/favicon.ico')
    tt = Test(tk0)
    tk0.mainloop()
    
def g2et_coordonnees_Geodesiques():
    
   global entry2_1,entry2_2,entry2_3,entry2_4,entry2_5,canvas2,Mafenetre2,entry2_6
   try:
        
        x,y,z,a,b,Epsilon=float(entry2_1.get()),float(entry2_2.get()),float(entry2_3.get()),float(entry2_4.get()),float(entry2_5.get()),float(entry2_6.get())
        Lambda2,Phi2,h=Transformation_coor_Geocentriques_Geodesiques(x,y,z,a,b,Epsilon)
    
        label7 = Label(Mafenetre2, text= 'La longitude Lambda (°) :',font=('Arial', 10))
        canvas2.create_window(450, 60, window=label7)
    
        label9 = Label(Mafenetre2, text= 'La latitude Phi (°) :',font=('Arial', 10))
        canvas2.create_window(450, 100, window=label9)

        label11 = Label( Mafenetre2,text= 'La hauteur ellipsoidale h (m) :',font=('Arial', 10))
        canvas2.create_window(450, 140, window=label11)
    

        if b<=a and 0<a and 0<b:
                        Lambda2,Phi2,h=Transformation_coor_Geocentriques_Geodesiques(x,y,z,a,b,Epsilon)
                        
                        label8 = Label(Mafenetre2, text= "{:05.5f}".format(Lambda2) ,font=('Arial', 10, 'bold'))
                        canvas2.create_window(550, 60, window=label8)
                        
                        label10 = Label(Mafenetre2, text= "{:05.5f}".format(Phi2) ,font=('Arial', 10, 'bold'))
                        canvas2.create_window(550, 100, window=label10)
                        
                        label12 = Label(Mafenetre2, text= "{:011.5f}".format(h) ,font=('Arial', 10, 'bold'))
                        canvas2.create_window(550, 140, window=label12)

                        coords = (Phi2,Lambda2)
                        map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=5)

                        coords = [Phi2,Lambda2]
                        folium.Marker(location=coords, popup = "").add_to(map)
                        map.save('indexx.html')
        else:
            messagebox.showerror('domain error',"""saisir a et b correctement""")
            
   except:
       messagebox.showerror('domain error',"""remplisser toutes les cases""")
        
def geocoder2():
        global entry2_1,entry2_2,entry2_3,entry2_4,entry2_5,canvas2,Mafenetre2,entry2_6
        try:
                x,y,z,a,b,Epsilon=float(entry2_1.get()),float(entry2_2.get()),float(entry2_3.get()),float(entry2_4.get()),float(entry2_5.get()),float(entry2_6.get())
                Lambda2,Phi2,h=Transformation_coor_Geocentriques_Geodesiques(x,y,z,a,b,Epsilon)
                geolocator = Nominatim(user_agent="geoapiExercises")
                Latitude = str(Phi2)
                Longitude = str(Lambda2)
                location = geolocator.reverse((Latitude+","+Longitude),language='en')
                address = location.raw['address']
                label13 = Label(Mafenetre2 , text= 'country :',font=('Arial', 10))
                canvas2.create_window(350, 180, window=label13)
            
                label14 = Label(Mafenetre2, text=address.get('country', '') ,font=('Arial', 10, 'bold'))
                canvas2.create_window(450, 180, window=label14)
        
        except ValueError:
                messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez""")

        except AttributeError:
                 messagebox.showerror('error',"""on n'a pas pus localiser ce pays!""")


def map3d2():
            global  entry2_1,entry2_2,entry2_3,entry2_4,entry2_5,canvas2,Mafenetre2,entry2_6
            try:
                x2,y2,z2,a,b,Epsilon=float(entry2_1.get()),float(entry2_2.get()),float(entry2_3.get()),float(entry2_4.get()),float(entry2_5.get()),float(entry2_6.get())
           
                   
                phi = np.linspace(0, 2*pi)
                theta = np.linspace(-pi/2, pi/2)
                phi, theta=np.meshgrid(phi, theta)
                X = cos(theta) * sin(phi) * a
                Y = cos(theta) * cos(phi) * a
                Z = sin(theta)*b
                fig = go.Figure(data=[go.Surface(x = X, y = Y, z=Z)])
                fig.update_layout(width=900, height=900);
                fig.update_traces(opacity=0.5,contours_z=dict(show=True, usecolormap=True,highlightcolor="limegreen", project_z=False))
                xdata =np.linspace(x2,x2,1)
                ydata = np.linspace(y2,y2,1)
                zdata = np.linspace(z2,z2,1)
                fig.add_scatter3d(x=xdata, y=ydata, z=zdata, mode='markers')
                fig.show()
            except:
                messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirezEn cas d'ambiguité consulter le guide d'utilisation""")



##    geocentrique vers astronomique

def Transformation_coor_Geocentriques_Astronomique(Phi3,Lambda3,DeltaX3,DeltaY3,DeltaZ3):

       
            Phi3=degree2radians(Phi3)
            Lambda3=degree2radians(Lambda3)
            M=[0,0,0]
            a=-sin(Phi3)*cos(Lambda3)
            b=-sin(Lambda3)
            c=cos(Phi3)*cos(Lambda3)
            d=-sin(Phi3)*sin(Lambda3)
            e=cos(Lambda3)
            f=cos(Phi3)*sin(Lambda3)
            g=cos(Phi3)
            h=0
            i=sin(Phi3)
            V1=a*DeltaX3+d*DeltaY3+g*DeltaZ3
            V2=b*DeltaX3+e*DeltaY3
            V3=c*DeltaX3+f*DeltaY3+i*DeltaZ3
        
            if V1>0 :
                Az3=atan(V2/V1)
                       
            elif V1<0 and V2>=0 :
                 Az3=(atan(V2/V1)+pi)
            elif V1<0 and V2<0 :
                 Az3=(atan(V2/V1)-pi)
            elif V2>0 and V1==0 :
                 Az3=pi
            elif V2<0 and V1==0 :
                 Az3=-pi
            else :
                  Az3=0
            if Az3<0:
                Az3=Az3+2*pi

            M[0]=Az3
            M[0]=radians2degree(M[0])

            C3=sqrt(DeltaX3**2+DeltaY3**2+DeltaZ3**2)
           
            
            if  C3 !=0 and (V3/C3)<=1 and  (V3/C3)>=-1 :
                
                M[1]=asin((V3/C3))
                M[1]=radians2degree(M[1])
                
            else :
                M[1]='Av ne peut pas etre calculé'
            
            M[0]=Az3
            M[2]=C3
            M[0]=radians2degree(M[0])
            return M[0],M[1],M[2] 
      
def   Geocentrique_vers_Astronomique():
    
    global entry3_2,entry3_1,entry3_3,entry3_4,entry3_5,canvas3,Mafenetre3,entry3_6,entry3_7,entry3_8
    
    Mafenetre3 = Tk()
    Mafenetre3.geometry('900x350')
    Mafenetre3.iconbitmap('Ressources/favicon.ico')
    Mafenetre3.title('Geocentrique_vers_Astronomique_locales')

    canvas3 = Canvas(Mafenetre3, width = 600, height = 500, relief = 'raised')
    canvas3.pack()
    canvas3.create_line(300, 35, 300, 220, dash=(4, 2))
    canvas3.create_line(305, 35, 305, 220, dash=(4, 2))

    canvas3.create_line(10, 250, 300, 250, dash=(4, 2))
    canvas3.create_line(10, 250, 305, 250, dash=(4, 2))
    
    label1 = Label(Mafenetre3, text='Transformation entre coordonnees:\n Géocentriques vers Astronomiques locales')
    label1.config(font=('Broadway', 18  ,'bold'),fg='#8B4513')
    canvas3.create_window(200, 25, window=label1)

    label2 = Label(Mafenetre3, text='La longitude Lambda (°)')
    label2.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas3.create_window(1, 60, window=label2)
    
    entry3_1 = Entry(Mafenetre3)
    canvas3.create_window(200, 60, window=entry3_1)

   
    label3 = Label(Mafenetre3, text='La latitude Phi(°) :')
    label3.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas3.create_window(1, 90, window=label3)
    
    entry3_2 = Entry(Mafenetre3) 
    canvas3.create_window(200, 90, window=entry3_2)

    label4 = Label(Mafenetre3, text='DeltaXpq (m) :')
    label4.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas3.create_window(1, 120, window=label4)
    
    entry3_3 = Entry(Mafenetre3) 
    canvas3.create_window(200, 120, window=entry3_3)

    label5 = Label(Mafenetre3, text='DeltaYpq (m) :')
    label5.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas3.create_window(1, 150, window=label5)
    entry3_4 = Entry(Mafenetre3) 
    canvas3.create_window(200, 150, window=entry3_4)

    label6 = Label(Mafenetre3, text='DeltaZpq (m) :')
    label6.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas3.create_window(1, 180, window=label6)
    
    entry3_5 = Entry(Mafenetre3) 
    canvas3.create_window(200, 180, window=entry3_5)


    Button3 = Button(Mafenetre3,text='Transformer', command = g3et_coordonnees_astronomique ,bg='#8B795E',fg='#FDFEFE', font=('Arial', 9, 'bold'))
    canvas3.create_window(200, 220,window=Button3)



    Btn3= Button(Mafenetre3, text = 'show map', command = openweb3 ,bg='#8B795E',fg='#FDFEFE', font=('Arial', 9, 'bold'))
    canvas3.create_window(30, 220, window=Btn3)



    Mafenetre3.mainloop()
    

   
    Mafenetre3.mainloop()



def ellipsoide3():
    
    class Test:
        
      def __init__(self, tk0):
        self.var = StringVar()
        fontCombo = ("Ink Free", 16, "bold")
        self.data = ("Maupertuis (1738)","Plessis (1817)","Everest (1830)","Everest 1830 Modified (1967)","Airy (1830)","Bessel (1841)","Clarke (1866)","Clarke (1878)","Clarke (1880)","Helmert (1906)","Hayford (1910)","International (1924)","Krassovsky (1940)","WGS66 (1966)","Australian National (1966)","New International (1967)","GRS-67 (1967)","South American (1969)","WGS-72 (1972)","GRS-80 (1979)","WGS-84 (1984)","IERS (1989)","IERS (2003)")
        self.cb = Combobox(tk0, values=self.data,font = fontCombo)
        self.cb.place(x=50, y=50)
        self.b1 = Button(tk0, text="Réactualiser", command=lambda:[self.select(),tk0.destroy()],bg='#8B795E',fg='#FDFEFE',font=('Arial', 9, 'bold')).place(x=160, y=110)

      def set_text(Entry,text):   
        Entry.delete(0,END)
        Entry.insert(0,text)
        return
    
      def select(self):
        value = self.cb.get()
        ent_a=entry3_6
        ent_b=entry3_7
        if value=="Maupertuis (1738)" :
            set_text(ent_a,6397300)
            set_text(ent_b,6363806.283)
        
        elif value=="Plessis (1817)" :
            set_text(ent_a,6376523.0)
            set_text(ent_b,6355862.9333)
        
        elif value=="Everest (1830)" :
            set_text(ent_a,6377299.365)
            set_text(ent_b,6356098.359)
        
        elif value=="Everest 1830 Modified (1967)" :
            set_text(ent_a,6377304.063)
            set_text(ent_b,6356103.0390)
        
        elif value=="Everest 1830 (1967 Definition)" :
            set_text(ent_a,6377298.556)
            set_text(ent_b,6356097.550)
        
        elif value=="Airy (1830)" :
            set_text(ent_a,6377563.396)
            set_text(ent_b,6356256.909)
        
        elif value=="Bessel (1841)" :
            set_text(ent_a,6377397.155)
            set_text(ent_b,6356078.963)
        
        elif value=="Clarke (1866)" :
            set_text(ent_a,6378206.4)
            set_text(ent_b,6356583.8)
        
        elif value=="Clarke (1878)" :
            set_text(ent_a,6378190)
            set_text(ent_b,6356456)
        
        elif value=="Clarke (1880)" :
            set_text(ent_a,6378249.145)
            set_text(ent_b,6356514.870)

        elif value=="Helmert (1906)" :
            set_text(ent_a,6378200)
            set_text(ent_b,6356818.17)
        
        elif value=="Hayford (1910)" :
            set_text(ent_a,6378388)
            set_text(ent_b,6356911.946)
        
        elif value=="International (1924)" :
            set_text(ent_a,6378245)
            set_text(ent_b,6356911.946)
        
        elif value=="Krassovsky (1940)" :
            set_text(ent_a,6378245)
            set_text(ent_b,6356863.019)
        
        elif value=="WGS66 (1966)" :
            set_text(ent_a,6378145)
            set_text(ent_b,6356759.769)
             
        elif value=="Australian National (1966)" :
            set_text(ent_a,6378160)
            set_text(ent_b,6356774.719)
        
        elif value=="New International (1967)" :
            set_text(ent_a,6378157.5)
            set_text(ent_b,6356772.2)
    
        elif value=="GRS-67 (1967)" :
            set_text(ent_a,6378160)
            set_text(ent_b,6356774.516)
        
        elif value=="South American (1969)" :
            set_text(ent_a,6378160)
            set_text(ent_b,6356774.719)

        elif value=="WGS-72 (1972)" :
            set_text(ent_a,6378135)
            set_text(ent_b,6356750.52)
        
        elif value=="GRS-80 (1979)" :
            set_text(ent_a,6378137)
            set_text(ent_b,6356752.3141)
        
        elif value=="WGS-84 (1984)" :
            set_text(ent_a,6378137)
            set_text(ent_b,6356752.3142)
        
        elif value=="IERS (1989)" :
            set_text(ent_a,6378136)
            set_text(ent_b,6356751.302)

        elif value=="IERS (2003)" :
            set_text(ent_a,6378136.6)
            set_text(ent_b,6356751.9)
        else:
          messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")  
    tk0 = Tk()
    tk0.geometry("378x170")
    tk0.title("Chose_ellipsoid")
    tk0.iconbitmap('Ressources/favicon.ico')
    tt = Test(tk0)
    tk0.mainloop()
def g3et_coordonnees_astronomique():
  
         global entry3_1,entry3_2,entry3_3,entry3_4,entry3_5,canvas3,Mafenetre3

        
         Lambda3,Phi3,DeltaX3,DeltaY3,DeltaZ3=float(entry3_1.get()),float(entry3_2.get()),float(entry3_3.get()),float(entry3_4.get()),float(entry3_5.get())
    


         label7 = Label(Mafenetre3 ,text= 'Azimut astronomique Apq (°) :')
         label7.config(font=('Arial', 10))
         canvas3.create_window(450, 60, window=label7)
    


         label9 = Label(Mafenetre3 , text= 'Distance entre P et Q Cpq (m) :',font=('Arial', 10))
         canvas3.create_window(450, 100, window=label9)
    


         label11 = Label(Mafenetre3 , text= 'Angle vertical Vpq (°) :',font=('Arial', 10))
         canvas3.create_window(450, 140, window=label11)
    

         if Phi3<=90 and -90<=Phi3:
            if Lambda3<=180 and -180<=Lambda3:
                    Az3,Av3,C3=Transformation_coor_Geocentriques_Astronomique(Phi3,Lambda3,DeltaX3,DeltaY3,DeltaZ3)
                    label8 = Label(Mafenetre3, text= "{:06.5f}".format(Az3) ,font=('Arial', 10, 'bold'))
                    canvas3.create_window(600, 60, window=label8)
                    label10 = Label(Mafenetre3, text= "{:011.5f}".format(C3) ,font=('Arial', 10, 'bold'))
                    canvas3.create_window(600, 100, window=label10)
                    label12 = Label(Mafenetre3, text= "{:011.5f}".format(Av3) ,font=('Arial', 10, 'bold'))
                    canvas3.create_window(600, 140, window=label12)



                    coords = (Phi3,Lambda3)
                    map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=5)

                    coords = [Phi3,Lambda3]
                    folium.Marker(location=coords, popup = "").add_to(map)
                    map.save('indexx.html')

            else:
                messagebox.showerror('domain error ',""" verifier lamda""")
         else:
            messagebox.showerror('domain error ',""" verifier phi """)




def map3d3():
            global entry3_1,entry3_2,entry3_3,entry3_4,entry3_5,canvas3,Mafenetre3,entry3_6,entry3_7,entry3_8

        
            Lambda,Phi,h,a,b=float(entry3_1.get()),float(entry3_2.get()),float(entry3_8.get()),float(entry3_6.get()),float(entry3_7.get())
            try:
                x3,y3,z3=transformation_cor_Geodisiques_Geocentriques(Lambda,Phi,h,a,b)

         

                
                   
                phi = np.linspace(0, 2*pi)
                theta = np.linspace(-pi/2, pi/2)
                phi, theta=np.meshgrid(phi, theta)
                X = cos(theta) * sin(phi) * a
                Y = cos(theta) * cos(phi) * a
                Z = sin(theta)*b
                fig = go.Figure(data=[go.Surface(x = X, y = Y, z=Z)])
                fig.update_layout(width=900, height=900);
                fig.update_traces(opacity=0.5,contours_z=dict(show=True, usecolormap=True,highlightcolor="lightblue", project_z=False))
                xdata =np.linspace(x3,x3,1)
                ydata = np.linspace(y3,y3,1)
                zdata = np.linspace(z3,z3,1)
                fig.add_scatter3d(x=xdata, y=ydata, z=zdata, mode='markers')
                fig.show()
            except:
               messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
##En cas d'ambiguité consulter le guide d'utilisation""")

        





            
  
## astronomique vers geocentrique


def Transformation_coor_Astronomique_Geocentriques(phi,Laambda,az,av,c) :

        phi=degree2radians(phi)
        Laambda=degree2radians(Laambda)
        az=degree2radians(az)
        av=degree2radians(av)
            
        l=[]
        v1=c*cos(av)*cos(az)
        v2=c*cos(av)*sin(az)
        v3=c*sin(av)
        a=-sin(phi)*cos(Laambda)
        b=-sin(Laambda)
        C=cos(phi)*cos(Laambda)
        d=-sin(phi)*sin(Laambda)
        e=cos(Laambda)
        f=cos(phi)*sin(Laambda)
        g=cos(phi)
        h=0
        i=sin(phi)
        x=a*v1+b*v2+C*v3
        y=d*v1+e*v2+f*v3
        z=g*v1+h*v2+i*v3
        l.append(x)
        l.append(y)
        l.append(z)
            
        return l[0],l[1],l[2]



def   Astronomique_vers_Geocentrique():
    

    global entry4_1,entry4_2,entry4_3,entry4_4,entry4_5,canvas4,Mafenetre4,entry4_6,entry4_7,entry4_8
    
    Mafenetre4 = Tk()
    Mafenetre4.geometry('900x350')
    Mafenetre4.iconbitmap('Ressources/favicon.ico')
    Mafenetre4.title('Astronomique_locale_vers_Geocentrique')

    canvas4 = Canvas(Mafenetre4, width = 600, height = 500, relief = 'raised')
    canvas4.pack()
    canvas4.create_line(300, 35, 300, 220, dash=(4, 2))
    canvas4.create_line(305, 35, 305, 220, dash=(4, 2))

    canvas4.create_line(10, 230, 300, 230, dash=(4, 2))
    canvas4.create_line(10, 230, 305, 230, dash=(4, 2))
    
    label1 = Label(Mafenetre4, text='Transformation entre coordonnees:\n Astronomiques locales  vers Géocentriques ')
    label1.config(font=('Broadway', 18  ,'bold'),fg='#8B4513')
    canvas4.create_window(200, 25, window=label1)

    label2 = Label(Mafenetre4, text='La longitude Lambda (°)')
    label2.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas4.create_window(1, 60, window=label2)
    
    entry4_1 = Entry(Mafenetre4)
    canvas4.create_window(200, 60, window=entry4_1)

   
    label3 = Label(Mafenetre4, text='La latitude Phi(°) :')
    label3.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas4.create_window(1, 90, window=label3)
    
    entry4_2 = Entry(Mafenetre4) 
    canvas4.create_window(200, 90, window=entry4_2)

    label4 = Label(Mafenetre4, text='Azimut astronomique Apq (°) :')
    label4.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas4.create_window(1, 120, window=label4)
    
    entry4_3 = Entry(Mafenetre4) 
    canvas4.create_window(200, 120, window=entry4_3)

    label5 = Label(Mafenetre4, text='Angle vertical Vpq (°) :')
    label5.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas4.create_window(1, 150, window=label5)
    entry4_4 = Entry(Mafenetre4) 
    canvas4.create_window(200, 150, window=entry4_4)

    label6 = Label(Mafenetre4, text='Distance entre P et Q Cpq (m) :')
    label6.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas4.create_window(1, 180, window=label6)
    
    entry4_5 = Entry(Mafenetre4) 
    canvas4.create_window(200, 180, window=entry4_5)

    label6 = Label(Mafenetre4, text='grand axe a :')
    label6.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas4.create_window(1, 260, window=label6)
    
    entry4_6 = Entry(Mafenetre4) 
    canvas4.create_window(200, 260, window=entry4_6)

    label6 = Label(Mafenetre4, text='ptit axe b :')
    label6.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas4.create_window(1, 280, window=label6)
    
    entry4_7 = Entry(Mafenetre4) 
    canvas4.create_window(200, 280, window=entry4_7)

    label7 = Label(Mafenetre4, text='hauteur ellipsoidale :')
    label7.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas4.create_window(1, 300, window=label7)
    
    entry4_8 = Entry(Mafenetre4) 
    canvas4.create_window(200, 300, window=entry4_8)

    button2 = Button(Mafenetre4,text='Transformer', command = g4et_coordonnees_geocentrique ,bg='#8B795E',fg='#FDFEFE', font=('Arial', 9, 'bold'))
    canvas4.create_window(200, 210, window=button2)

    Btn2 = Button(Mafenetre4, text = "Choisissez un datum",command=ellipsoide4,bg='#8B795E',fg='#FDFEFE',font=('Arial', 9, 'bold'))
    canvas4.create_window(1, 330, window=Btn2)

    Btn3= Button(Mafenetre4, text = 'show map', command =openweb3 ,bg='#8B795E',fg='#FDFEFE', font=('Arial', 9, 'bold'))
    canvas4.create_window(1, 210, window=Btn3)

    Btn4= Button(Mafenetre4, text = 'localisation', command =geocoder4 ,bg='#8B795E',fg='#FDFEFE', font=('Arial', 9, 'bold'))
    canvas4.create_window(100, 210, window=Btn4)

    Btn5= Button(Mafenetre4, text = 'visualisation 3D', command =map3d4 ,bg='#8B795E',fg='#FDFEFE', font=('Arial', 9, 'bold'))
    canvas4.create_window(200, 330, window=Btn5)
    

    
    Mafenetre4.mainloop()



def ellipsoide4():
    
    class Test:
        
      def __init__(self, tk0):
        self.var = StringVar()
        fontCombo = ("Ink Free", 16, "bold")
        self.data = ("Maupertuis (1738)","Plessis (1817)","Everest (1830)","Everest 1830 Modified (1967)","Airy (1830)","Bessel (1841)","Clarke (1866)","Clarke (1878)","Clarke (1880)","Helmert (1906)","Hayford (1910)","International (1924)","Krassovsky (1940)","WGS66 (1966)","Australian National (1966)","New International (1967)","GRS-67 (1967)","South American (1969)","WGS-72 (1972)","GRS-80 (1979)","WGS-84 (1984)","IERS (1989)","IERS (2003)")
        self.cb = Combobox(tk0, values=self.data,font = fontCombo)
        self.cb.place(x=50, y=50)
        self.b1 = Button(tk0, text="Réactualiser", command=lambda:[self.select(),tk0.destroy()],bg='#8B795E',fg='#FDFEFE',font=('Arial', 9, 'bold')).place(x=160, y=110)

      def set_text(Entry,text):   
        Entry.delete(0,END)
        Entry.insert(0,text)
        return
    
      def select(self):
        value = self.cb.get()
        ent_a=entry4_6
        ent_b=entry4_7
        if value=="Maupertuis (1738)" :
            set_text(ent_a,6397300)
            set_text(ent_b,6363806.283)
        
        elif value=="Plessis (1817)" :
            set_text(ent_a,6376523.0)
            set_text(ent_b,6355862.9333)
        
        elif value=="Everest (1830)" :
            set_text(ent_a,6377299.365)
            set_text(ent_b,6356098.359)
        
        elif value=="Everest 1830 Modified (1967)" :
            set_text(ent_a,6377304.063)
            set_text(ent_b,6356103.0390)
        
        elif value=="Everest 1830 (1967 Definition)" :
            set_text(ent_a,6377298.556)
            set_text(ent_b,6356097.550)
        
        elif value=="Airy (1830)" :
            set_text(ent_a,6377563.396)
            set_text(ent_b,6356256.909)
        
        elif value=="Bessel (1841)" :
            set_text(ent_a,6377397.155)
            set_text(ent_b,6356078.963)
        
        elif value=="Clarke (1866)" :
            set_text(ent_a,6378206.4)
            set_text(ent_b,6356583.8)
        
        elif value=="Clarke (1878)" :
            set_text(ent_a,6378190)
            set_text(ent_b,6356456)
        
        elif value=="Clarke (1880)" :
            set_text(ent_a,6378249.145)
            set_text(ent_b,6356514.870)

        elif value=="Helmert (1906)" :
            set_text(ent_a,6378200)
            set_text(ent_b,6356818.17)
        
        elif value=="Hayford (1910)" :
            set_text(ent_a,6378388)
            set_text(ent_b,6356911.946)
        
        elif value=="International (1924)" :
            set_text(ent_a,6378245)
            set_text(ent_b,6356911.946)
        
        elif value=="Krassovsky (1940)" :
            set_text(ent_a,6378245)
            set_text(ent_b,6356863.019)
        
        elif value=="WGS66 (1966)" :
            set_text(ent_a,6378145)
            set_text(ent_b,6356759.769)
             
        elif value=="Australian National (1966)" :
            set_text(ent_a,6378160)
            set_text(ent_b,6356774.719)
        
        elif value=="New International (1967)" :
            set_text(ent_a,6378157.5)
            set_text(ent_b,6356772.2)
    
        elif value=="GRS-67 (1967)" :
            set_text(ent_a,6378160)
            set_text(ent_b,6356774.516)
        
        elif value=="South American (1969)" :
            set_text(ent_a,6378160)
            set_text(ent_b,6356774.719)

        elif value=="WGS-72 (1972)" :
            set_text(ent_a,6378135)
            set_text(ent_b,6356750.52)
        
        elif value=="GRS-80 (1979)" :
            set_text(ent_a,6378137)
            set_text(ent_b,6356752.3141)
        
        elif value=="WGS-84 (1984)" :
            set_text(ent_a,6378137)
            set_text(ent_b,6356752.3142)
        
        elif value=="IERS (1989)" :
            set_text(ent_a,6378136)
            set_text(ent_b,6356751.302)

        elif value=="IERS (2003)" :
            set_text(ent_a,6378136.6)
            set_text(ent_b,6356751.9)
        else:
          messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")  
    tk0 = Tk()
    tk0.geometry("378x170")
    tk0.title("Chose_ellipsoid")
    tk0.iconbitmap('Ressources/favicon.ico')
    tt = Test(tk0)
    tk0.mainloop()
def g4et_coordonnees_geocentrique():
    
           global entry4_1,entry4_2,entry4_3,entry4_4,entry4_5,canvas4,Mafenetre4
           try:
            
               Lambda4,Phi4,Az4,Av4,C4=float(entry4_1.get()),float(entry4_2.get()),float(entry4_3.get()),float(entry4_4.get()),float(entry4_5.get())

               label7 = Label(Mafenetre4 ,text= 'DeltaXpq (m) :')
               label7.config(font=('Arial', 10))
               canvas4.create_window(400, 60, window=label7)
            
               label9 = Label(Mafenetre4 , text= 'DeltaYpq(m) :',font=('Arial', 10))
               canvas4.create_window(400, 100, window=label9)
            
               label11 = Label(Mafenetre4 , text= 'DeltaYpq (m) :',font=('Arial', 10))
               canvas4.create_window(400, 140, window=label11)
            
               if Phi4<=90 and -90<=Phi4:
                    if Lambda4<=180 and -180<=Lambda4:
                        if Az4<=360 and Az4>=0:
                            if Av4>=0 and Av4<90:
                                if C4>=0:
                                     DeltaX4,DeltaY4,DeltaZ4=Transformation_coor_Astronomique_Geocentriques(Phi4,Lambda4,Az4,Av4,C4)
                                     label8 = Label(Mafenetre4, text= "{:011.5f}".format(DeltaX4) ,font=('Arial', 10, 'bold'))
                                     canvas4.create_window(550, 60, window=label8)
                                     label10 = Label(Mafenetre4, text= "{:011.5f}".format(DeltaY4) ,font=('Arial', 10, 'bold'))
                                     canvas4.create_window(550, 100, window=label10)
                                     label12 = Label(Mafenetre4, text= "{:011.5f}".format(DeltaZ4) ,font=('Arial', 10, 'bold'))
                                     canvas4.create_window(550, 140, window=label12)


                                     coords = (Phi4,Lambda4)
                                     map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=5)

                                     coords = [Phi4,Lambda4]
                                     folium.Marker(location=coords, popup = "").add_to(map)
                                     map.save('indexx.html')
                                else:
                                     messagebox.showerror('domain error ',""" verifier c """)
                            else:
                                messagebox.showerror('domain error ',"""vérifier la valeur de av""")
                        else:
                            messagebox.showerror('domain error ',""" verifier az""")
                                     
                    else:
                        messagebox.showerror('domain error ',""" verifier lamda""")
               else:
                    messagebox.showerror('domain error ',""" verifier phi """)

           except ValueError:
                       messagebox.showerror('domain error',"""vous devez remplir toutes les cases """)
##

def geocoder4():
        global entry4_1,entry4_2,canvas4,Mafenetre4
        try:
                Lambda4,Phi4=float(entry4_1.get()),float(entry4_2.get())
                geolocator = Nominatim(user_agent="geoapiExercises")
                Latitude = str(Phi4)
                Longitude = str(Lambda4)
                location = geolocator.reverse((Latitude+","+Longitude),language='en')
                address = location.raw['address']
                label13 = Label(Mafenetre4 , text= 'country :',font=('Arial', 10))
                canvas4.create_window(350, 180, window=label13)
            
                label14 = Label(Mafenetre4, text=address.get('country', '') ,font=('Arial', 10, 'bold'))
                canvas4.create_window(450, 180, window=label14)
        
        except ValueError:
                messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez""")

        except AttributeError:
                 messagebox.showerror('error',"""on n'a pas pus localiser ce pays!""")

def map3d4():
            global entry4_1,entry4_2,canvas4,Mafenetre4,entry4_6,entry4_7,entry4_8

        
            Lambda,Phi,h,a,b=float(entry4_1.get()),float(entry4_2.get()),float(entry4_8.get()),float(entry4_6.get()),float(entry4_7.get())
            try:
                x4,y4,z4=transformation_cor_Geodisiques_Geocentriques(Lambda,Phi,h,a,b)

            
                if b<=a and 0<a and 0<b: 
                    if Phi<=90 and -90<=Phi:
                        if Lambda<=180 and -180<=Lambda:
                    
                                    phi = np.linspace(0, 2*pi)
                                    theta = np.linspace(-pi/2, pi/2)
                                    phi, theta=np.meshgrid(phi, theta)
                                    X = cos(theta) * sin(phi) * a
                                    Y = cos(theta) * cos(phi) * a
                                    Z = sin(theta)*b
                                    fig = go.Figure(data=[go.Surface(x = X, y = Y, z=Z)])
                                    fig.update_layout(width=900, height=900);
                                    fig.update_traces(opacity=0.5,contours_z=dict(show=True, usecolormap=True,highlightcolor="limegreen", project_z=False))
                                    xdata =np.linspace(x4,x4,1)
                                    ydata = np.linspace(y4,y4,1)
                                    zdata = np.linspace(z4,z4,1)
                                    fig.add_scatter3d(x=xdata, y=ydata, z=zdata, mode='markers')
                                    fig.show()
                        else:
                            messagebox.showerror('domain error ',""" verifier lamda""")
                    else:
                     messagebox.showerror('domain error ',""" verifier phi """)
                else:
                 messagebox.showerror('domain error ',""" saisir a et b correctement""")

            except ValueError:
                        messagebox.showerror('domain error',"""vous devez remplir toutes les cases """)
            
##Géodésique locales vers geocentrique  

def transformation_geodesique_locales_vers_geocentrique(lambdap,phip,alphapq,vpq,cpq):
    
    lambdap=degree2radians(lambdap)
    phip=degree2radians(phip)
    alphapq=degree2radians(alphapq)
    vpq=degree2radians(vpq)
    
    a=cpq*cos(vpq)*cos(alphapq)
    b=cpq*cos(vpq)*sin(alphapq)
    c=cpq*sin(vpq)
    
    DeltaXpq=-sin(phip)*cos(lambdap)*a-sin(lambdap)*b+c*cos(phip)*cos(lambdap)
    DeltaYpq=-sin(phip)*sin(lambdap)*a+cos(lambdap)*b+cos(phip)*sin(lambdap)*c
    DeltaZpq=cos(phip)*a+c*sin(phip)
    
    return DeltaXpq,DeltaYpq,DeltaZpq


def   geodesique_locales_vers_Geocentrique():
    
    global entry5_1,entry5_2,entry5_3,entry5_4,entry5_5,canvas5,Mafenetre5,entry5_6,entry5_7,entry5_8
    
    Mafenetre5 = Tk()
    Mafenetre5.geometry('900x350')
    Mafenetre5.iconbitmap('Ressources/favicon.ico')
    Mafenetre5.title('Géodésique_locales_vers_Géocentrique')

    canvas5 = Canvas(Mafenetre5, width = 600, height = 500, relief = 'raised')
    canvas5.pack()
    canvas5.create_line(300, 35, 300, 220, dash=(4, 2))
    canvas5.create_line(305, 35, 305, 220, dash=(4, 2))

    canvas5.create_line(10, 230, 300, 230, dash=(4, 2))
    canvas5.create_line(10, 230, 305, 230, dash=(4, 2))
    
    label1 = Label(Mafenetre5, text='Transformation entre coordonnees:\n Géodésique locale vers Géocentriques')
    label1.config(font=('Arial', 14 ,'bold'),fg='#8B4513')
    canvas5.create_window(200, 25, window=label1)

    label2 = Label(Mafenetre5, text='La longitude Lambda (°)')
    label2.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas5.create_window(1, 60, window=label2)
    
    entry5_1 = Entry(Mafenetre5)
    canvas5.create_window(200, 60, window=entry5_1)

   
    label3 = Label(Mafenetre5, text='La latitude Phi(°) :')
    label3.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas5.create_window(1, 90, window=label3)
    
    entry5_2 = Entry(Mafenetre5) 
    canvas5.create_window(200, 90, window=entry5_2)

    label4 = Label(Mafenetre5, text='Azimut astronomique Apq (°) :')
    label4.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas5.create_window(1, 120, window=label4)
    
    entry5_3 = Entry(Mafenetre5) 
    canvas5.create_window(200, 120, window=entry5_3)

    label5 = Label(Mafenetre5, text='Angle vertical Vpq (°) :')
    label5.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas5.create_window(1, 150, window=label5)
    entry5_4 = Entry(Mafenetre5) 
    canvas5.create_window(200, 150, window=entry5_4)

    label6 = Label(Mafenetre5, text='Distance entre P et Q Cpq (m) :')
    label6.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas5.create_window(1, 180, window=label6)
    
    entry5_5 = Entry(Mafenetre5) 
    canvas5.create_window(200, 180, window=entry5_5)

    label6 = Label(Mafenetre5, text='grand axe a :')
    label6.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas5.create_window(1, 260, window=label6)
    
    entry5_6 = Entry(Mafenetre5) 
    canvas5.create_window(200, 260, window=entry5_6)

    label6 = Label(Mafenetre5, text='ptit axe b :')
    label6.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas5.create_window(1, 280, window=label6)
    
    entry5_7 = Entry(Mafenetre5) 
    canvas5.create_window(200, 280, window=entry5_7)

    label7 = Label(Mafenetre5, text='hauteur ellipsoidale :')
    label7.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas5.create_window(1, 300, window=label7)
    
    entry5_8 = Entry(Mafenetre5) 
    canvas5.create_window(200, 300, window=entry5_8)

    button2 = Button(Mafenetre5,text='Transformer', command = g5et_coordonnees_geocentrique ,bg='#8B795E',fg='#FDFEFE', font=('Arial',11, 'bold'))
    canvas5.create_window(125, 210, window=button2)

    Btn2 = Button(Mafenetre5, text = "Choisissez un datum",command=ellipsoide5,bg='#8B795E',fg='#FDFEFE',font=('Arial', 9, 'bold'))
    canvas5.create_window(1, 330, window=Btn2)

    Btn3= Button(Mafenetre5, text = 'show map', command =openweb3 ,bg='#8B795E',fg='#FDFEFE', font=('Arial', 9, 'bold'))
    canvas5.create_window(1, 210, window=Btn3)

    Btn4= Button(Mafenetre5, text = 'localisation', command =geocoder5 ,bg='#8B795E',fg='#FDFEFE', font=('Arial', 9, 'bold'))
    canvas5.create_window(250, 210, window=Btn4)

    Btn5= Button(Mafenetre5, text = 'visualisation 3D', command =map3d5 ,bg='#8B795E',fg='#FDFEFE', font=('Arial', 9, 'bold'))
    canvas5.create_window(200, 330, window=Btn5)
    

    Mafenetre5.mainloop()
def ellipsoide5():
    
    class Test:
        
      def __init__(self, tk0):
        self.var = StringVar()
        fontCombo = ("Ink Free", 16, "bold")
        self.data = ("Maupertuis (1738)","Plessis (1817)","Everest (1830)","Everest 1830 Modified (1967)","Airy (1830)","Bessel (1841)","Clarke (1866)","Clarke (1878)","Clarke (1880)","Helmert (1906)","Hayford (1910)","International (1924)","Krassovsky (1940)","WGS66 (1966)","Australian National (1966)","New International (1967)","GRS-67 (1967)","South American (1969)","WGS-72 (1972)","GRS-80 (1979)","WGS-84 (1984)","IERS (1989)","IERS (2003)")
        self.cb = Combobox(tk0, values=self.data,font = fontCombo)
        self.cb.place(x=50, y=50)
        self.b1 = Button(tk0, text="Réactualiser", command=lambda:[self.select(),tk0.destroy()],bg='#8B795E',fg='#FDFEFE',font=('Arial', 9, 'bold')).place(x=160, y=110)

      def set_text(Entry,text):   
        Entry.delete(0,END)
        Entry.insert(0,text)
        return
    
      def select(self):
        value = self.cb.get()
        ent_a=entry5_6
        ent_b=entry5_7
        if value=="Maupertuis (1738)" :
            set_text(ent_a,6397300)
            set_text(ent_b,6363806.283)
        
        elif value=="Plessis (1817)" :
            set_text(ent_a,6376523.0)
            set_text(ent_b,6355862.9333)
        
        elif value=="Everest (1830)" :
            set_text(ent_a,6377299.365)
            set_text(ent_b,6356098.359)
        
        elif value=="Everest 1830 Modified (1967)" :
            set_text(ent_a,6377304.063)
            set_text(ent_b,6356103.0390)
        
        elif value=="Everest 1830 (1967 Definition)" :
            set_text(ent_a,6377298.556)
            set_text(ent_b,6356097.550)
        
        elif value=="Airy (1830)" :
            set_text(ent_a,6377563.396)
            set_text(ent_b,6356256.909)
        
        elif value=="Bessel (1841)" :
            set_text(ent_a,6377397.155)
            set_text(ent_b,6356078.963)
        
        elif value=="Clarke (1866)" :
            set_text(ent_a,6378206.4)
            set_text(ent_b,6356583.8)
        
        elif value=="Clarke (1878)" :
            set_text(ent_a,6378190)
            set_text(ent_b,6356456)
        
        elif value=="Clarke (1880)" :
            set_text(ent_a,6378249.145)
            set_text(ent_b,6356514.870)

        elif value=="Helmert (1906)" :
            set_text(ent_a,6378200)
            set_text(ent_b,6356818.17)
        
        elif value=="Hayford (1910)" :
            set_text(ent_a,6378388)
            set_text(ent_b,6356911.946)
        
        elif value=="International (1924)" :
            set_text(ent_a,6378245)
            set_text(ent_b,6356911.946)
        
        elif value=="Krassovsky (1940)" :
            set_text(ent_a,6378245)
            set_text(ent_b,6356863.019)
        
        elif value=="WGS66 (1966)" :
            set_text(ent_a,6378145)
            set_text(ent_b,6356759.769)
             
        elif value=="Australian National (1966)" :
            set_text(ent_a,6378160)
            set_text(ent_b,6356774.719)
        
        elif value=="New International (1967)" :
            set_text(ent_a,6378157.5)
            set_text(ent_b,6356772.2)
    
        elif value=="GRS-67 (1967)" :
            set_text(ent_a,6378160)
            set_text(ent_b,6356774.516)
        
        elif value=="South American (1969)" :
            set_text(ent_a,6378160)
            set_text(ent_b,6356774.719)

        elif value=="WGS-72 (1972)" :
            set_text(ent_a,6378135)
            set_text(ent_b,6356750.52)
        
        elif value=="GRS-80 (1979)" :
            set_text(ent_a,6378137)
            set_text(ent_b,6356752.3141)
        
        elif value=="WGS-84 (1984)" :
            set_text(ent_a,6378137)
            set_text(ent_b,6356752.3142)
        
        elif value=="IERS (1989)" :
            set_text(ent_a,6378136)
            set_text(ent_b,6356751.302)

        elif value=="IERS (2003)" :
            set_text(ent_a,6378136.6)
            set_text(ent_b,6356751.9)
        else:
          messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")  
    tk0 = Tk()
    tk0.geometry("378x170")
    tk0.title("Chose_ellipsoid")
    tk0.iconbitmap('Ressources/favicon.ico')
    tt = Test(tk0)
    tk0.mainloop()
def g5et_coordonnees_geocentrique():
        
            global entry5_1,entry5_2,entry5_3,entry5_4,entry5_5,canvas5,Mafenetre5
            try:
                    lambdap,phip,alphapq,vpq,cpq=float(entry5_1.get()),float(entry5_2.get()),float(entry5_3.get()),float(entry5_4.get()),float(entry5_5.get())

                    label7 = Label(Mafenetre5 ,text= 'DeltaXpq (m) :')
                    label7.config(font=('Arial', 10))
                    canvas5.create_window(350, 60, window=label7)

                    label9 = Label(Mafenetre5 , text= 'DeltaYpq (m) :',font=('Arial', 10))
                    canvas5.create_window(350, 100, window=label9)

                    label11 = Label(Mafenetre5 , text= 'DeltaZpq (m) :',font=('Arial', 10))
                    canvas5.create_window(350, 140, window=label11)
                
                    if 90>=phip and -90<=phip :
                        if 180>= lambdap and -180<= lambdap :
                            if alphapq<360 and 0<=alphapq:
                                if vpq<=90 and vpq>=0 :
                                    if cpq>0:
                                        DeltaX4,DeltaY4,DeltaZ4=transformation_geodesique_locales_vers_geocentrique(lambdap,phip,alphapq,vpq,cpq)
                                        label8 = Label(Mafenetre5, text= "{:011.5f}".format(DeltaX4) ,font=('Arial', 10, 'bold'))
                                        canvas5.create_window(450, 60, window=label8)
                                        label10 = Label(Mafenetre5, text= "{:011.5f}".format(DeltaY4) ,font=('Arial', 10, 'bold'))
                                        canvas5.create_window(450, 100, window=label10)
                                        label12 = Label(Mafenetre5, text= "{:011.5f}".format(DeltaZ4) ,font=('Arial', 10, 'bold'))
                                        canvas5.create_window(450, 140, window=label12)



                                        coords = (phip,lambdap)
                                        map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=5)

                                        coords = [phip,lambdap]
                                        folium.Marker(location=coords, popup = "").add_to(map)
                                        map.save('indexx.html')
                                    else:
                                         messagebox.showerror('domain error',"""Verifier la distance""")
                                else:
                                    messagebox.showerror('domain error',"""Verifier langle verticale""")
                            else:
                                 messagebox.showerror('domain error',"""verifier l azimut""")
                        else:
                             messagebox.showerror('domain error',"""Verifier lambda""")
                    else:
                        messagebox.showerror('domain error',"""Verifier phi""")  
            
            except ValueError:
                        messagebox.showerror('domain error',"""vous devez remplir toutes les cases """)
def geocoder5():
        global entry5_1,entry5_2,canvas5,Mafenetre5
        try:
                Lambda5,Phi5=float(entry5_1.get()),float(entry5_2.get())
                geolocator = Nominatim(user_agent="geoapiExercises")
                Latitude = str(Phi5)
                Longitude = str(Lambda5)
                location = geolocator.reverse((Latitude+","+Longitude),language='en')
                address = location.raw['address']
                label13 = Label(Mafenetre5 , text= 'country :',font=('Arial', 10))
                canvas5.create_window(350, 180, window=label13)
            
                label14 = Label(Mafenetre5, text=address.get('country', '') ,font=('Arial', 10, 'bold'))
                canvas5.create_window(450, 180, window=label14)
        
        except ValueError:
                messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez""")

        except AttributeError:
                 messagebox.showerror('error',"""on n'a pas pus localiser ce pays!""")


def map3d5():
            global entry5_1,entry5_2,canvas5,Mafenetre5,entry5_6,entry5_7,entry5_8
            try:
        
                Lambda5,Phi5,h,a,b=float(entry5_1.get()),float(entry5_2.get()),float(entry5_8.get()),float(entry5_6.get()),float(entry5_7.get())
                x5,y5,z5=transformation_cor_Geodisiques_Geocentriques(Lambda5,Phi5,h,a,b)

           

                
                   
                if b<=a and 0<a and 0<b: 
                        if Phi5<=90 and -90<=Phi5:
                            if Lambda5<=180 and -180<=Lambda5:
                        
                                        phi = np.linspace(0, 2*pi)
                                        theta = np.linspace(-pi/2, pi/2)
                                        phi, theta=np.meshgrid(phi, theta)
                                        X = cos(theta) * sin(phi) * a
                                        Y = cos(theta) * cos(phi) * a
                                        Z = sin(theta)*b
                                        fig = go.Figure(data=[go.Surface(x = X, y = Y, z=Z)])
                                        fig.update_layout(width=900, height=900);
                                        fig.update_traces(opacity=0.5,contours_z=dict(show=True, usecolormap=True,highlightcolor="limegreen", project_z=False))
                                        xdata =np.linspace(x5,x5,1)
                                        ydata = np.linspace(y5,y5,1)
                                        zdata = np.linspace(z5,z5,1)
                                        fig.add_scatter3d(x=xdata, y=ydata, z=zdata, mode='markers')
                                        fig.show()
                            else:
                                messagebox.showerror('domain error ',""" verifier lamda""")
                        else:
                         messagebox.showerror('domain error ',""" verifier phi """)
                else:
                     messagebox.showerror('domain error ',""" saisir a et b correctement""")

            except ValueError:
                        messagebox.showerror('domain error',"""vous devez remplir toutes les cases """)
##Géodésique locales vers astronomiques locales


def transformation_Geodesique_locales_vers_astronomiques_locales(Ap,Op,lambdap,phip,cgs,vgs,alphags):
     
     Ap=degree2radians(Ap)
     Op=degree2radians(Op)
     lambdap=degree2radians(lambdap)
     phip=degree2radians(phip)
     rpq=cgs*cos(vgs)*cos(alphags)
     spq=cgs*cos(vgs)*sin(alphags)
     tpq=cgs*sin(vgs)
     upq=rpq-(Ap-lambdap)*sin(Op)*spq-(Op-phip)*tpq
     vpq=spq+rpq*(Ap-lambdap)*sin(Op)-cos(Op)*tpq
     wpq=rpq*(Op-phip)+(Ap-lambdap)*cos(Op)*spq+tpq
     v_ast=asin(wpq/cgs)*180/pi
     if upq>0:
         az_ast=atan(vpq/upq)*180/pi
     elif vpq>=0 and upq<0:
         az_ast=(atan(vpq/upq)*180/pi )+180
     elif vpq<0 and upq<0:
         az_ast=(atan(vpq/upq)*180/pi)-180
     elif vpq>0 and upq==0:
         az_ast=180
     elif vpq<0 and upq==0:
         az_ast=-180
     else:
         az_ast=0
     
     

     if az_ast<0:
         az_ast=az_ast+360
     return az_ast,v_ast,cgs
    
def  Geodesique_locales_vers_astronomiques_locales():
    
    global entry6_1,entry6_2,entry6_3,entry6_4,entry6_5,canvas6,Mafenetre6,entry6_6,entry6_7,entry6_8,entry6_9,entry6_10
    
    Mafenetre6 = Tk()
    Mafenetre6.geometry('900x350')
    Mafenetre6.iconbitmap('Ressources/favicon.ico')
    Mafenetre6.title('Geodesique_locales_vers_astronomiques_locales')

    canvas6 = Canvas(Mafenetre6, width =600, height = 500, relief = 'raised')
    canvas6.pack()
    canvas6.create_line(300, 35, 300, 220, dash=(4, 2))
    canvas6.create_line(305, 35, 305, 220, dash=(4, 2))

    canvas6.create_line(0, 230, 300, 230, dash=(4, 2))
    canvas6.create_line(0, 230, 305, 230, dash=(4, 2))
    
    label1 = Label(Mafenetre6, text='Transformation entre coordonnees:\n Géodésique locales vers Astronomiques locales')
    label1.config(font=('Arial', 14 ,'bold'),fg='#8B4513')
    canvas6.create_window(200, 25, window=label1)

    label2 = Label(Mafenetre6, text='La longitude Lambda (°)')
    label2.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas6.create_window(1, 60, window=label2)
    
    entry6_1 = Entry(Mafenetre6)
    canvas6.create_window(220, 60, window=entry6_1)

   
    label3 = Label(Mafenetre6, text='La latitude Phi(°) :')
    label3.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas6.create_window(1, 80, window=label3)
    
    entry6_2 = Entry(Mafenetre6) 
    canvas6.create_window(220, 80, window=entry6_2)

    label4 = Label(Mafenetre6, text='Ap longitude astronomique locale de P (°):')
    label4.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas6.create_window(1, 100, window=label4)
    
    entry6_3 = Entry(Mafenetre6) 
    canvas6.create_window(220, 100, window=entry6_3)

    label5 = Label(Mafenetre6, text='Op latitude astronomique de P (°) :')
    label5.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas6.create_window(1, 120, window=label5)
    entry6_4 = Entry(Mafenetre6) 
    canvas6.create_window(220, 120, window=entry6_4)

    label6 = Label(Mafenetre6, text='alpha gs :')
    label6.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas6.create_window(1, 140, window=label6)
    
    entry6_5 = Entry(Mafenetre6) 
    canvas6.create_window(220, 140, window=entry6_5)

    label6 = Label(Mafenetre6, text='vgs :')
    label6.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas6.create_window(1, 160, window=label6)
    
    entry6_6 = Entry(Mafenetre6) 
    canvas6.create_window(220, 160, window=entry6_6)

    label6 = Label(Mafenetre6, text='cgs :')
    label6.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas6.create_window(1, 180, window=label6)
    
    entry6_7 = Entry(Mafenetre6) 
    canvas6.create_window(220, 180, window=entry6_7)
    
    label6 = Label(Mafenetre6, text='grand axe a :')
    label6.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas6.create_window(1, 260, window=label6)
    
    entry6_8 = Entry(Mafenetre6) 
    canvas6.create_window(220, 260, window=entry6_8)

    label6 = Label(Mafenetre6, text='ptit axe b :')
    label6.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas6.create_window(1, 280, window=label6)
    
    entry6_9 = Entry(Mafenetre6) 
    canvas6.create_window(220, 280, window=entry6_9)

    label7 = Label(Mafenetre6, text='hauteur ellipsoidale :')
    label7.config(font=('Arial', 10 ,'bold'),fg='#8B4513')
    canvas6.create_window(1, 300, window=label7)
    
    entry6_10 = Entry(Mafenetre6) 
    canvas6.create_window(220, 300, window=entry6_10)

    button2 = Button(Mafenetre6,text='Transformer', command = g6et_coordonnees_astronomiques_locales ,bg='#8B795E',fg='#FDFEFE', font=('Arial', 11, 'bold'))
    canvas6.create_window(100, 210, window=button2)

    Btn2 = Button(Mafenetre6, text = "Choisissez un datum",command=ellipsoide6,bg='#8B795E',fg='#FDFEFE',font=('Arial', 9, 'bold'))
    canvas6.create_window(50, 340, window=Btn2)

    Btn3= Button(Mafenetre6, text = 'show map', command =openweb3 ,bg='#8B795E',fg='#FDFEFE', font=('Arial', 9, 'bold'))
    canvas6.create_window(1, 210, window=Btn3)

    Btn4= Button(Mafenetre6, text = 'localisation', command =geocoder6 ,bg='#8B795E',fg='#FDFEFE', font=('Arial', 9, 'bold'))
    canvas6.create_window(200, 210, window=Btn4)

    Btn5= Button(Mafenetre6, text = 'visualisation 3D', command =map3d6 ,bg='#8B795E',fg='#FDFEFE', font=('Arial', 9, 'bold'))
    canvas6.create_window(200, 340, window=Btn5)
    

    Mafenetre6.mainloop()
def ellipsoide6():
    
    class Test:
        
      def __init__(self, tk0):
        self.var = StringVar()
        fontCombo = ("Ink Free", 16, "bold")
        self.data = ("Maupertuis (1738)","Plessis (1817)","Everest (1830)","Everest 1830 Modified (1967)","Airy (1830)","Bessel (1841)","Clarke (1866)","Clarke (1878)","Clarke (1880)","Helmert (1906)","Hayford (1910)","International (1924)","Krassovsky (1940)","WGS66 (1966)","Australian National (1966)","New International (1967)","GRS-67 (1967)","South American (1969)","WGS-72 (1972)","GRS-80 (1979)","WGS-84 (1984)","IERS (1989)","IERS (2003)")
        self.cb = Combobox(tk0, values=self.data,font = fontCombo)
        self.cb.place(x=50, y=50)
        self.b1 = Button(tk0, text="Réactualiser", command=lambda:[self.select(),tk0.destroy()],bg='#8B795E',fg='#FDFEFE',font=('Arial', 9, 'bold')).place(x=160, y=110)

      def set_text(Entry,text):   
        Entry.delete(0,END)
        Entry.insert(0,text)
        return
    
      def select(self):
        value = self.cb.get()
        ent_a=entry6_8
        ent_b=entry6_9
        if value=="Maupertuis (1738)" :
            set_text(ent_a,6397300)
            set_text(ent_b,6363806.283)
        
        elif value=="Plessis (1817)" :
            set_text(ent_a,6376523.0)
            set_text(ent_b,6355862.9333)
        
        elif value=="Everest (1830)" :
            set_text(ent_a,6377299.365)
            set_text(ent_b,6356098.359)
        
        elif value=="Everest 1830 Modified (1967)" :
            set_text(ent_a,6377304.063)
            set_text(ent_b,6356103.0390)
        
        elif value=="Everest 1830 (1967 Definition)" :
            set_text(ent_a,6377298.556)
            set_text(ent_b,6356097.550)
        
        elif value=="Airy (1830)" :
            set_text(ent_a,6377563.396)
            set_text(ent_b,6356256.909)
        
        elif value=="Bessel (1841)" :
            set_text(ent_a,6377397.155)
            set_text(ent_b,6356078.963)
        
        elif value=="Clarke (1866)" :
            set_text(ent_a,6378206.4)
            set_text(ent_b,6356583.8)
        
        elif value=="Clarke (1878)" :
            set_text(ent_a,6378190)
            set_text(ent_b,6356456)
        
        elif value=="Clarke (1880)" :
            set_text(ent_a,6378249.145)
            set_text(ent_b,6356514.870)

        elif value=="Helmert (1906)" :
            set_text(ent_a,6378200)
            set_text(ent_b,6356818.17)
        
        elif value=="Hayford (1910)" :
            set_text(ent_a,6378388)
            set_text(ent_b,6356911.946)
        
        elif value=="International (1924)" :
            set_text(ent_a,6378245)
            set_text(ent_b,6356911.946)
        
        elif value=="Krassovsky (1940)" :
            set_text(ent_a,6378245)
            set_text(ent_b,6356863.019)
        
        elif value=="WGS66 (1966)" :
            set_text(ent_a,6378145)
            set_text(ent_b,6356759.769)
             
        elif value=="Australian National (1966)" :
            set_text(ent_a,6378160)
            set_text(ent_b,6356774.719)
        
        elif value=="New International (1967)" :
            set_text(ent_a,6378157.5)
            set_text(ent_b,6356772.2)
    
        elif value=="GRS-67 (1967)" :
            set_text(ent_a,6378160)
            set_text(ent_b,6356774.516)
        
        elif value=="South American (1969)" :
            set_text(ent_a,6378160)
            set_text(ent_b,6356774.719)

        elif value=="WGS-72 (1972)" :
            set_text(ent_a,6378135)
            set_text(ent_b,6356750.52)
        
        elif value=="GRS-80 (1979)" :
            set_text(ent_a,6378137)
            set_text(ent_b,6356752.3141)
        
        elif value=="WGS-84 (1984)" :
            set_text(ent_a,6378137)
            set_text(ent_b,6356752.3142)
        
        elif value=="IERS (1989)" :
            set_text(ent_a,6378136)
            set_text(ent_b,6356751.302)

        elif value=="IERS (2003)" :
            set_text(ent_a,6378136.6)
            set_text(ent_b,6356751.9)
        else:
          messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez
En cas d'ambiguité consulter le guide d'utilisation""")  
    tk0 = Tk()
    tk0.geometry("378x170")
    tk0.title("Chose_ellipsoid")
    tk0.iconbitmap('Ressources/favicon.ico')
    tt = Test(tk0)
    tk0.mainloop()

def g6et_coordonnees_astronomiques_locales():
    
     global entry6_1,entry6_2,entry6_2,entry6_4,entry6_5,entry6_6,canvas6,Mafenetre6,entry6_7,entry7_8,entry6_9,entry6_10
     try:
        
         lambdap,phip,Ap,Op,alphags,vgs,cgs=float(entry6_1.get()),float(entry6_2.get()),float(entry6_3.get()),float(entry6_4.get()),float(entry6_5.get()),float(entry6_6.get()),float(entry6_7.get())

        
         label7 = Label(Mafenetre6, text= 'az_ast(°) :',font=('Arial', 10))
         canvas6.create_window(430, 60, window=label7)
        
         label9 = Label(Mafenetre6, text= 'V_ast (°)  :',font=('Arial', 10))
         canvas6.create_window(430, 100, window=label9)

         label11 = Label( Mafenetre6,text= 'cgs (°) :',font=('Arial', 10))
         canvas6.create_window(430, 140, window=label11)
        
            
         if phip<=90 and -90<=phip:
             if lambdap<=180 and -180<=lambdap:
                
                if Op<=90 and -90<=Op:
                      if Ap<=180 and -180<=Ap:
                          if alphags<360 and 0<=alphags:
                              if vgs<=90 and 0<=vgs:
                                  if cgs>0:
                                     az_ast,v_ast,cgs=transformation_Geodesique_locales_vers_astronomiques_locales(Ap,Op,lambdap,phip,alphags,vgs,cgs)
                                     label8 = Label(Mafenetre6, text="{:05.5f}".format(az_ast) ,font=('Arial', 10, 'bold'))
                                     canvas6.create_window(580, 60, window=label8)
                                     label10 = Label(Mafenetre6, text= "{:05.5f}".format(v_ast) ,font=('Arial', 10, 'bold'))
                                     canvas6.create_window(580, 100, window=label10)
                                     label12 = Label(Mafenetre6, text= "{:010.5f}".format(cgs) ,font=('Arial', 10, 'bold'))
                                     canvas6.create_window(580, 140, window=label12)
                                     import folium


                                     coords = (phip,lambdap)
                                     map = folium.Map(location=coords, tiles='OpenStreetMap', zoom_start=5)

                                     coords = [phip,lambdap]
                                     folium.Marker(location=coords, popup = "").add_to(map)
                                     map.save(ur3)
                                     
                                  else:
                                   messagebox.showerror('domain error ',""" verifier la valeur de cgs""")
                              else:
                                messagebox.showerror('domain error ',""" verifier la valeur de vgs""")
                          else:
                             messagebox.showerror('domain error ',""" verifier la valeur de alphags""")
                      else:
                       messagebox.showerror('domain error ',""" verifier la valeur de lambda astro""")
                else:
                    messagebox.showerror('domain error ',""" verifier la valeur de phi astro """)
             else:
                 messagebox.showerror('domain error ',""" verifier la valeur de lambda""")
         else:
             messagebox.showerror('domain error ',""" verifier la valeur de phi""")
     except ValueError:
                 messagebox.showerror('domain error',"""vous devez remplir toutes les cases """)


def geocoder6():
        global entry6_1,entry6_2,canvas6,Mafenetre6
        try:
                Lambda6,Phi6=float(entry6_1.get()),float(entry6_2.get())
                geolocator = Nominatim(user_agent="geoapiExercises")
                Latitude = str(Phi6)
                Longitude = str(Lambda6)
                location = geolocator.reverse((Latitude+","+Longitude),language='en')
                address = location.raw['address']
                label13 = Label(Mafenetre6 , text= 'country :',font=('Arial', 10))
                canvas6.create_window(350, 180, window=label13)
            
                label14 = Label(Mafenetre6, text=address.get('country', '') ,font=('Arial', 10, 'bold'))
                canvas6.create_window(450, 180, window=label14)
        
        except ValueError:
                messagebox.showerror('domain error',"""Verifier les valeurs que vous avez saisirez""")

        except AttributeError:
                 messagebox.showerror('error',"""on n'a pas pus localiser ce pays!""")


def map3d6():
            global entry6_1,entry6_2,canvas6,Mafenetre6,entry6_8,entry6_9,entry6_10

        
            Lambda,Phi,h,a,b=float(entry6_1.get()),float(entry6_2.get()),float(entry6_10.get()),float(entry6_8.get()),float(entry6_9.get())
            x6,y6,z6=transformation_cor_Geodisiques_Geocentriques(Lambda,Phi,h,a,b)

            try:
                  
                if b<=a and 0<a and 0<b: 
                        if Phi<=90 and -90<=Phi:
                            if Lambda<=180 and -180<=Lambda:
                        
                                        phi = np.linspace(0, 2*pi)
                                        theta = np.linspace(-pi/2, pi/2)
                                        phi, theta=np.meshgrid(phi, theta)
                                        X = cos(theta) * sin(phi) * a
                                        Y = cos(theta) * cos(phi) * a
                                        Z = sin(theta)*b
                                        fig = go.Figure(data=[go.Surface(x = X, y = Y, z=Z)])
                                        fig.update_layout(width=900, height=900);
                                        fig.update_traces(opacity=0.5,contours_z=dict(show=True, usecolormap=True,highlightcolor="limegreen", project_z=False))
                                        xdata =np.linspace(x6,x6,1)
                                        ydata = np.linspace(y6,y6,1)
                                        zdata = np.linspace(z6,z6,1)
                                        fig.add_scatter3d(x=xdata, y=ydata, z=zdata, mode='markers')
                                        fig.show()
                            else:
                                messagebox.showerror('domain error ',""" verifier lamda""")
                        else:
                         messagebox.showerror('domain error ',""" verifier phi """)
                else:
                     messagebox.showerror('domain error ',""" saisir a et b correctement""")

            except ValueError:
                        messagebox.showerror('domain error',"""vous devez remplir toutes les cases """)


               



from tkinter import Tk,Canvas,Label,StringVar,Scale,HORIZONTAL,Entry,Button,BOTTOM,font,PhotoImage,END,NE,messagebox
from math import sqrt,cos,atan,pi,sin,asin,radians
import webbrowser
from decimal import Decimal
from folium import Map,Marker,PolyLine
from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import datetime
import glob
import logging
import os
from numpy import *
import plotly.graph_objs as go
from plotly.offline import plot
import numpy as np
from geopy.geocoders import Nominatim
import folium




new = 2



ur3='indexx.html'

ur1_2='image_illustrative.jpg'



def set_text(Entry,text):   
    Entry.delete(0,END)
    Entry.insert(0,text)
    return





    


def openweb3():
    webbrowser.open(ur3,new=new)

def openweb134_2():
    webbrowser.open(ur1_2,new=new)
   
def degree2radians(degree):
  # convert degrees to radians
  return degree*(pi/180)

def radians2degree(radians):
  # convert  radians to degrees
  return radians*(180/pi)

def close():
    Mafenetre0.destroy()
    root = Tk()
    l = AnimatedGIF(root, "Ressources/Earth.gif")
    l.pack()
    root.after(7000, lambda: root.destroy()) # Destroy the widget after 30 seconds
    root.overrideredirect(True)
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
 
# Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)-300
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)-200
 
# Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))
    root.mainloop()


    
class AnimatedGIF(Label, object):
    def __init__(self, master, path, forever=True):
        self._master = master
        self._loc = 0
        self._forever = forever

        self._is_running = False

        im = Image.open(path)
        self._frames = []
        i = 0
        try:
            while True:
                photoframe = ImageTk.PhotoImage(im.copy().convert('RGBA'))
                self._frames.append(photoframe)

                i += 1
                im.seek(i)
        except EOFError: pass
        
        self._last_index = len(self._frames) - 1

        try:
            self._delay = im.info['duration']
        except:
            self._delay = 100

        self._callback_id = None

        super(AnimatedGIF, self).__init__(master, image=self._frames[0])

    def start_animation(self, frame=None):
        if self._is_running: return

        if frame is not None:
            self._loc = 0
            self.configure(image=self._frames[frame])

        self._master.after(self._delay, self._animate_GIF)
        self._is_running = True

    def stop_animation(self):
        if not self._is_running: return

        if self._callback_id is not None:
            self.after_cancel(self._callback_id)
            self._callback_id = None

        self._is_running = False

    def _animate_GIF(self):
        self._loc += 1
        self.configure(image=self._frames[self._loc])

        if self._loc == self._last_index:
            if self._forever:
                self._loc = 0
                self._callback_id = self._master.after(self._delay, self._animate_GIF)
            else:
                self._callback_id = None
                self._is_running = False
        else:
            self._callback_id = self._master.after(self._delay, self._animate_GIF)

    def pack(self, start_animation=True, **kwargs):
        if start_animation:
            self.start_animation()

        super(AnimatedGIF, self).pack(**kwargs)

    def grid(self, start_animation=True, **kwargs):
        if start_animation:
            self.start_animation()

        super(AnimatedGIF, self).grid(**kwargs)
        
    def place(self, start_animation=True, **kwargs):
        if start_animation:
            self.start_animation()

        super(AnimatedGIF, self).place(**kwargs)
        
    def pack_forget(self, **kwargs):
        self.stop_animation()

        super(AnimatedGIF, self).pack_forget(**kwargs)

    def grid_forget(self, **kwargs):
        self.stop_animation()

        super(AnimatedGIF, self).grid_forget(**kwargs)
        
    def place_forget(self, **kwargs):
        self.stop_animation()

        super(AnimatedGIF, self).place_forget(**kwargs)


root = Tk()
l = AnimatedGIF(root, "Ressources/intro.gif")
l.pack()

root.after(8000, lambda: root.destroy()) # Destroy the widget after 30 seconds
root.overrideredirect(True)
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
 
# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)-300
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)-200
 
# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))
root.mainloop()

root.mainloop()

Mafenetre0= Tk()

Mafenetre0.title('GEODESIE')
Mafenetre0.geometry('800x850')

Mafenetre0.config(background='#FDF5E6')

x1=Button(Mafenetre0)
photo1=PhotoImage(file="Ressources/close.png")
x1.config(image=photo1,width="20",height="20",activebackground="#FDF5E6",bg="#FDF5E6", bd=0,command=close)
x1.place(relx=1,x=-20, y=20, anchor=NE)



label_title=Label(Mafenetre0,text="La Géodésie Géométrique",font=('Broadway', 20 ,'bold'),fg='#8B795E',bg='#FDF5E6')##,bg='#8EF0F0',fg='#6C91BB'
label_title.pack()
label_subtitle=Label(Mafenetre0,text=" Transformation entre systèmes de coordonnées : \n Veuillez choisir la nature de la transformation : ",font=('Arial',20),bg='#FDF5E6',fg='#A6ACAF')##bg='#8EF0F0',fg='#285D97'
label_subtitle.pack()

Bouton1 = Button(Mafenetre0, text = ' Géodésiques \n vers\n Géocentriques :',width=20, command = Geodesiques_vers_geocentriques, cursor="plus",bg='#8B795E',fg='#FDFEFE')##,bg='#91ACCA'
Bouton1['font']=font.Font(family='Arial',size=20,weight='bold')
Bouton1.pack(anchor=W, expand='yes')


Bouton2 = Button(Mafenetre0, text = ' Géocentriques \n vers \n Géodésiques :',width=20, command = geocentriques_vers_Geodesiques, cursor="plus",bg='#8B795E',fg='#FDFEFE')
Bouton2['font']=font.Font(family='Arial',size=20,weight='bold')
Bouton2.pack(anchor=E,expand='yes')


Bouton3 = Button(Mafenetre0, text = 'Géocentriques \n vers \n Astronomiques locales :',width=20 ,command = Geocentrique_vers_Astronomique, cursor="plus",bg='#8B795E',fg='#FDFEFE')
Bouton3['font']=font.Font(family='Arial',size=20,weight='bold')
Bouton3.pack(anchor=W,expand='yes')


Bouton4 = Button(Mafenetre0, text = ' Astronomiques locales \n vers \n Géocentriques : ',width=20, command =Astronomique_vers_Geocentrique, cursor="plus",bg='#8B795E',fg='#FDFEFE')
Bouton4['font']=font.Font(family='Arial',size=20,weight='bold')
Bouton4.pack(anchor=E,expand='yes')


Bouton5 = Button(Mafenetre0, text = ' Géodesique locale \n vers \n Géocentrique : ',width=20, command =geodesique_locales_vers_Geocentrique, cursor="plus",bg='#8B795E',fg='#FDFEFE')
Bouton5['font']=font.Font(family='Arial',size=20,weight='bold')
Bouton5.pack(anchor=W,expand='yes')




Bouton7 = Button(Mafenetre0, text = ' Géodesique locale \n vers \n Astronomiques locales: ',width=20, command =Geodesique_locales_vers_astronomiques_locales, cursor="plus",bg='#8B795E',fg='#FDFEFE')
Bouton7['font']=font.Font(family='Arial',size=20,weight='bold')
Bouton7.pack(anchor=E,expand='yes')


Mafenetre0.overrideredirect(True)
windowWidth = Mafenetre0.winfo_reqwidth()
windowHeight = Mafenetre0.winfo_reqheight()
 
# Gets both half the screen width/height and window width/height
positionRight = int(Mafenetre0.winfo_screenwidth()/2 - windowWidth/2)-300
positionDown = int(Mafenetre0.winfo_screenheight()/2 - windowHeight/2)-300
 
# Positions the window in the center of the page.
Mafenetre0.geometry("+{}+{}".format(positionRight, positionDown))
Mafenetre0.mainloop()
