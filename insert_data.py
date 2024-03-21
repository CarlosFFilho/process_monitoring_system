from tkinter import *
from main import *
from results import *


def btn_clicked():
    
    NewData(entry0.get(), entry1.get(), entry2.get(), entry3.get())
    
    previsao_oa_flow = TrainPredict.Train_Predict_OA(entry0.get(), entry1.get(), entry2.get(), entry3.get())
    previsao_oa_flow = round(previsao_oa_flow[0], 1)
    
    previsao_conversion = TrainPredict.Train_Predict_Conversions(entry0.get(), entry1.get(), entry2.get(), entry3.get())
    previsao_conversion = round(previsao_conversion[0]*100, 1)
    
    previsao_water = TrainPredict.Train_Predict_Water(entry0.get(), entry1.get(), entry2.get(), entry3.get())
    previsao_water = round(previsao_water[0], 1)
    
    results = StatusAndRecommend.Status_Concept(previsao_oa_flow, entry0.get(), entry1.get(), entry2.get(), entry3.get(), previsao_conversion, previsao_water)

    triolein_feed = round(results[2], 1) if results[2] != ' ' else ' '
    water_feed = round(results[3], 1) if results[3] != ' ' else ' '
    pressure = round(results[4], 1)  if results[4] != ' ' else ' '
    tubes = round(results[5], 1) if results[5] != ' ' else ' '
    process_status = results[0]
    recommended_actions = results[1]
    
    status_page (previsao_conversion, previsao_water, previsao_oa_flow, triolein_feed, water_feed, pressure, tubes, process_status, recommended_actions)

window = Tk()

window.geometry("832x531")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 531,
    width = 832,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"images/background.png")
background = canvas.create_image(
    416.0, 265.5,
    image=background_img)

entry0_img = PhotoImage(file = f"images/img_textBox0.png")
entry0_bg = canvas.create_image(
    188.0, 388.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry0.place(
    x = 162, y = 380,
    width = 52,
    height = 15)

entry1_img = PhotoImage(file = f"images/img_textBox1.png")
entry1_bg = canvas.create_image(
    337.0, 388.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry1.place(
    x = 311, y = 380,
    width = 52,
    height = 15)

entry2_img = PhotoImage(file = f"images/img_textBox2.png")
entry2_bg = canvas.create_image(
    473.0, 388.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry2.place(
    x = 447, y = 380,
    width = 52,
    height = 15)

entry3_img = PhotoImage(file = f"images/img_textBox3.png")
entry3_bg = canvas.create_image(
    619.0, 388.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry3.place(
    x = 593, y = 380,
    width = 52,
    height = 15)

img0 = PhotoImage(file = f"images/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 362, y = 440,
    width = 109,
    height = 27)

window.resizable(False, False)
window.mainloop()
