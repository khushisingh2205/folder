# from django.shortcuts import render
# import mysql.connector as sql
# ten=''
# em=''
# fin=''
# pwd=''
# a1=''
# a2=''
# a3=''
# a4=''
# sn=''
# tn=''
# fon=''

# # Create your views here.
# def signaction(request):
#     global ten,em,fin,pwd,a2,a2,a3,a4,sn,tn,fon
#     if request.method=="POST":
#         m=sql.connect(host="localhost",user="root",passwd="admin123",database='website')
#         cursor=m.cursor()
#         d=request.POST
#         for key,value in d.items():
#             if key=="tenement_no":
#                 ten=value
#             if key=="first_name":
#                 fin=value
#             if key=="aadhar1":
#                 a1=value
#             if key=="second_name":
#                 sn=value
#             if key=="aadhar2":
#                 a2=value
#             if key=="third_name":
#                 tn=value
#             if key=="aadhar3":
#                 a3=value
#             if key=="fourt_name":
#                 fon=value
#             if key=="aadhar4":
#                 a4=value
#             if key=="email":
#                 em=value
#             if key=="password":
#                 pwd=value            
            

        
#         c = "INSERT INTO users VALUES({},'{}',{},'{}',{},'{}',{},'{}',{},'{}','{}')".format(ten,fin, a1, sn, a2, tn, a3, fon, a4, em, pwd)

#         cursor.execute(c)
#         m.commit()

#     return render(request,'signup_page.html')



from django.shortcuts import render
import mysql.connector as sql
ti=''
n=''
em=''
pn=''
pwd=''
# Create your views here.
def signaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="admin123",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="tenement_id":
                ti=value
            if key=="name":
                n=value
            if key=="email":
                em=value
            if key=="phone_number":
                pn=value
            if key=="password":
                pwd=value
        
        c="insert into users Values('{}','{}','{}','{}','{}')".format(ti,n,em,pn,pwd)
        cursor.execute(c)
        m.commit()

    return render(request,'signup_page.html')

# from django.shortcuts import render
# import mysql.connector as sql

# # Create your views here.
# def signaction(request):
#     if request.method == "POST":
#         ti = request.POST.get("tenement_id")
#         n = request.POST.get("name")
#         em = request.POST.get("email")
#         pn = request.POST.get("phone_number")
#         pwd = request.POST.get("password")

#         # Ensure that the 'phone_number' value is an integer
#         try:
#             pn = int(pn)
#         except ValueError:
#             # Handle the case where 'phone_number' is not a valid integer
#             # You can raise an error, display a message, or handle it as needed

#         try:
#             # Connect to the database
#             m = sql.connect(host="localhost", user="root", passwd="admin123", database="website")

#             # Use parameterized queries to avoid SQL injection
#             c = "INSERT INTO users (tenement_id, name, email, phone_number, password) VALUES (%s, %s, %s, %s, %s)"
#             values = (ti, n, em, pn, pwd)

#             cursor = m.cursor()
#             cursor.execute(c, values)
#             m.commit()
#         except sql.Error as e:
#             # Handle the database error and provide a user-friendly error message
#             error_message = "An error occurred while saving your data. Please try again later."
#             # You can log the actual error for debugging purposes if needed
#             print(f"Database error: {e}")
#         finally:
#             cursor.close()
#             m.close()

#     return render(request, 'signup_page.html')


