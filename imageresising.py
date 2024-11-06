from PIL import Image
import os
import tkinter as tk

root = tk.Tk()
root.title("Image Resizer")
root.geometry("300x200")

tk.Label(root, text="Path to image folder").grid(column=0, row=0)
enterstartfolder = tk.Entry(root)
enterstartfolder.grid(column=0, row=1)
tk.Label(root, text="Path to dump folder").grid(column=0, row=2)
enterdumpfolder = tk.Entry(root)
enterdumpfolder.grid(column=0, row=3)
tk.Label(root, text="Size in: width, height").grid(column=0, row=4)
entersize = tk.Entry(root)
entersize.grid(column=0, row=5)

def resizerfunc():
    # Haal de actuele waarden op uit de invoervelden en verwijder eventuele aanhalingstekens
    folder_path = enterstartfolder.get().strip('"')
    output_folder = enterdumpfolder.get().strip('"')
    
    # Controleer of de invoer voor breedte en hoogte een geldige tuple is
    try:
        size = tuple(map(int, entersize.get().split(',')))  # Converteer naar (width, height)
    except ValueError:
        print("Invalid size format. Please enter two integers separated by a comma.")
        return

    # Controleer of de opgegeven paden bestaan
    if not os.path.exists(folder_path):
        print(f"Input folder path does not exist: {folder_path}")
        return
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Maak de output folder aan als deze niet bestaat
    
    # Loop door elk bestand in de directory
    for filename in os.listdir(folder_path):
        # Alleen afbeeldingen verwerken (controleren op bestandsextensies)
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
            # Volledig pad naar de afbeelding
            img_path = os.path.join(folder_path, filename)
        
            # Open de afbeelding
            with Image.open(img_path) as img:
                # Verklein of verwerk de afbeelding
                img_resized = img.resize(size)
            
                # Optioneel: Opslaan naar output folder
                output_path = os.path.join(output_folder, filename)
                img_resized.save(output_path)
            
                # Print de naam van het verwerkte bestand
                print(f"Processed: {filename}")

button_start = tk.Button(root, text="Resize Photos", command=resizerfunc)
button_start.grid(column=1, row=0)

root.mainloop()
