#import module
import pyautogui as pg
import time

message=input("Masukan Pesan: ")
jumlah=input("Masukan Jumlah Pesan Spam: ")
print("Arahkan Cursor Ketempat Yang Ingin DiSpam Sebelum Waktu Habis")
print("Processing..")

counter=0
while(counter<=5):
    time.sleep(1)
    print(counter)
    counter+=1

for i in range(1,int(jumlah)):
    pg.typewrite(message+'\n')

print("Selesai")
print("By Aldev Developer")
print("Sedekah 089513430382")
print("Terimakasih Telah Mencoba Bot Ini")