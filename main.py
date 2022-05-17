



from tkinter import *
import googletrans
from googletrans import Translator
import pyttsx3
import speech_recognition as sr


#global variables
message =''
whats_in_translate=""
glb_color="#957898"




tk = Tk()
tk.title('Google translate')
tk.config(bg=glb_color)




#functions
def google_trans_fun():
    global text_box,text_box1,menu,source_msg,dest_msg,languages1,languages,glanguages,whats_in_translate
    translator = Translator()
    
    source_lang=translator.detect(text_box.get("1.0", "end-1c"))
    trans_to=menu.get()
    translated=translator.translate(text_box.get("1.0", "end-1c"), dest=languages[trans_to])

    if translated.pronunciation!=None:
        whats_in_translate=translated.pronunciation
    else:
        whats_in_translate=text_box1.get("1.0", "end-1c")

    print(whats_in_translate)

    
    text_box1.delete("1.0","end")
    text_box1.insert('end', translated.text)
    source_msg.config(text=glanguages[source_lang.lang].capitalize())
    dest_msg.config(text=trans_to.capitalize())
    
    

def trans_pronountiation():
    global whats_in_translate,text_box
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 200)
    engine.say(whats_in_translate)
    engine.runAndWait()
    

    

#source

source=Frame(tk,bg=glb_color)

source_msg=Label(source,text="IN",font=("bold",20),bg=glb_color)
source_msg.grid(row=0,column=0)
text_box = Text(source,height=10,width=30,font=(25))
text_box.insert('end', message)
text_box.grid(row=1,column=0,padx=20,pady=20)

source.grid(row=0,column=0,padx=10,pady=40)



#controls
control=Frame(tk,bg=glb_color)

translate_to=Label(control,text="Translate to: ",font=("bold",15),bg=glb_color)
translate_to.grid(row=0,column=0,padx=10)

menu= StringVar()
menu.set("Select Any Language")
languages={}
languages1=[]
glanguages=googletrans.LANGUAGES


for i in glanguages:
    languages[glanguages[i]]=i
    languages1.append(glanguages[i])

drop= OptionMenu(control, menu,*languages1)
drop.config(font=("bold",10))
drop.grid(row=1,column=0,padx=30,pady=10)

trans=Button(control,text="Translate",font=("bold",12),command=google_trans_fun,width=20)
trans.grid(row=2,column=0,pady=10)

pronunciation=Button(control,text="pronunciation",font=("bold",12),command=trans_pronountiation,width=20)
pronunciation.grid(row=3,column=0,pady=10)

control.grid(row=0,column=1)

#destinaton
dest=Frame(tk,bg=glb_color)
dest_msg=Label(dest,text="OUT",font=("bold",20),bg=glb_color)
dest_msg.grid(row=0,column=0)
text_box1 = Text(dest,height=10,width=30,font=(25))
text_box1.insert('end', message)
text_box1.grid(row=1,column=0,padx=20,pady=20)
dest.grid(row=0,column=2,padx=10,pady=40)



tk.mainloop()
