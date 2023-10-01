#import all the required modules 
import tkinter
import tkinter .messagebox
import pickle

#create a GUI window
window = tkinter.Tk()

#Defining title of window
window.title("TO DO LIST")

#function for adding a specified task
def task_adding():
    todo = task_add.get()
    if todo!= "":
        todo_box.insert(tkinter.END,todo)
        task_add.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!",message="To add a task in your list , please enter some task !")

#function for deleting a specified task
def task_removing():
    try:
        index_todo = todo_box.curselection()[0]
        todo_box.delete(index_todo)

    except:
        tkinter.messagebox.showwarning(title="Warning!",message="To delete a task from your list,please select a task!")


#function for loading saved tasks
def task_load():
    try:
        
        tasks = pickle.load(open("tasks.dat","rb"))
        todo_box.delete(0,tkinter.END)
        for todo in tasks:
            todo_box.insert(tkinter.END,todo)
    except:
        tkinter.messagebox.showwarning(title="Warning!",message="Cannot find any tasks")

#function for saving the tasks
def task_save():
    tasks = todo_box.get(0,todo_box.size())
    pickle.dump(tasks,open("tasks.dat","wb"))

#create frame 
list_frame = tkinter.Frame(window)
list_frame.pack()

#create a todo box where all the tasks will appear
todo_box = tkinter.Listbox(list_frame,height=20,width=50,background="skyblue",borderwidth=5)
todo_box.pack(side=tkinter.LEFT)

#Adding a scroller 
scroller = tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT,fill=tkinter.Y)

#configuring todo box 
todo_box.config(yscrollcommand=scroller.set)
scroller.config(command=todo_box.yview)

#create a task entry box 
task_add = tkinter.Entry(window,width=50)
task_add.pack()

#create a button to add task in to do list
add_task_button = tkinter.Button(window,text="ADD TASK",font=("Times New Roman",20,"bold"),background="yellow",width=20,command=task_adding)
add_task_button.pack()

#create a button to delete task from to do list
remove_task_button = tkinter.Button(window,text="DELETE TASK",font=("Times New Roman",20,"bold"),background="red",width=20,command=task_removing)
remove_task_button.pack()

#create a button to load all saved tasks
load_task_button = tkinter.Button(window,text="LOAD TASK",font=("Times New Roman",20,"bold"),background="blue",width=20,command=task_load)
load_task_button.pack()

#create a button to save task in to do list
save_task_button = tkinter.Button(window,text="SAVE TASK",font=("Times New Roman",20,"bold"),background="green",width=20,command=task_save)
save_task_button.pack()

#start the GUI 
window.mainloop()