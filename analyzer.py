print("="*45)
print("CONSTRUCTION PROJECT PERFORMANCE REPORT")
print("="*45)
#filename = "project_data.txt"
file = input("Enter file name: ")
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
    
    #Activity schedule Status
    if project[number]["SPI"]>1.0:
        activity_sstatus = "AHEAD OF SCHEDULE"
    elif project[number]["SPI"]==1.0:
        activity_sstatus = "ON SCHEDULE"
    elif project[number]["SPI"]<1.0:
        activity_sstatus = "BEHIND SCHEDULE"

    #Activity Budget Status
    if project[number]["CPI"]>1.0:
        activity_cstatus = "UNDER-BUDGET"
    elif project[number]["CPI"]==1.0:
        activity_cstatus = "ON-BUDGET"
    elif project[number]["CPI"]<1.0:
        activity_cstatus = "OVER-BUDGET"
        
    project[number] = {"name":name, "PV":PV, "EV":EV, "AC":AC, "CV":CV, "SV":SV, "CPI":CPI, "SPI":SPI,"Schedule Status": activity_sstatus, "Cost Status": activity_cstatus}

total_activities = 0         #Total Activities
ahead_of_schedule = 0  #Number of Activities Ahead of Schedule
on_schedule = 0     #Number of Activities on Schedule
behind_schedule = 0    #Number of Activities Behind Schedule

for activity in project:
    total_activities = total_activities+1
    if project[activity]["Schedule Status"]=="AHEAD OF SCHEDULE":
        ahead_of_schedule = ahead_of_schedule + 1
    elif project[activity]["Schedule Status"]=="ON SCHEDULE":
        on_schedule = on_schedule+1
    elif project[activity]["Schedule Status"]=="BEHIND SCHEDULE":
        behind_schedule = behind_schedule+1
print("")   #empty line
print(f"Total Activities: {total_activities}\nActivities Ahead of Schedule: {ahead_of_schedule}\nActivities On Schedule: {on_schedule}\nActivities Behind Schedule: {behind_schedule}")
print("")   #empty line
#print(project)


#OVERALL PROJECT PERFORMANCE
    
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
    project_cstatus = "UNDER-BUDGET"
elif project_SPI==1:
    project_cstatus = "ON-BUDGET"
else:
    project_cstatus = "OVER-BUDGET"
    
print(f"Project Summary\nProject SPI:{project_SPI}\nProject CPI: {project_CPI}\nOverall Schedule Status:{project_sstatus}\nOverall Cost Status:{project_cstatus}")

#print(project)