import streamlit as lit
import time

lit.title('Learn.')
lit.subheader('Teaching a machine to teach a human.')
lit.write('Leveraging AI techniques to build interactive textbooks and modules that facilitate learning by oneself.') 

lit.subheader('Step 1: Upload!')
learning_material = lit.file_uploader('Upload your learning material here! :bulb:')

if learning_material:
    lit.subheader('Step 2: Choose!')
    lit.write('You have uploaded a *474-page e-textbook* titled *"Object-Oriented Design and Patterns"*. It contains *10 chapters*.')
    choice = lit.radio('How would you like to learn?',['Interactive Textbook','Learning Module','Summarized Textbook','Simplified Audiobook'])
    
    if lit.button("Click to Convert!"):
        progress_text = "Please wait, the magic is happening!"
        my_bar = lit.progress(0, text=progress_text)
    
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        my_bar.empty()

        lit.balloons()
        lit.subheader('Step 3: Learn!')
        lit.write("Here's your [file](https://oops-textbook-but-its-fun.streamlit.app/)! Happy Learning :)")
