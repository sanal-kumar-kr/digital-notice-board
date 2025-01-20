from django.shortcuts import render,redirect
from Authentication.models import Register
from exam.models import Exams
from department.models import *
from subject.models import *
from classroom.models import *
from classallotment.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from random import shuffle
from collections import defaultdict

@login_required(login_url='/login')
def add_classallotment(request):
    a = Departments.objects.all()
    b = Semesters.objects.all()
    c = Subjects.objects.all()
    d = Exams.objects.all()
    e = Classes.objects.all()
    f = Register.objects.filter(usertype ="2",examstatus="0")
    if(request.method == 'POST'):
            # print(request.POST['exam'].date)
            exam_id = request.POST['exam']
            selected_exam = Exams.objects.get(id=exam_id)
            classid = request.POST['classname']
            selected_class = Classes.objects.get(id=classid)

    # Now you can access the attributes of the selected_exam
            # print(selected_class.id)
            cid=selected_class.id

            # # print(request.POST['exam'].start_time)
            # # print(request.POST['exam'].end_time)
            v=ClassAllotments.objects.filter(classroom=cid)
            print(ClassAllotments.objects.filter(classroom=cid,exam__date=selected_exam.date,exam__start_time=selected_exam.start_time,exam__end_time=selected_exam.end_time).exists())

            print(v)

           
           
        # if v: 
        #     for i in v:
        #         s= ClassAllotments.objects.get(exam=i.id)
        #         s.department = Departments.objects.get(id=request.POST['department']),
        #         s.semester = Semesters.objects.get(id=request.POST['semester']),
        #         s.subject = Subjects.objects.get(id=request.POST['subject']),
        #         s.exam = Exams.objects.get(id=request.POST['exam']),
        #         s.classroom = Classes.objects.get(id=request.POST['classname'])
        #         s.save()
                

        
        # else:  
            ClassAllotments.objects.create(
                department = Departments.objects.get(id=request.POST['department']),
                semester = Semesters.objects.get(id=request.POST['semester']),
                subject = Subjects.objects.get(id=request.POST['subject']),
                exam = Exams.objects.get(id=request.POST['exam']),
                classroom = Classes.objects.get(id=request.POST['classname']),
                # staff = Register.objects.get(id=request.POST['name']),
            )
            # a = Register.objects.get(id=request.POST['name'])
            # a.examstatus = 1
            # a.save()
            return redirect('/classallotment_view')
    else:
        return render(request,'classallotment_add.html',{'a':a,'b':b,'c':c,'d':d,'e':e,'f':f})
    
@login_required(login_url='/login')
def view_classallotment(request):
    a = ClassAllotments.objects.all()
    search = request.GET.get('search','')
    if search:
        a = a.filter(Q(exam__examname__icontains=search)|Q(department__departmentname__icontains=search))
        print(a)
        
    return render(request,'classallotment_view.html',{'a':a})

# @login_required(login_url='/login')
# def delete_classallotment(request,id):
#     data = ClassAllotments.objects.get(id=id)
#     staffid=data.staff.id
#     b=Register.objects.get(id=staffid)
#     b.examstatus=0
#     b.save()
#     data.delete()
#     return redirect('/classallotment_view')


@login_required(login_url='/login')
def delete_classallotment(request,id):
    data = ClassAllotments.objects.get(id=id)
    ab = data.classroom
    abc = data.exam
    abcd = data.exam.date
    abcde = data.exam.start_time
    print(abc)
    print(abcd)
    print(abcde)
    c = ClassAllotments.objects.filter(exam__start_time=abcde,exam__date=abcd,classroom=ab,status=1)
    print(ab)
    print(c)
    a = Allot.objects.filter(classroom=data)
    for i in a:
        i.staff
        staffid=i.staff.id
        b=Register.objects.get(id=staffid)
        b.examstatus=0
        b.save()
    if data.status == 1:
        c.delete()
    else:
        data.delete()   
    return redirect('/classallotment_view')


