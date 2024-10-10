import tkinter
import tkinter.filedialog
import tkinter.messagebox
import PIL.Image
import customtkinter
import PIL
from CTkListbox import *

def browse_images():
    file_types = [
        ('Image files', '*.jpeg *.jpg *.png *.gif *.bmp'),
        ('All files', '*.*')
    ]

    file_paths = tkinter.filedialog.askopenfilenames(title="Select file(s)", filetypes=file_types)

    for path in file_paths:
        listbox.insert(tkinter.END, path)

def convert_to_pdf():
    images = listbox.get(tkinter.ALL)
    try:
        
        imagesList = [PIL.Image.open(image).convert('RGB') for image in images]

        if not imagesList:
            tkinter.messagebox.showerror('Error', 'No images to convert.')
            return
        output_pdf_path = tkinter.filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

        if not output_pdf_path:
            return  # User cancelled save
        
        imagesList[0].save(output_pdf_path, save_all=True, append_images=imagesList[1:])
        tkinter.messagebox.showinfo('Success', 'The images have been successfully converted to PDF!')

    except Exception as e:
        tkinter.messagebox.showerror('Error', f'An error occurred: {e}')

def delete_item():
    selected_indices = listbox.curselection()
    print("Removed: ", selected_indices)
    for i in reversed(selected_indices):
        listbox.delete(i)    

def show_value(selected_option):
    print("Selected: ", selected_option)

def clear_list():
    listbox.delete(tkinter.ALL)

customtkinter.set_appearance_mode("System")    

app=customtkinter.CTk()
app.title('To PDF')
app.geometry("720x480")

listbox = CTkListbox(app, command=show_value, multiple_selection=True)
listbox.pack(fill="both", expand=True, padx=10, pady=10)

select_button=customtkinter.CTkButton(app, text="Select Images", command=browse_images)
select_button.pack(fill=tkinter.X)

convert_button=customtkinter.CTkButton(app, text="To PDF", command=convert_to_pdf)
convert_button.pack(fill=tkinter.X)

remove_button = customtkinter.CTkButton(app, text='Remove Selected', command=delete_item)
remove_button.pack(fill=tkinter.X)

clear_button = customtkinter.CTkButton(app, text='Clear', command=clear_list)
clear_button.pack(fill=tkinter.X)

app.mainloop()


