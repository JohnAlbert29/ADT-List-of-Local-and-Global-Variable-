recd = []
def getRec():
    name = input("Enter Name: ")
    quiz = []
    for a in range(3):
        quiz.append(float(input("Enter Quiz {}: ".format(a+1))))
    recd.append({'name': name, 'quiz': quiz})

def display():
    print("Name    Quiz1    Quiz2    Quiz3    Ave    Remarks")  
    for a, record in enumerate(recd):
        ave = sum(record['quiz'])/len(record['quiz'])
        if ave >= 75.0:
            remarks = "Passed"
        else:
            remarks = "Failed"
        print("{:<7} {:<7} {:<7} {:<7} {:<10.2f} {:<7}".format(record['name'], record['quiz'][0], record['quiz'][1], record['quiz'][2], ave, remarks))
        
def avg():
    for record in recd:
        avg = sum(record['quiz'])/len(record['quiz'])

for a in range(0,2):
 getRec()
 display()
 avg()