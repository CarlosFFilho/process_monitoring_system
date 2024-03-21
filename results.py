from tkinter import *

def status_page (conversion_rate, water_consumption, product_flow, triolein_feed, water_feed, pressure, tubes, process_status, recommended_actions):

    window2 = Toplevel()
    
    window2.geometry("832x531")
    window2.configure(bg = "#ffffff")
    canvas = Canvas(
        window2,
        bg = "#ffffff",
        height = 531,
        width = 832,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)
    
    background2_img = PhotoImage(file = f"images/background_2.png")
    background2 = canvas.create_image(
        416.0, 265.5,
        image=background2_img)
    
    canvas.create_text(
        279.0, 215.0,
        text = conversion_rate,
        fill = "#000000",
        font = ("SofiaSansRoman", int(10.0), "bold"))
    
    canvas.create_text(
        683.5, 215.0,
        text = water_consumption,
        fill = "#000000",
        font = ("SofiaSansRoman", int(10.0), "bold"))
    
    canvas.create_text(
        464.5, 215.0,
        text = product_flow,
        fill = "#000000",
        font = ("SofiaSansRoman", int(10.0), "bold"))
    
    canvas.create_text(
        207.5, 443.0,
        text = triolein_feed,
        fill = "#000000",
        font = ("SofiaSansRoman", int(10.0), "bold"))
    
    canvas.create_text(
        367.5, 443.0,
        text = water_feed,
        fill = "#000000",
        font = ("SofiaSansRoman", int(10.0), "bold"))
    
    canvas.create_text(
        507.5, 443.0,
        text = pressure,
        fill = "#000000",
        font = ("SofiaSansRoman", int(10.0), "bold"))
    
    canvas.create_text(
        646.0, 443.0,
        text = tubes,
        fill = "#000000",
        font = ("SofiaSansRoman", int(10.0), "bold"))
    
    canvas.create_text(
        416.0, 281.0,
        text = process_status,
        fill = "#FF0000" if process_status == "PROPER CONVERSION NOT ACHIEVED!" else '#00FF00',
        font = ("SofiaSansRoman", int(10.0), "bold"))
    
    canvas.create_text(
        417.0, 348.0,
        text = recommended_actions,
        fill = "#000000",
        font = ("SofiaSansRoman", int(7.5), "bold"))
    
    window2.resizable(False, False)
    window2.mainloop()
