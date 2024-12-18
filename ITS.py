from tkinter import *
from owlready2 import get_ontology

# Load ontology
ontology_path = "C:\Users\AzharHussain\Desktop\Ontologyfiles\skeletalsystem.owx" 
onto = get_ontology(f"file://{ontology_path}").load()

# Initialize the interface
root = Tk()
root.title("Skeletal System ITS")
root.geometry("800x600")

# Function to display bone details
def show_bone_details(bone_name):
    bone = onto.search_one(hasName=bone_name)
    if bone:
        details = f"Name: {bone.hasName[0]}\nFunction: {bone.hasFunction[0]}\nLocated In: {bone.locatedIn[0].name}"
    else:
        details = "Bone not found in the ontology."
    details_label.config(text=details)

# Left panel for skeletal navigation
navigation_frame = Frame(root, width=200, bg="lightgray")
navigation_frame.pack(side=LEFT, fill=Y)

Label(navigation_frame, text="Bones", bg="lightgray", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=10)

# Add navigation buttons for bones
for bone_instance in onto.Bone.instances():
    Button(navigation_frame, text=bone_instance.hasName[0], bg="white", command=lambda bn=bone_instance.hasName[0]: show_bone_details(bn)).pack(anchor="w", padx=10, pady=2)

# Main content area
content_frame = Frame(root, bg="white")
content_frame.pack(side=RIGHT, expand=True, fill=BOTH)

details_label = Label(content_frame, text="Select a bone to view details.", font=("Arial", 14), bg="white", wraplength=500, justify=LEFT)
details_label.pack(padx=20, pady=20)

# Quiz section
quiz_frame = Frame(root, bg="white", pady=20)
quiz_frame.pack(side=BOTTOM, fill=X)

Label(quiz_frame, text="Quiz: Identify the Function of Bones", font=("Arial", 12, "bold"), bg="white").pack(pady=5)

# Function to handle quiz answers
def check_answer():
    user_answer = quiz_entry.get()
    if user_answer.lower() == "support":
        result_label.config(text="Correct!", fg="green")
    else:
        result_label.config(text="Incorrect. Hint: The femur is a weight-bearing bone.")

quiz_entry = Entry(quiz_frame, font=("Arial", 12))
quiz_entry.pack(pady=5)

Button(quiz_frame, text="Submit Answer", command=check_answer).pack(pady=5)

result_label = Label(quiz_frame, text="", font=("Arial", 12), bg="white")
result_label.pack()

# Run the application
root.mainloop()
________________________________________
