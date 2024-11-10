import tkinter as tk
import math  # Import math module to handle trigonometric and other scientific calculations

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
SHIFT_ON_COLOR = "#FFD700"  # Gold color to indicate shift is active
RADIAN_ON_COLOR = "#87CEEB"  # Light blue color to indicate radian is active


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("600x700")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.total_expression = ""
        self.current_expression = ""
        self.memory = 0  # Memory storage
        self.is_degree = True  # Degree/radian toggle status
        self.is_shift = False  # Shift button toggle status

        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (2, 1), 8: (2, 2), 9: (2, 3),
            4: (3, 1), 5: (3, 2), 6: (3, 3),
            1: (4, 1), 2: (4, 2), 3: (4, 3),
            0: (5, 2), '.': (5, 1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 6):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.create_memory_buttons()
        self.create_log_buttons()
        self.create_deg_rad_button()
        self.create_backspace_and_shift_buttons()
        self.create_power_button()  # Adding power button
        self.create_exp_button()  # Adding exp button
        self.bind_keys()

        # Create variables for buttons that need to change labels
        self.sin_button = None
        self.cos_button = None
        self.tan_button = None
        self.sinh_button = None
        self.cosh_button = None
        self.tanh_button = None

        # After creating buttons, we will call update_shift_display
        self.create_trigonometric_buttons()

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()
        self.create_percentage_button()
        self.create_parentheses_buttons()

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,
                         fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        divide_button = tk.Button(self.buttons_frame, text="\u00F7", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                                  borderwidth=0, command=lambda: self.append_operator("/"))
        divide_button.grid(row=1, column=4, sticky=tk.NSEW)

        multiply_button = tk.Button(self.buttons_frame, text="\u00D7", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                                    borderwidth=0, command=lambda: self.append_operator("*"))
        multiply_button.grid(row=2, column=4, sticky=tk.NSEW)

        minus_button = tk.Button(self.buttons_frame, text="-", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                                 borderwidth=0, command=lambda: self.append_operator("-"))
        minus_button.grid(row=3, column=4, sticky=tk.NSEW)

        plus_button = tk.Button(self.buttons_frame, text="+", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                                borderwidth=0, command=lambda: self.append_operator("+"))
        plus_button.grid(row=4, column=4, sticky=tk.NSEW)

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.clear)
        button.grid(row=1, column=5, sticky=tk.NSEW)

    def create_percentage_button(self):
        button = tk.Button(self.buttons_frame, text="%", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.percentage)
        button.grid(row=1, column=6, sticky=tk.NSEW)

    def percentage(self):
        try:
            self.current_expression = str(eval(f"({self.current_expression}) / 100"))
            self.update_label()
        except Exception as e:
            print(f"Error in percentage: {e}")
            self.current_expression = "Error"
            self.update_label()

    def square(self):
        self.current_expression = "square("
        self.update_label()

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.square)
        button.grid(row=1, column=2, sticky=tk.NSEW)

    def sqrt(self):
        self.current_expression += "√("
        self.update_label()

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.sqrt)
        button.grid(row=1, column=3, sticky=tk.NSEW)

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            # Apply inverse functions if shift is on
            if self.is_shift:
                self.total_expression = self.total_expression.replace("sin", "math.asin")
                self.total_expression = self.total_expression.replace("cos", "math.acos")
                self.total_expression = self.total_expression.replace("tan", "math.atan")
                self.total_expression = self.total_expression.replace("sinh", "asinh")
                self.total_expression = self.total_expression.replace("cosh", "acosh")
                self.total_expression = self.total_expression.replace("tanh", "atanh")
            else:
                self.total_expression = self.total_expression.replace("sin", "math.sin")
                self.total_expression = self.total_expression.replace("cos", "math.cos")
                self.total_expression = self.total_expression.replace("tan", "math.tan")
                self.total_expression = self.total_expression.replace("sinh", "sinh")
                self.total_expression = self.total_expression.replace("cosh", "cosh")
                self.total_expression = self.total_expression.replace("tanh", "tanh")

            # Add log and ln using math module
            self.total_expression = self.total_expression.replace("ln", "log")
            self.total_expression = self.total_expression.replace("log", "log10")

            # Handle power and roots
            if self.is_shift:
                self.total_expression = self.total_expression.replace("^", "**(1/")
            else:
                self.total_expression = self.total_expression.replace("^", "**")

            print(f"Evaluating: {self.total_expression}")  # Print statement for debugging

            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            print(f"Error in evaluation: {e}")  # Print the error for debugging
            self.current_expression = "Error"
        finally:
            self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.evaluate)
        button.grid(row=5, column=3, columnspan=2, sticky=tk.NSEW)

    def create_memory_buttons(self):
        memory_add_button = tk.Button(self.buttons_frame, text="M+", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                                      borderwidth=0, command=self.memory_add)
        memory_add_button.grid(row=5, column=5, sticky=tk.NSEW)

        memory_subtract_button = tk.Button(self.buttons_frame, text="M-", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                                           borderwidth=0, command=self.memory_subtract)
        memory_subtract_button.grid(row=5, column=6, sticky=tk.NSEW)

        memory_recall_button = tk.Button(self.buttons_frame, text="MR", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                                         borderwidth=0, command=self.memory_recall)
        memory_recall_button.grid(row=1, column=7, sticky=tk.NSEW)

        memory_clear_button = tk.Button(self.buttons_frame, text="MC", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                                        borderwidth=0, command=self.memory_clear)
        memory_clear_button.grid(row=2, column=7, sticky=tk.NSEW)

    def memory_add(self):
        try:
            self.memory += float(self.current_expression)
            self.update_label()
        except Exception as e:
            print(f"Error in memory_add: {e}")
            self.current_expression = "Error"

    def memory_subtract(self):
        try:
            self.memory -= float(self.current_expression)
            self.update_label()
        except Exception as e:
            print(f"Error in memory_subtract: {e}")
            self.current_expression = "Error"

    def memory_recall(self):
        self.current_expression = str(self.memory)
        self.update_label()

    def memory_clear(self):
        self.memory = 0
        self.update_label()

    def create_log_buttons(self):
        ln_button = tk.Button(self.buttons_frame, text="ln", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                              borderwidth=0, command=lambda: self.add_to_expression("ln("))
        ln_button.grid(row=3, column=7, sticky=tk.NSEW)

        log_button = tk.Button(self.buttons_frame, text="log", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=lambda: self.add_to_expression("log("))
        log_button.grid(row=4, column=7, sticky=tk.NSEW)

    def create_deg_rad_button(self):
        self.deg_rad_button = tk.Button(self.buttons_frame, text="D/R", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                                   borderwidth=0, command=self.toggle_deg_rad)
        self.deg_rad_button.grid(row=5, column=7, sticky=tk.NSEW)

    def toggle_deg_rad(self):
        self.is_degree = not self.is_degree
        if self.is_degree:
            self.deg_rad_button.config(bg=OFF_WHITE)
        else:
            self.deg_rad_button.config(bg=RADIAN_ON_COLOR)
        self.label.config(text="Degree" if self.is_degree else "Radian")

    def create_backspace_and_shift_buttons(self):
        backspace_button = tk.Button(self.buttons_frame, text="⌫", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                                     borderwidth=0, command=self.backspace)
        backspace_button.grid(row=1, column=8, sticky=tk.NSEW)

        shift_button = tk.Button(self.buttons_frame, text="SHIFT", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                                 borderwidth=0, command=self.toggle_shift)
        shift_button.grid(row=2, column=8, sticky=tk.NSEW)

    def backspace(self):
        self.current_expression = self.current_expression[:-1]
        self.update_label()

    def toggle_shift(self):
        self.is_shift = not self.is_shift
        self.update_shift_display()

    def update_shift_display(self):
        shift_button = self.buttons_frame.grid_slaves(row=2, column=8)[0]  # Get the shift button
        if self.is_shift:
            shift_button.config(bg=SHIFT_ON_COLOR)
            # Change button labels to their inverse counterparts
            self.sin_button.config(text="asin")
            self.cos_button.config(text="acos")
            self.tan_button.config(text="atan")
            self.sinh_button.config(text="asinh")
            self.cosh_button.config(text="acosh")
            self.tanh_button.config(text="atanh")
        else:
            shift_button.config(bg=OFF_WHITE)
            # Revert button labels to normal functions
            self.sin_button.config(text="sin")
            self.cos_button.config(text="cos")
            self.tan_button.config(text="tan")
            self.sinh_button.config(text="sinh")
            self.cosh_button.config(text="cosh")
            self.tanh_button.config(text="tanh")

    def create_power_button(self):
        power_button = tk.Button(self.buttons_frame, text="^", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                                 borderwidth=0, command=self.add_power_or_root)
        power_button.grid(row=3, column=8, sticky=tk.NSEW)

    def add_power_or_root(self):
        if self.is_shift:
            self.current_expression += "**(1/"
        else:
            self.current_expression += "^"
        self.update_label()

    def create_exp_button(self):
        # Creating the exp button
        exp_button = tk.Button(self.buttons_frame, text="exp", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=lambda: self.add_to_expression("math.exp("))
        exp_button.grid(row=4, column=8, sticky=tk.NSEW)  # Position below ^ and to the right of log

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def create_parentheses_buttons(self):
        parentheses_frame = tk.Frame(self.buttons_frame)
        parentheses_frame.grid(row=1, column=1, sticky=tk.NSEW)

        open_paren_button = tk.Button(parentheses_frame, text="(", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                                      borderwidth=0, command=lambda: self.add_to_expression("("))
        open_paren_button.pack(side=tk.LEFT, expand=True, fill="both")

        close_paren_button = tk.Button(parentheses_frame, text=")", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                                       borderwidth=0, command=lambda: self.add_to_expression(")"))
        close_paren_button.pack(side=tk.RIGHT, expand=True, fill="both")

    def create_trigonometric_buttons(self):
        # SIN Button
        self.sin_button = tk.Button(self.buttons_frame, text="sin", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                                    borderwidth=0, command=lambda: self.add_trigonometric_function("sin"))
        self.sin_button.grid(row=2, column=5, sticky=tk.NSEW)

        # SINH Button
        self.sinh_button = tk.Button(self.buttons_frame, text="sinh", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                                     borderwidth=0, command=lambda: self.add_trigonometric_function("sinh"))
        self.sinh_button.grid(row=2, column=6, sticky=tk.NSEW)

        # COS Button
        self.cos_button = tk.Button(self.buttons_frame, text="cos", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                                    borderwidth=0, command=lambda: self.add_trigonometric_function("cos"))
        self.cos_button.grid(row=3, column=5, sticky=tk.NSEW)

        # COSH Button
        self.cosh_button = tk.Button(self.buttons_frame, text="cosh", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                                     borderwidth=0, command=lambda: self.add_trigonometric_function("cosh"))
        self.cosh_button.grid(row=3, column=6, sticky=tk.NSEW)

        # TAN Button
        self.tan_button = tk.Button(self.buttons_frame, text="tan", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                                    borderwidth=0, command=lambda: self.add_trigonometric_function("tan"))
        self.tan_button.grid(row=4, column=5, sticky=tk.NSEW)

        # TANH Button
        self.tanh_button = tk.Button(self.buttons_frame, text="tanh", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                                     borderwidth=0, command=lambda: self.add_trigonometric_function("tanh"))
        self.tanh_button.grid(row=4, column=6, sticky=tk.NSEW)

    def add_trigonometric_function(self, function):
        self.current_expression += f"{function}("
        self.update_label()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
