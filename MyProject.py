from tkinter import *

def meters():
    number = int(number_input.get())

    output = ''
    output += 'เมตร แปลง เป็นกิโลเมตร' + ' = ' + str(number * 1/10**3) + ' กิโลเมตร' + '\n'
    output += 'เมตร แปลง เป็นเซนติเมตร' + ' = ' + str(number * 100) + ' เซนติเมตร' + '\n'
    output += 'เมตร แปลง เป็นมิลลิเมตร' + ' = ' + str(number * 1000000) + ' มิลลิเมตร' + '\n'
    output += 'เมตร แปลง เป็นนาโนเมตร' + ' = ' + str(number * 1000000000000) + ' นาโนเมตร' + '\n'

    output_label.configure(text=output)

def kilometers():
    number = int(number_input.get())

    output = ''
    output += 'กิโลเมตร แปลง เป็นเมตร' + ' = ' + str(number * 1000) + ' เมตร' + '\n'
    output += 'กิโลเมตร แปลง เป็นเซนติเมตร' + ' = ' + str(number * 100000) + ' เซนติเมตร' + '\n'
    output += 'กิโลเมตร แปลง เป็นมิลลิเมตร' + ' = ' + str(number * 1000000) + ' มิลลิเมตร' + '\n'
    output += 'กิโลเมตร แปลง เป็นนาโนเมตร' + ' = ' + str(number * 1000000000000) + ' นาโนเมตร' + '\n'

    output_label.configure(text=output)

def centimeters():
    number = int(number_input.get())

    output = ''
    output += 'เซนติเมตร แปลง เป็นเมตร' + ' = ' + str(number * 1/10**2) + ' เมตร' + '\n'
    output += 'เซนติเมตร แปลง เป็นกิโลเมตร' + ' = ' + str(number * 1/10**5) + ' กิโลติเมตร' + '\n'
    output += 'เซนติเมตร แปลง เป็นมิลลิเมตร' + ' = ' + str(number * 10) + ' มิลลิเมตร' + '\n'
    output += 'เซนติเมตร แปลง เป็นนาโนเมตร' + ' = ' + str(number * 10000000) + ' นาโนเมตร' + '\n'

    output_label.configure(text=output)

def millimeters():
    number = int(number_input.get())

    output = ''
    output += 'มิลลิเมตร แปลง เป็นเมตร' + ' = ' + str(number * 1/10**3) + ' เมตร' + '\n'
    output += 'มิลลิเมตร แปลง เป็นกิโลมตร' + ' = ' + str(number * 1/10**6) + ' กิโลติเมตร' + '\n'
    output += 'มิลลิเมตร แปลง เป็นเซนติเมตร' + ' = ' + str(number * 1/10) + ' เซนติเมตร' + '\n'
    output += 'มิลลิเมตร แปลง เป็นนาโนเมตร' + ' = ' + str(number * 1000000) + ' นาโนเมตร' + '\n'

    output_label.configure(text=output)

def nanometers():
    number = int(number_input.get())

    output = ''
    output += 'นาโนเมตร แปลง เป็นเมตร' + ' = ' + str(number * 1/10**9) + ' เมตร' + '\n'
    output += 'นาโนเมตร แปลง เป็นกิโลเมตร' + ' = ' + str(number * 1/10**12) + ' กิโลเมตร' + '\n'
    output += 'นาโนเมตร แปลง เป็นเซนติเมตร' + ' = ' + str(number * 1/10**7) + ' เซนติเมตร' + '\n'
    output += 'นาโนเมตร แปลง เป็นมิลลิเมตร' + ' = ' + str(number * 1/10**6) + ' มิลลิเมตร' + '\n'

    output_label.configure(text=output)

window = Tk()
window.title('MyProject')
window.minsize(width=280, height=320)
window.configure(background='#111111')

title_label = Label(master=window, text='แปลงคำอุปสรรค'.upper(), background="#111111", fg="white")
title_label.pack(pady=3)

number_input = Entry(master=window, background="#222222" , fg="white")
number_input.pack(pady=10)

go_button = Button(master=window, text="แปลงจากเมตร", background="#333333", fg="white", command=meters)
go_button.pack(pady=3)
go_button = Button(master=window, text="แปลงจากกิโลเมตร", background="#333333", fg="white", command=kilometers)
go_button.pack(pady=3)
go_button = Button(master=window, text="แปลงจากเซนติเมตร", background="#333333", fg="white", command=centimeters)
go_button.pack(pady=3)
go_button = Button(master=window, text="แปลงมิลลิเมตร", background="#333333", fg="white", command=millimeters)
go_button.pack(pady=3)
go_button = Button(master=window, text="แปลงจากนาโนเมตร", background="#333333", fg="white", command=nanometers)
go_button.pack(pady=3)

output_label = Label(master=window, background="#111111", fg="white")
output_label.pack(pady=5)

window.mainloop()