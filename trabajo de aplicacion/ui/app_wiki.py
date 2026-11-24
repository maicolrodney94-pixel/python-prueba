import tkinter as tk
from tkinter import ttk, messagebox
from services.user_service import UserService

class app_wiki:
    def __init__(self, root: tk.Tk, user_service: UserService):
        self.root = root
        self.user_service = user_service
        self.root.title("gestion de usuarios")
        self.create_widgets()
        self.root.geometry("800x600")
        self.load_data()
        
    def create_widgets(self):    
        form_frame = tk.LabelFrame(self.root, text="nuevo usuario", padx=10, pady=10)
        form_frame.pack(padx=15, pady=10, fill="x")
        
        tk.Label(form_frame, text="nombre:").grid(row=0, column=0, sticky="w",padx=5, pady=5)
        self.fname_entry = tk.Entry(form_frame, width=30)
        self.fname_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="apellido:").grid(row=1, column=0, sticky="w",padx=5, pady=5)
        self.lname_entry = tk.Entry(form_frame, width=30)
        self.lname_entry.grid(row=1, column=1, padx=5, pady=5)
         
        tk.Label(form_frame, text="edad:").grid(row=2, column=0, sticky="w",padx=5, pady=5)
        self.age_entry = tk.Entry(form_frame, width=30)
        self.age_entry.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="email:").grid(row=3, column=0, sticky="w",padx=5, pady=5)
        self.email_entry = tk.Entry(form_frame, width=30)
        self.email_entry.grid(row=3, column=1, padx=5, pady=5)
       
        btn_create = tk.Button(form_frame, text="crear usuario", command=self.handle_create_user)
        btn_create.grid(row=4, column=0, columnspan=2, pady=10)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",rowheight=26, boldercolor="#cccccc29",bolderwidth=1,relief="solid")
        style.configure("Treeview.Heading", background="#e1e1e1",relief="raised",bordercolor="#100b0b")
        columns = ("uuid", "fname", "lname", "age", "email")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
    
      
        self.tree.heading("uuid", text="UUID")
        self.tree.heading("fname", text="nombre") 
        self.tree.heading("lname", text="apellido")
        self.tree.heading("age", text="edad")
        self.tree.heading("email", text="email")
        
        self.tree.column("uuid", width=200, anchor="center")
        self.tree.column("fname", width=120, anchor="center")
        self.tree.column("lname", width=120, anchor="center")
        self.tree.column("age", width=50, anchor="center")
        self.tree.column("email", width=180, anchor="center")
        
        self.tree.pack(padx=15, pady=10, fill="both", expand=True)
        
        self.load_data()
        
    def handle_create_user(self):
            fname = self.fname_entry.get()
            lname = self.lname_entry.get()
            age = self.age_entry.get()
            email = self.email_entry.get()
            
            try:
                age_int = int(age)
                self.user_service.create_user(fname, lname, age_int, email)
                messagebox.showinfo("exito", "usuario creado correctamente")
                self.load_data()
                self.clear_inputs()
            except ValueError as e:
                messagebox.showerror("dato invalido", f"verifica los campos({str(e)})")
                       
    def load_data(self):
            for row in self.tree.get_children():
                self.tree.delete(row)
                
            users = self.user_service.get_all_users()
            for user in users:
                self.tree.insert("", "end", values=(user.uuid, user.fname, user.lname, user.age, user.email))
        
    def clear_inputs(self):
            self.fname_entry.delete(0, tk.END)
            self.lname_entry.delete(0, tk.END)
            self.age_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)