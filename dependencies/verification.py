# import mysql.connector

# from mysql.connector import Error
# try:

#     connect=mysql.connector.connect(host="localhost",user="root",password="carnal",db="Examples")
# except:
#     connect=mysql.connector.connect(host="localhost",user="dbuser",password="Squ@d123",db="BasicDB")
    
    
# c=connect.cursor()

# # Check Movie ID in Movie Table

# def check_movie_id(id):
#     sql="select movie_name from MoviesTable where movie_id = %s"
#     c.execute(sql,(id,))
#     ids=c.fetchone()
#     if ids :
#         return ids[0]
#     else:
#         return False
    


# # check if Contact Already Exists
# def check_contact(contact,choice):
#     if choice==0:
#         sql="select u_contact from Users where u_contact=%s"
#     if choice==1:
#         sql="select a_contact from MRAdmin where a_contact=%s"
#     c.execute(sql,(contact,))
#     contactdata=c.fetchone()
#     if contactdata:
#         return True
#     else:
#         return False



# # Check if the Email Exists int the Database
# def check_email(email,choice):
#     if choice==0:
#         sql="select u_email from Users where u_email =%s"
#     if choice==1:
#         sql="select a_email from MRAdmin where a_email =%s"
#     c.execute(sql,(email,))
#     data=c.fetchone()
    
#     if data:
#         return True
#     else:
#         return False


# # # Verif if  User  Email And Password MAtch
# # def verify_user(email,password):
# #     sql="select u_email,u_pass,u_name from Users where u_email=%s and u_pass=%s"
# #     c.execute(sql,(email,password))
# #     data=c.fetchone()
# #     if data is not None:
# #         return (True,data[2])
# #     else:
# #         validemail=check_email(email,choice=0)
# #         if validemail==False:
# #             return f"Email Id {email} is Not Registered,\nPlease Sign In First"
# #         else:
# #             return "Invalid Password"
    


# # ANother User Login 
# def verify_user(email,password):
#     sql=f"select u_email,u_pass from Users where u_email='{email}'"
#     c.execute(sql)
#     data=c.fetchone()
#     if data:
#         verify_pass=data[1]
#         if verify_pass==password:

#             return True
#         else:
#             return "\nInvalid Password "
#     else:
#         return "\nEmail Does Not Exists"


# # Verify If ADmin Email and PAssword Match
# def verify_admin(email,password):
#     sql="select a_email,a_pass from MRAdmin where a_email=%s and a_pass=%s"
#     c.execute(sql,(email,password))
#     data=c.fetchone()
#     if data:
#         return True
#     else:
#         if check_email(email,choice=1):
#             return False

#         else:
#             return "Email Does Not Exists."    

# # check if movie exists in the table
# def check_movie(rmovie_name):
#     rmovie_name=rmovie_name.capitalize()
#     sql="select movie_name from MoviesTable where movie_name = %s"
#     c.execute(sql,(rmovie_name,))
#     data=c.fetchone()
#     if data:
#         return True
#     else:
#         return False  

# # check if review is available for the movie
# def check_review(movie):
#     movie=movie.capitalize()
#     sql="select movie_name from MovieReview where movie_name=%s"
#     c.execute(sql,(movie,))
#     data=c.fetchone()
#     if data :
#         return True
#     else:
#         return False


# # check review id
# def check_review_id(id):
#     sql=f"select u_name from MovieReview where review_id = '{id}'"
#     c.execute(sql)
#     data=c.fetchone()
#     if data is not None:
#         return data[0]
#     else:
#         return False
    
# # x=check_review_id(5)
# # print(x)

# def check_user(user):
#     sql="select u_name from Users where u_id=%s"
#     c.execute(sql,(user,))
#     u=c.fetchone()
#     if u :
#         return u[0]
#     else:
#         return False
    


# # Check Movie Id if available....
# def check_Movie_id(id):
#     sql=f"select movie_name from MoviesTable where movie_id='{id}'"
#     c.execute(sql)
#     data=c.fetchone()
#     if data:
#         return data[0]
#     else:
#         return False