@login_required(login_url='/login')
def edit_classallotment(request,id):
    data = ClassAllotments.objects.get(id=id)
    a = Departments.objects.all()
    b = Semesters.objects.all()
    c = Subjects.objects.all()
    d = Exams.objects.all()
    e = Classes.objects.all()
    f = Register.objects.filter(usertype = "2")
    if request.method == 'POST':
            # j = data.staff.id
            # m = Register.objects.get(id=j)
            # m.examstatus = "0" 
            # m.save()
            data.department = Departments.objects.get(id=request.POST['department'])
            data.semester = Semesters.objects.get(id=request.POST['semester'])
            data.subject = Subjects.objects.get(id=request.POST['subject'])
            data.exam = Exams.objects.get(id=request.POST['exam'])
            data.classroom = Classes.objects.get(id=request.POST['classname'])
            # data.staff = Register.objects.get(id=request.POST['name'])
            # data.strength = e.strength.id
            # k = data.staff.id
            # l = Register.objects.get(id=k)
            # l.examstatus="1"
            # l.save()
            data.save()
            return redirect('/classallotment_view')
    return render(request,'classallotment_edit.html',{'data':data,'d':d,'e':e,'f':f,'a':a,'b':b,'c':c})

     
@login_required(login_url='/login')
def allot_seats(request, id):
    try:

        class_allotment = ClassAllotments.objects.get(id=id)
        a = list(Register.objects.filter(examstatus=0, usertype="2"))
        if not a: 
            a = ClassAllotments.objects.all()

            no_staff_member = True
            return render(request, 'classallotment_view.html', {'no_staff_member': no_staff_member, 'g': False,'a':a})

        print(id)
        print(class_allotment)
        print(a)
        # exit()
        if a:
            staff_member = a.pop(0)
            print(staff_member)
           


        else:
            staff_member = None
        exam = class_allotment.exam
        print(exam)
        rid = class_allotment.classroom.id
        classroom = Classes.objects.get(id=rid)
        print(classroom)
        row = classroom.seatrows
        column = classroom.seatcolumns
        cl = rid
        print(cl)
        abab = class_allotment.exam.date
        ababc = class_allotment.exam.start_time
        print(abab)
        print(ababc)
        ex = ClassAllotments.objects.filter(classroom=classroom, exam__date=abab, exam__start_time=ababc)
        print(ex)
        # exit()

        department_students = defaultdict(list)
        print(department_students)
        print("department_students")
        
        for i in ex:
            aaa = i.department
            print(aaa)
            print("^^^^^^^^^^^^")
            bbb = Register.objects.filter(department=aaa, usertype=3)
            print(bbb)
            for student in bbb:
                department_students[aaa].append(student)
                
        print(111111111111111)
        print(department_students)
        print("rows")
        
        for department, students in department_students.items():
            shuffle(students)
            
        ccount = 0
        print("&&&&&&&&&&&&&")
        
        for x in range(row):
            for y in range(column):
                department = list(department_students.keys())[ccount % len(department_students)]
                students = department_students[department]
                print(students)
                print("students")
                if students:
                    student = students.pop(0)
                    
                    print(students)
                    print(student)
                    student_exam = Exams.objects.get(department=student.department, date=abab, start_time=ababc)
                    print(student_exam)
                    print("*************")
                    allotment = Allot.objects.create(
                        classroom=class_allotment,
                        exam=student_exam,
                        row=x + 1,
                        column=y + 1,
                        staff=staff_member
                    )
                    a = staff_member
                    a.examstatus = 1
                    a.save()
                    print(allotment)
                    allotment.student.add(student)
                    allotment.save()
                    ccount += 1
                else:
                    ccount = 0
                    break
                ClassAllotments.objects.filter(classroom=classroom, exam__date=abab, exam__start_time=ababc).update(status=1)
        return redirect('/classallotment_view')
    except ClassAllotments.DoesNotExist:
        return render(request, 'classallotment_view.html', {'g': True})
    


def view_seat(request):
    c = Allot.objects.all()
    
    # for i in c:
    #     print(i.student.regno)
    # print(c)
    # c = c.distinct()
    sid=request.user.id
    # print(sid)
    ab = Register.objects.get(id=sid)
    a = Allot.objects.filter(student=ab)
    # for i in c:
        # print(i.row)
    search = request.GET.get('search','')
    if search:
        c = c.filter(Q(exam__examname__icontains=search)|Q(exam__subject__name__icontains=search)|Q(exam__department__departmentname__icontains=search)|Q(student__username__icontains=search)|Q(classroom__classroom__classname__icontains=search))
        print(c)
    
    return render(request,'seat_arrangement.html',{'a':a,'c':c})

