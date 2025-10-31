import tkinter as tk
from tkinter import ttk, messagebox
import pickle
import pandas as pd


class LinearRegressionApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Linear Regression Predictor")
        self.root.geometry("500x500")
        self.root.configure(bg="#f0f0f0")
        
        # Load models
        self.load_models()
        
        # Create main menu
        self.create_main_menu()
    
    def load_models(self):
        """Load all pickle models"""
        try:
            with open('simple.pkl', 'rb') as f:
                self.simple_model = pickle.load(f)
        except:
            self.simple_model = None
            
        try:
            with open('polynomial_transformer.pkl', 'rb') as f:
                self.poly_transformer = pickle.load(f)
            with open('linear_model.pkl', 'rb') as f:
                self.poly_lin_reg = pickle.load(f)
        except:
            self.poly_transformer = None
            self.poly_lin_reg = None
            
        try:
            with open('model.pkl', 'rb') as f:
                self.multiple_model = pickle.load(f)
        except:
            self.multiple_model = None
    
    def create_main_menu(self):
        """Create the main menu with buttons for each regression type"""
        # Clear any existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Title
        title = tk.Label(
            self.root,
            text="Linear Regression Predictor",
            font=("Arial", 24, "bold"),
            bg="#f0f0f0",
            fg="#333"
        )
        title.pack(pady=30)
        
        # Subtitle
        subtitle = tk.Label(
            self.root,
            text="Select a regression type to make predictions",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#666"
        )
        subtitle.pack(pady=10)
        
        # Button frame
        btn_frame = tk.Frame(self.root, bg="#f0f0f0")
        btn_frame.pack(pady=30)
        
        # Simple Linear Regression Button
        simple_btn = tk.Button(
            btn_frame,
            text="Simple Linear Regression\n(Study Hours → Marks)",
            command=self.open_simple_regression,
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            width=30,
            height=3,
            cursor="hand2"
        )
        simple_btn.pack(pady=10)
        
        # Polynomial Regression Button
        poly_btn = tk.Button(
            btn_frame,
            text="Polynomial Regression\n(Level → Salary)",
            command=self.open_polynomial_regression,
            font=("Arial", 12),
            bg="#2196F3",
            fg="white",
            width=30,
            height=3,
            cursor="hand2"
        )
        poly_btn.pack(pady=10)
        
        # Multiple Linear Regression Button
        multiple_btn = tk.Button(
            btn_frame,
            text="Multiple Linear Regression\n(Startup Profit Prediction)",
            command=self.open_multiple_regression,
            font=("Arial", 12),
            bg="#FF9800",
            fg="white",
            width=30,
            height=3,
            cursor="hand2"
        )
        multiple_btn.pack(pady=10)
        
        # Signature
        signature = tk.Label(
            self.root,
            text="@ ONYX PYTHON 2ND APP | 2025",
            font=("Arial", 9, "italic"),
            bg="#f0f0f0",
            fg="#999"
        )
        signature.pack(side="bottom", pady=10)
    
    def open_simple_regression(self):
        """Open Simple Linear Regression window"""
        if self.simple_model is None:
            messagebox.showerror("Error", "simple.pkl model file not found!")
            return
        
        window = tk.Toplevel(self.root)
        window.title("Simple Linear Regression")
        window.geometry("450x300")
        window.configure(bg="#f0f0f0")
        
        # Title
        title = tk.Label(
            window,
            text="Predict Marks from Study Hours",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0"
        )
        title.pack(pady=20)
        
        # Input frame
        input_frame = tk.Frame(window, bg="#f0f0f0")
        input_frame.pack(pady=20)
        
        tk.Label(
            input_frame,
            text="Study Hours (1-10):",
            font=("Arial", 12),
            bg="#f0f0f0"
        ).grid(row=0, column=0, padx=10, pady=10)
        
        hours_entry = tk.Entry(input_frame, font=("Arial", 12), width=15)
        hours_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # Result label
        result_label = tk.Label(
            window,
            text="",
            font=("Arial", 14, "bold"),
            bg="#f0f0f0",
            fg="#4CAF50"
        )
        result_label.pack(pady=20)
        
        def predict():
            try:
                hrs = float(hours_entry.get())
                if hrs >= 1 and hrs <= 10:
                    marks = self.simple_model.predict([[hrs]])
                    result_label.config(
                        text=f"Predicted Marks: {int(marks[0])}",
                        fg="#4CAF50"
                    )
                else:
                    result_label.config(
                        text="Please enter hours between 1 and 10",
                        fg="#f44336"
                    )
            except ValueError:
                result_label.config(
                    text="Please enter a valid number",
                    fg="#f44336"
                )
        
        # Predict button
        predict_btn = tk.Button(
            window,
            text="Predict",
            command=predict,
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            width=15,
            cursor="hand2"
        )
        predict_btn.pack(pady=10)
        
        # Back button
        back_btn = tk.Button(
            window,
            text="Back to Menu",
            command=window.destroy,
            font=("Arial", 10),
            bg="#757575",
            fg="white",
            width=15,
            cursor="hand2"
        )
        back_btn.pack(pady=5)
    
    def open_polynomial_regression(self):
        """Open Polynomial Regression window"""
        if self.poly_transformer is None or self.poly_lin_reg is None:
            messagebox.showerror("Error", "polynomial_transformer.pkl or linear_model.pkl file not found!")
            return
        
        window = tk.Toplevel(self.root)
        window.title("Polynomial Regression")
        window.geometry("450x300")
        window.configure(bg="#f0f0f0")
        
        # Title
        title = tk.Label(
            window,
            text="Predict Salary from Level",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0"
        )
        title.pack(pady=20)
        
        # Input frame
        input_frame = tk.Frame(window, bg="#f0f0f0")
        input_frame.pack(pady=20)
        
        tk.Label(
            input_frame,
            text="Level:",
            font=("Arial", 12),
            bg="#f0f0f0"
        ).grid(row=0, column=0, padx=10, pady=10)
        
        level_entry = tk.Entry(input_frame, font=("Arial", 12), width=15)
        level_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # Result label
        result_label = tk.Label(
            window,
            text="",
            font=("Arial", 14, "bold"),
            bg="#f0f0f0",
            fg="#2196F3"
        )
        result_label.pack(pady=20)
        
        def predict():
            try:
                level = int(level_entry.get())
                # Transform the input level into polynomial features
                level_poly = self.poly_transformer.transform([[level]])
                # Use the loaded linear model to predict on the polynomial features
                predict_sal = self.poly_lin_reg.predict(level_poly)
                result_label.config(
                    text=f"Predicted Salary: ${int(predict_sal[0]):,}",
                    fg="#2196F3"
                )
            except ValueError:
                result_label.config(
                    text="Please enter a valid integer",
                    fg="#f44336"
                )
            except Exception as e:
                result_label.config(
                    text=f"Error: {str(e)}",
                    fg="#f44336"
                )
        
        # Predict button
        predict_btn = tk.Button(
            window,
            text="Predict",
            command=predict,
            font=("Arial", 12),
            bg="#2196F3",
            fg="white",
            width=15,
            cursor="hand2"
        )
        predict_btn.pack(pady=10)
        
        # Back button
        back_btn = tk.Button(
            window,
            text="Back to Menu",
            command=window.destroy,
            font=("Arial", 10),
            bg="#757575",
            fg="white",
            width=15,
            cursor="hand2"
        )
        back_btn.pack(pady=5)
    
    def open_multiple_regression(self):
        """Open Multiple Linear Regression window"""
        if self.multiple_model is None:
            messagebox.showerror("Error", "model.pkl model file not found!")
            return
        
        window = tk.Toplevel(self.root)
        window.title("Multiple Linear Regression")
        window.geometry("500x500")
        window.configure(bg="#f0f0f0")
        
        # Title
        title = tk.Label(
            window,
            text="Startup Profit Prediction",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0"
        )
        title.pack(pady=20)
        
        # Input frame
        input_frame = tk.Frame(window, bg="#f0f0f0")
        input_frame.pack(pady=10)
        
        # Location inputs
        tk.Label(
            input_frame,
            text="California (0 or 1):",
            font=("Arial", 11),
            bg="#f0f0f0"
        ).grid(row=0, column=0, sticky="w", padx=10, pady=5)
        california_entry = tk.Entry(input_frame, font=("Arial", 11), width=20)
        california_entry.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(
            input_frame,
            text="New York (0 or 1):",
            font=("Arial", 11),
            bg="#f0f0f0"
        ).grid(row=1, column=0, sticky="w", padx=10, pady=5)
        newyork_entry = tk.Entry(input_frame, font=("Arial", 11), width=20)
        newyork_entry.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(
            input_frame,
            text="Florida (0 or 1):",
            font=("Arial", 11),
            bg="#f0f0f0"
        ).grid(row=2, column=0, sticky="w", padx=10, pady=5)
        florida_entry = tk.Entry(input_frame, font=("Arial", 11), width=20)
        florida_entry.grid(row=2, column=1, padx=10, pady=5)
        
        tk.Label(
            input_frame,
            text="R&D Spend:",
            font=("Arial", 11),
            bg="#f0f0f0"
        ).grid(row=3, column=0, sticky="w", padx=10, pady=5)
        rd_entry = tk.Entry(input_frame, font=("Arial", 11), width=20)
        rd_entry.grid(row=3, column=1, padx=10, pady=5)
        
        tk.Label(
            input_frame,
            text="Administration Spend:",
            font=("Arial", 11),
            bg="#f0f0f0"
        ).grid(row=4, column=0, sticky="w", padx=10, pady=5)
        admin_entry = tk.Entry(input_frame, font=("Arial", 11), width=20)
        admin_entry.grid(row=4, column=1, padx=10, pady=5)
        
        tk.Label(
            input_frame,
            text="Marketing Spend:",
            font=("Arial", 11),
            bg="#f0f0f0"
        ).grid(row=5, column=0, sticky="w", padx=10, pady=5)
        marketing_entry = tk.Entry(input_frame, font=("Arial", 11), width=20)
        marketing_entry.grid(row=5, column=1, padx=10, pady=5)
        
        # Result label
        result_label = tk.Label(
            window,
            text="",
            font=("Arial", 14, "bold"),
            bg="#f0f0f0",
            fg="#FF9800"
        )
        result_label.pack(pady=20)
        
        def predict():
            try:
                california = int(california_entry.get())
                newyork = int(newyork_entry.get())
                florida = int(florida_entry.get())
                rd = int(rd_entry.get())
                admin = int(admin_entry.get())
                marketing = int(marketing_entry.get())
                
                # Validate binary inputs
                if california not in [0, 1] or newyork not in [0, 1] or florida not in [0, 1]:
                    result_label.config(
                        text="Location values must be 0 or 1",
                        fg="#f44336"
                    )
                    return
                
                user_input = {
                    'california': california,
                    'newyork': newyork,
                    'florida': florida,
                    'rd': rd,
                    'admin': admin,
                    'marketing': marketing
                }
                
                user_data = pd.DataFrame(user_input, index=[0])
                prediction = self.multiple_model.predict(user_data)
                
                result_label.config(
                    text=f"Predicted Profit: ${int(prediction[0]):,}",
                    fg="#FF9800"
                )
            except ValueError:
                result_label.config(
                    text="Please enter valid numbers",
                    fg="#f44336"
                )
            except Exception as e:
                result_label.config(
                    text=f"Error: {str(e)}",
                    fg="#f44336"
                )
        
        # Predict button
        predict_btn = tk.Button(
            window,
            text="Predict",
            command=predict,
            font=("Arial", 12),
            bg="#FF9800",
            fg="white",
            width=15,
            cursor="hand2"
        )
        predict_btn.pack(pady=10)
        
        # Back button
        back_btn = tk.Button(
            window,
            text="Back to Menu",
            command=window.destroy,
            font=("Arial", 10),
            bg="#757575",
            fg="white",
            width=15,
            cursor="hand2"
        )
        back_btn.pack(pady=5)


def main():
    root = tk.Tk()
    app = LinearRegressionApp(root)
    root.mainloop()


if _name_ == "_main_":
    main()
