# Project-Title-MASTER-GIFT-All-in-One-Speech-AI-Chatbot-Nexus


### 📌Project Description:
The **~MASTER-GIFT~ All-in-One Speech AI-Chatbot Nexus** is an interactive application that offers a range of features for document reading, text-to-speech, and chatbot functionalities. It leverages a graphical interface built using `Tkinter`, enabling users to easily interact with various options. Key features include:

1. **Document Upload and Reading**:  
   Users can upload a PDF or DOCX file from their local system, and the program will read the content aloud using the built-in text-to-speech (TTS) engine.

2. **Text-to-Speech from User Input**:  
   Users can input text directly into a text box within the interface, and the program will read the text aloud using TTS.

3. **Text Display**:  
   The user can enter text into the program, which will be displayed and presented in a pop-up window.

4. **Offline Chatbot**:  
   The program includes an offline chatbot feature that allows users to ask questions. The chatbot is driven by an intents-based system where responses are provided based on matching patterns.

5. **Exit Option**:  
   A simple command allows users to exit the application directly from the interface.

### 🚀Features:
- **File Upload and Reading**: Users can upload PDF or DOCX files, and the content will be extracted and read aloud.
- **Text-to-Speech**: Paste or enter any text into the program, and it will read it aloud using the TTS engine.
- **Chatbot Assistant**: A basic chatbot that responds to user input based on predefined intents loaded from a JSON file.
- **User-Friendly Interface**: Built using `Tkinter`, the program provides an easy-to-use graphical interface with buttons for each feature.
- **Exit Command**: A simple exit button allows users to close the program.

### 📝Libraries Used:
1. **Tkinter**:  
   Used for creating the GUI elements and managing the application's main window.  
   [Documentation](https://docs.python.org/3/library/tkinter.html)

2. **Pillow** (`PIL`):  
   Used for handling and displaying images in the application.  
   [Documentation](https://pillow.readthedocs.io/en/stable/)

3. **Pyttsx3**:  
   A text-to-speech conversion library used to read text aloud.  
   [Documentation](https://pyttsx3.readthedocs.io/en/latest/)

4. **PyPDF2**:  
   Used to extract text from PDF files for reading.  
   [Documentation](https://pypi.org/project/PyPDF2/)

5. **python-docx**:  
   Used to extract text from DOCX files.  
   [Documentation](https://python-docx.readthedocs.io/en/latest/)

6. **Pygame**:  
   A multimedia library used for audio output and handling media-related functionalities.  
   [Documentation](https://www.pygame.org/docs/)

7. **JSON**:  
   Used for loading and parsing chatbot intents from a JSON file.  
   [Documentation](https://docs.python.org/3/library/json.html)

8. **Random**:  
   Provides random selection functionalities for generating chatbot responses.  
   [Documentation](https://docs.python.org/3/library/random.html)

9. **Regex** (`re`):  
   Used for pattern matching in chatbot input to identify user intents.  
   [Documentation](https://docs.python.org/3/library/re.html)

###⭐ How to Use:
1. Clone the repository and ensure all dependencies are installed.
2. Run the Python script.
3. Choose an option from the menu:
   - Upload a PDF or DOCX file and let the program read it.
   - Input text into the box and have it read aloud.
   - Use the chatbot to ask questions.
   - Exit the program.

### 🏁Installation:
To run the program, you’ll need to install the required libraries:
```bash
pip install pyttsx3 PyPDF2 python-docx Pillow pygame
``
