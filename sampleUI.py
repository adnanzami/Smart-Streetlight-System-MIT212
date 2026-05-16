#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 13:37:38 2026

@author: Lushant
"""

def heading(name):

        print("-" * 40)
        print(f"        {name}")
        print("-" * 40)
    
    
    
def main_menu():
        print("\n1. Manage Streetlights")
        print("2. Manage Maintenance Ticket")
        print("3. Track Energy Usage")

        
        print("4. Exit ")
    
    
    
    
def registration_input():
        print( "\nChoose a Zone ID:" +
              "\n  Z1 = Karabar" +
             "\n  Z2 = Woden" +
             "\n  Z3 = Holt")
        
        zoneID = (input("\nEnter your choice: ")).lower()
        streetLightID = input("\nEnter Streetlight ID: " +zoneID+ "sl")
        registrationDate = input("\nEnter registration date: ")
        location = input("\nEnter the street address: ")
        lightType = input("\nEnter the type of the streetlight: ")
        powerRating = float(input("\nEnter the power rating of the streetlight (Watts): "))
        lightStatus = input("\nEnter the status of the streetlight (ON / OFF/ FAULTY): ")
        

        
        print("\n YOUR REGISTRATION WAS SUCCESSFULL !!! \n")
        
        heading("REGISTRATION DETAILS")
        
        
        
        print(f"\nStreetlight ID : {streetLightID}  \nLocation: {location} \nLight Type: {lightType} \nPower Rating: {powerRating} \nLight Status: {lightStatus}\n\n")
          
       
        lightInfo = [streetLightID, zoneID, location, lightType, powerRating, lightStatus ]
       
        print(lightInfo) #Checking what is inside the array
        
        
        
        
def registration_menu():
            print("\n1. Register a streetlight")
            print("2. Update street light details")
            print("3. View street light details ")
            print("4. Show Malfunctioning Streetlights")
            print("5. Remove decomissioned lights")
            print("6. Go Back \n")
            
            
            choice = input("Please enter an option: " )
            
            if choice == "1":
                heading("STREETLIGHT REGISTRATION")
                registration_input()
            elif choice == "2":
                heading("UPDATE STREETLIGHT DETAILS")
                update_input()
            elif choice == "3":
                
                heading("VIEW STREETLIGHT DETAILS")
            elif choice == "4":
                heading("REMOVE STREETLIGHT")
                print("you chose option 4")
            elif choice == "5":
                print('option 5')
            elif choice =="6":
                return
            else:
                print("Please enter a valid option")
                

        
        
def update_input():
        streetLightID = input("\nEnter Streetlight ID to update: ")
        
        print( "\nChoose a Zone ID:" +
              "\n  Z1 = Karabar" +
             "\n  Z2 = Woden" +
             "\n  Z3 = Holt")
        
        zoneID = input("\nEnter your choice: ")

        location = input("\nEnter the street address: ")
        lightType = input("\nEnter the type of the streetlight: ")
        powerRating = float(input("\nEnter the power rating of the streetlight (Watts): "))
        lightStatus = input("\nEnter the status of the streetlight (ON / OFF/ FAULTY): ")
        

        
        print("\n YOUR REGISTRATION WAS SUCCESSFULL !!! \n")
        
        heading("REGISTRATION DETIALS")
        
        
        
        print(f"\nStreetlight ID : {streetLightID}  /nRegistration Date (DD/MM/YYYY): {registrationDate} \nLocation: {location} \nLight Type: {lightType} \nPower Rating: {powerRating} \nLight Status: {lightStatus}\n\n")
          
       
        lightInfo = [streetLightID, zoneID, location, lightType, powerRating, lightStatus ]
       
        print(lightInfo) #Checking what is inside the array
        
        
        
        
        
        
        
        

def maintenance_input():
    
        streetLightID = input("\nEnter streetlight ID: ")
        date = input("\nEnter date: ")
        technicianName = input("\nEnter technician name: ")
        description= input("\nEnter fault description: ")
        
        print("\nChoose the status of the streetlight")
        print("1. Fixed \n2. Pending \n3. Decommissioned")
        lightStatus = input("\nEnter the status: ")
        

        
        print("\nRECORD ADDED SUCCESSFULLY !!! \n")
        
  
        

def main():
    
    
    url = "mongodb+srv://lushant:adminLushant@clusterlushant.o9igtd2.mongodb.net/?appName=ClusterLushant"
    
    while True:
        heading("MAIN MENU")
        main_menu()
        
        option = input("\nPlease choose an option: ")
        print("\n")
        
      
        
        if option == "1":
            
            heading("MANAGE STREET LIGHTS")
            registration_menu()
            

            

            
        elif option == "2" :
            heading("MANAGE MAINTENANCE RECORDS")
            
            print("\n1. Enter maintenance record")
            print("2. Update maintenance record")
            print("3. View maintenance record")
            print("4. Delete maintenance record")
            print("5. Go Back \n")
                        
            choice = input("Please enter an option: " )
            
            if choice == "1":
                heading("ENTER RECORD")
                maintenance_input()
               
            elif choice == "2":
                heading("UPDATE RECORD")
   
            elif choice == "3":
                heading("VIEW RECORD")
                
            elif choice == "4":
                heading("REMOVE RECORD")
                print("you chose option 4")
                
            elif choice == "5":
                continue
        
        
        elif option == "3":
            print("Do Something")
            
        elif option == "4":
            print("Do Something")
            
       
            
        elif option == "5":
           
            print("EXITING...")
            return
            
        else:
            print("!!!  PLEASE ENTER A VALID OPTION  !!! \n")
        
    

if __name__ == "__main__":
    main()