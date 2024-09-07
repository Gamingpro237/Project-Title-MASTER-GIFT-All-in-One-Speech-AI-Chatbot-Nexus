import tkinter as tk
from tkinter import filedialog, Text
from tkinter import messagebox
from PIL import Image, ImageTk
import pyttsx3
import PyPDF2
import docx
import random
import re
import json
import pygame



# Initialize the main window
root = tk.Tk()
root.title("Gift Thinker")
root.geometry("1100x600")
root.resizable(True,True)

#initialize pygame
pygame.init()
pygame.mixer.init()

# Set up a variable for blinking color state
blink_color = True

# Initialize the text-to-speech engine
engine = pyttsx3.init()


# Set background image
bg_image = Image.open(r"C:\Users\USER\Python-Code\Thinker-Test\bg.png")  # Change the path to your background image file
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = tk.Label(root, image=bg_photo)
background_label.image = bg_photo
background_label.place(relwidth=1, relheight=1)

#menu thinker
menu=tk.Menu(root)

#Sub menu thinker
file_menu=tk.Menu(menu,tearoff=False)
file_menu.add_command(label='New',command=lambda:print("New file"))
menu.add_cascade(label='File', menu=file_menu)

#another sub menu
help_menu=tk.Menu(menu,tearoff=False)
help_menu.add_command(label='Help Entry',command=lambda:print("help"))
menu.add_cascade(label='Help', menu=help_menu)
root.configure(menu=menu)



"""

#initialize the pygame for windows for video playable
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Video Background')
clock=pygame.time.Clock()

#Load and play video

"""

# Create a frame for the main options
frame = tk.Frame(root, bg="#ffffff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

# Label for the application name
app_name_label = tk.Label(frame, text="~MASTER-GIFT~ all in one Speech Ai-Chatbot Nexus", font=("Helvetica", 24), bg="#ffffff")
app_name_label.place(relwidth=1, relheight=1)

# Function to open and read PDF/DOCX files
def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf"), ("Word files", "*.docx")])
    if file_path.endswith('.pdf'):
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            text = ''
            for page in range(reader.numPages):
                text += reader.getPage(page).extract_text()
            read_text(text)
    elif file_path.endswith('.docx'):
        doc = docx.Document(file_path)
        text = '\n'.join([para.text for para in doc.paragraphs])
        read_text(text)
    else:
        messagebox.showerror("Unsupported File", "Please select a PDF or DOCX file.")

#Function to run the chatbot
class Chatbot:
    def __init__(self, intents_file):
        with open(intents_file, 'r') as file:
            self.intents = json.load(file)
        
    def get_response(self, user_input):
        for intent in self.intents['intents']:
            for pattern in intent['patterns']:
                if re.search(r'\b' + re.escape(pattern) + r'\b', user_input, re.IGNORECASE):
                    return random.choice(intent['responses'])
        return random.choice(self.intents['intents'][-1]['responses'])

def main2():
    chatbot = Chatbot(r'C:\Users\USER\Python-Code\chatbot-test\intents.json')
    
    intro=print("MASTER GIFT Ai Chatbot is running!")
    voice=engine.getProperty('voices')
    engine.setProperty('voice',voice[1].id)
    engine.say(intro)
    engine.runAndWait()
    print()
    print("Chatbot is running! (type 'quit' to exit)")
    while True:
        
        user_input = text_box.get("1.0", "end-1c").strip()
        if user_input.lower() == 'quit':
            break
        response = chatbot.get_response(user_input)
        
        messagebox.showinfo(f"Chatbot:", response)
        
        
# Function to read text using TTS
def read_text(text):
    engine.say(text)
    engine.runAndWait()

# Function for Option 1
def option1():
    upload_file()

# Function for Option 2
def option2():
    text = text_box.get("1.0", "end-1c")
    read_text(text)

# Function for Option 3
def option3():
    text = text_box.get("1.0", "end-1c")
    messagebox.showinfo("Your Text", text)

# Function for Option 3
def option4():
    main2()

# Create buttons for the main options
btn_frame = tk.Frame(root, bg="#ffffff")
btn_frame.place(relx=0.5, rely=0.3, relwidth=0.9, relheight=0.8, anchor="n")

button1 = tk.Button(btn_frame, text="1. Upload Document (PDF/DOCX)", command=option1, bg="#76c7c0", font=("Helvetica", 18))
button1.pack(side="top", fill="x", pady=10)

button2 = tk.Button(btn_frame, text="2. Paste Your Text to be read Below", command=option2, bg="#76c7c0", font=("Helvetica", 18))
button2.pack(side="top", fill="x", pady=10)

button3 = tk.Button(btn_frame, text="3. Display your text", command=option3, bg="#76c7c0", font=("Helvetica", 18))
button3.pack(side="top", fill="x", pady=10)

button4 = tk.Button(btn_frame, text="4. Ask Your Assistant ~MASTER-GIFT~ Ai Chatbot any question", command=option4, bg="#76c7c0", font=("Helvetica", 18))
button4.pack(side="top", fill="x", pady=10)

button5 = tk.Button(btn_frame, text="5. Exit", command=root.quit, bg="#76c7c0", font=("Helvetica", 18))
button5.pack(side="top", fill="x", pady=10)

# Create a text box for user input
heading1=tk.Label(btn_frame, text="Enter your Text below", font=("Helvetica", 10), bg="#ffffff")
heading1.pack(side="top", fill="x", pady=13)

text_box = Text(root, font=("Helvetica", 16))
text_box.place(relx=0.5, rely=0.8, relwidth=0.75, relheight=0.15, anchor="n")

root.mainloop()
