import csv
import os
from datetime import date
FILE_NAME="job_applications.csv"
FIELDS=["ID","Company","Job_Role","Applied_Date","Status"]
STATUSES=["Applied","Interview","Selected","Rejected"]
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME,"w",newline="",encoding="utf-8")as file:
            writer=csv.DictWriter(file,fieldnames=FIELDS)
            writer.writeheader()
def load_applications():
    create_file()
    with open(FILE_NAME,"r",newline="",encoding="utf-8")as file:
       return list(csv.DictReader(file))
def save_application(applications):
    with open(FILE_NAME,"w",newline="",encoding="utf-8")as file:
            writer=csv.DictWriter(file,fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(applications)
def add_applications():
    applications=load_applications()
    company=input("Enter company name:").strip()
    role=input("Enter job role:").strip()
    if not company or not role:
        print("Company name and Job role cannot be empty.")
        return
    next_id=max((int(app["ID"])for app in applications),default=0)+1
    application={"ID":next_id,"Company":company,"Job_Role":role,"Applied_Date":date.today().isoformat(),"Status":"Applied"}
    applications.append(application)
    save_application(applications)
    print("Job application added successfully!")
def view_applications():
    applications=load_applications()
    if not applications:
        print("No job applications found.")
        return
    print("\n----------JOB APPLICATIONS------------")
    print("-"*85)
    print(f"{'ID':<5}{'Company':<22}{'Job Role':<25}"f"{'Applied Date':<16}{'Status'}")
    print("-"*85)
    for app in applications:
        print(f"{app['ID']:<5}{app['Company'][:20]:<22}"f"{app['Job_Role'][:23]:<25}"f"{app['Applied_Date']:<16}{app['Status']}")
def search_application():
    applications=load_applications()
    company=input("Enter company name to search:").strip().lower()
    matches=[app for app in applications if company in app["Company"].lower()]
    if matches:
        for app in matches:
            print(app)
    else:
        print("No matching applications found.")
def update_status():
    applications=load_applications()
    try:
        app_id=int(input("Enter application id:"))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return
    for app in applications:
        if int(app["ID"])==app_id:
            print("Available Statuses:", ",".join(STATUSES))
            status=input("Enter new status:").strip().title()
            if status not in STATUSES:
                  print("Invalid status.")
                  return
            app["Status"]=status
            save_application(applications)
            print("Application status updated!")
            return
    print("Application ID not found!")
def delete_application():
    applications=load_applications()
    try:
        app_id=int(input("Enter application ID to be delete:"))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return
    remaining=[app for app in applications if int(app["ID"])!=app_id]
    if len(remaining)==len(applications):
        print("Application id not found.")
        return
    save_application(remaining)
    print("Application deleted successfully!")
def show_summary():
    applications=load_applications()
    print("\n======JOB SEARCH SUMMARY ====")
    print("Total applications:",len(applications))
    for status in STATUSES:
        count=sum(app["Status"]==status for app in applications)
        print(f"{status}:{count}")
def main():
    create_file()
    while True:
        print("\n====== JOB APPLICATIONS TRACKER====")
        print("1.Add Job Application")
        print("2.View all Applications")
        print("3.Search by Company")
        print("4.Update Application Status")
        print("5.Delete Application")
        print("6.View Summary")
        print("7.Exit")
        choice=input("Enter your choice(1-7):").strip()
        if choice=="1":
            add_applications()
        elif choice=="2":
            view_applications()
        elif choice=="3":
            search_application()
        elif choice=="4":
            update_status()
        elif choice=="5":
            delete_application()
        elif choice=="6":
            show_summary()
        elif choice=="7":
            print("Thank you for using Job Application Tracker!")
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")
if __name__=="__main__":
    main()





































    
