from math import *
import sys

arr = [1.2, 1.38, 1.46, 1.55, 1.64, 1.73 ,1.9]

def risinajums(svars, augums, vecums, dzimus):
    print("Trukst fiziska slodze vai minimala (1)")
    print("Videji smaguma trenini 3 reizes nedela  (2)")
    print("Videji smaguma trenini 5 reizes nedela (3)")
    print("Intensivas trenini 5 reizes nedela (4)")
    print("Trenini katru dienu (5)")
    print("Intensivie trenini katru dienu vai 2 reizes diena (6)")
    print("Ikdienas slodze + fiziskais darbs (7)")
    a = int(input("Izvelieties savu fizisko aktivitati: "))
    if a<1 and a>7:
        print("Jus ievadijat nepareizus datus")
        return 0
    if dzimus=="sieviesu":
        dci = (svars*10 + augums*6.25 - vecums*5 - 161) * arr[a-1]
    elif dzimus=="viriesu":
        dci = (svars*10 + augums*6.25 - vecums*5 + 5) * arr[a-1]
    return dci

def kalorijuDaudzumsNoLaika(laiks,dci):
    if laiks=="brokastis":
        return round(0.25*dci)
    elif laiks=="pusdienas":
        return round(0.4*dci)
    elif laiks=="vakarinas":
        return round(0.25*dci)
    return 0


print("Si programma ir prieks cilvekiem, kurs ir vecaks par 16 gadiem")
print()

svars = float(input("Ievadiet jusu svaru: (kg): "))
augums = float(input("Ievadiet jusu augumu (cm): "))
vecums = int(input("Ievadiet jusu vecumu (16+): "))
dzimus = str(input("Ievadiet jusu dzimumu (viriesu vai sieviesu): "))

print()

if svars>=30 and augums>=66 and vecums>=16:
    dci = risinajums(svars, augums, vecums, dzimus)
    if dci != 0:
        print("Jusu optimalais kaloriju daudzums ir:", round(dci), "kaloriju diena")
else:
    print("Jus ievadijat nepareizus datus")
    sys.exit()
    

print()
print("Tagad jus varesiet uzzinat kads kaloriju daudzums jums ir nepiciesams ")
laiks = str(input("Ievadiet edienas laiku (brokastis, pusdienas, vakarinas): "))
res = kalorijuDaudzumsNoLaika(laiks,dci)
if res!=0:
    print("Jusu optimalais kaloriju daudzums laika(",laiks,") ir:",res)
else:
    print("Jus ievadijat nepareizus datus")
    
    
