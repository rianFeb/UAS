import random
import os

os.system(("cls"))
print("=== Batu Gunting Kertas ===")
print("")
print("1. Batu")
print("2. Gunting")
print("3. Kertas")

pilihan = int(input("Pilihan Anda (1/2/3): "))
computer = random.choice(["Batu", "Gunting", "Kertas"])

if pilihan == 1:
    print("Anda     : Batu")
    print("computer : ", computer)
    if computer == "Batu":
        print("Hasil Seimbang")
    elif computer == "Gunting":
        print("Anda Menang")
    elif computer == "Kertas":
        print("Anda Kalah")
if pilihan == 2:
    print("Anda     : Gunting")
    print("computer : ", computer)
    if computer == "Batu":
        print("Anda Kalah")
    elif computer == "Gunting":
        print("Hasil Seimbang")
    elif computer == "Kertas":
        print("Anda Menang")
if pilihan == 3:
    print("Anda     : Kertas")
    print("computer : ", computer)
    if computer == "Batu":
        print("Anda Menang")
    elif computer == "Gunting":
        print("Anda Kalah")
    elif computer == "Kertas":
        print("Hasil Seimbang")
else:
    print("Pilihan salah!")