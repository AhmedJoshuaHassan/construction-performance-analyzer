#file = input("Enter file name: ")
file = "project_data.txt"
file_op = open(file)
project = {}


for line in file_op:
    line = line.rstrip()
    line = line.split(",")
    number, name, PV, EV, AC = line
    #Cost Variance
    CV = float(EV) - float(AC)
    #Schedule Variance
    SV = float(EV) - float(PV)
    #Cost Performance Indicator
    CPI = round(float(EV)/float(AC),2)
    #Schedule Performance Indicator
    SPI = round(float(EV)/float(PV),2)
    
    project[number] = {"name":name, "PV":PV, "EV":EV, "AC":AC, "CV":CV, "SV":SV, "CPI":CPI, "SPI":SPI}
    
    #activity schedule Status
    if project[number]["SPI"]>1:
        activity_sstatus = "AHEAD OF SCHEDULE"
    elif project[number]["SPI"]==1:
        activity_sstatus = "ON SCHEDULE"
    else:
        activity_sstatus = "BEHIND SCHEDULE"

    #Overall Budget Status
    if project[number]["CPI"]>1:
        activity_cstatus = "OVER-BUDGET"
    elif project[number]["CPI"]>1:
        activity_cstatus = "ON-BUDGET"
    else:
        project_cstatus = "UNDER-BUDGET"
        
    project[number] = {"name":name, "PV":PV, "EV":EV, "AC":AC, "CV":CV, "SV":SV, "CPI":CPI, "SPI":SPI,"Schedule Status": activity_sstatus, "Cost Status": activity_cstatus}
    
total_PV = 0
total_EV = 0
total_AC = 0

for activity in project:
    total_PV = total_PV + float(project[activity]["PV"])
    total_EV = total_EV + float(project[activity]["EV"])
    total_AC = total_AC + float(project[activity]["AC"])

    
project_SV = total_EV - total_PV
project_CV = total_EV - total_AC
project_SPI = round(total_EV/total_PV,2)
project_CPI = round(total_EV/total_AC,2)

#Overall Schedule Status
if project_SPI>1:
    project_sstatus = "AHEAD OF SCHEDULE"
elif project_SPI==1:
    project_sstatus = "ON SCHEDULE"
else:
    project_sstatus = "BEHIND SCHEDULE"

#Overall Budget Status
if project_CPI>1:
    project_cstatus = "OVER-BUDGET"
elif project_SPI==1:
    project_cstatus = "ON-BUDGET"
else:
    project_cstatus = "UNDER-BUDGET"
    
print(f"Project Summary\nProject SPI:{project_SPI}\nProject CPI: {project_CPI}\nOverall Schedule Status:{project_sstatus}\nOverall Cost Status:{project_cstatus}")

print(project)