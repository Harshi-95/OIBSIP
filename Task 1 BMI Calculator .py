from tkinter import *

root = Tk()
root.title("BMI CALCULATOR")
root.geometry("400x300")

title_label = Label(root, text="METRIC BMI CALCULATOR APP", anchor=CENTER, borderwidth=10, fg="blue")
title_label.config(font=("ARIAL", 16))
title_label.grid(row=0, column=0, columnspan=5)

weight = Label(root, text="WEIGHT", borderwidth=1, fg="black", bg="white")
weight.config(font=("Lucida Console", 20))
weight.grid(row=1, column=0)

nill1 = Label(root, text="", borderwidth=4, bg="white").grid(row=2, column=0, columnspan=5)

kg = Label(root, text="kgs", fg="black", bg="white")
kg.config(font=("Lucida Console", 13))
kg.grid(row=1, column=5)

height = Label(root, text="HEIGHT", borderwidth=15, fg="black", bg="white")
height.config(font=("Lucida Console", 20))
height.grid(row=3, column=0)

nill2 = Label(root, text="", borderwidth=4, bg="white").grid(row=4, column=0, columnspan=5)

slider = Scale(root, from_=20, to=120, orient=HORIZONTAL, bd=3, length=200, tickinterval=20, width=15, fg="black", bg="white", troughcolor="blue")
slider.config(highlightbackground="#FFFF99")
slider.set(60)
slider.grid(row=1, column=1, columnspan=4)

height_slider = Scale(root, from_=1.0, to=2.5, orient=HORIZONTAL, bd=3, length=200, tickinterval=0.1, width=15, fg="black", bg="white", troughcolor="blue", resolution=0.01)
height_slider.config(highlightbackground="#FFFF99")
height_slider.set(1.75)
height_slider.grid(row=3, column=1, columnspan=4)

meters = Label(root, text="meters", fg="black", bg="white")
meters.config(font=("Lucida Console", 13))
meters.grid(row=3, column=5)

def calculate_bmi():
    weight = slider.get()
    height = height_slider.get()
    bmi = weight / (height ** 2)
    return bmi

def sub():
    new = Tk()
    new.title("YOUR BMI RESULTS")
    new.geometry("445x80")
    new.configure(bg="blue")
    bmi = calculate_bmi()
    result_label = Label(new, text="YOUR BMI : " + str(round(bmi, 2)), bg="blue", fg="#FFFF99")
    result_label.config(font=("Lucida Console", 20))
    result_label.grid(row=0, column=0)
    if bmi < 18.5:
        info_label = Label(new, text="YOU BELONG TO UNDERWEIGHT CATEGORY", bg="white", fg="blue")
        info_label.config(font=("Lucida Console", 15))
        info_label.grid(row=1, column=0)
    elif 18.5 <= bmi < 25:
        info_label = Label(new, text="YOU BELONG TO NORMAL WEIGHT CATEGORY", bg="white", fg="green")
        info_label.config(font=("Lucida Console", 15))
        info_label.grid(row=1, column=0)
    elif 25 <= bmi < 30:
        info_label = Label(new, text="YOU BELONG TO OVER WEIGHT CATEGORY", bg="white", fg="brown")
        info_label.config(font=("Lucida Console", 15))
        info_label.grid(row=1, column=0)
    else:
        info_label = Label(new, text="YOU ARE OBESE..NEED TO BURN OUT A LOT!", bg="white", fg="red")
        info_label.config(font=("Lucida Console", 15))
        info_label.grid(row=1, column=0)

submit = Button(root, text="SUBMIT", command=sub, width=10, borderwidth=5, anchor=CENTER)
submit.configure(bg="blue", fg="#FFFF99")
submit.grid(row=5, column=0, columnspan=5)

root.mainloop()