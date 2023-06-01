import mysql.connector
from mysql.connector import Error
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import maskpass


import time,os
# def clearscr():
#     time.sleep(1)
    
#     try:
#         os.system("clear")
#     except:
#         os.system("cls")
database=input("Enter Database Name : ")
passwd=maskpass.askpass(mask="*")

try:

    connect=mysql.connector.connect(host="localhost",user="root",password=passwd,db=database)
except:
    connect=mysql.connector.connect(host="localhost",user="dbuser",password=passwd,db=database)
c=connect.cursor()




# create user info table

try:
    sql="""create table if not exists  MRUsers(u_id int auto_increment,
    u_name varchar(30) not null,
    u_email varchar(50) not null ,
    u_contact bigint not null,
    u_pass varchar(20),
    primary key(u_id))
    """

    c.execute(sql)
    # print("Table Created")
    connect.commit()
except Error as e:
    print("Error : ",e )





#create movie review admin data table

try:
    sql="""create table if not exists MRAdmin(a_id int auto_increment,
    a_name varchar(30) not null,
    a_email varchar(50) not null ,
    a_contact bigint not null,
    a_pass varchar(20),
    primary key(a_id))
    """

    c.execute(sql)
    connect.commit()
    # print("Admin Table for Movie review Created .")
except Error as e:
    print("Error : ",e)



# create movie info table

try:
    sql="""create table if not exists MoviesTable(movie_id int auto_increment,
    movie_name varchar(60) not null,
    movie_genre varchar(100) not null,
    movie_cast varchar(100) not null,
    movie_year date not null,
    movie_director varchar(50),
    movie_runtime smallint ,
    movie_language varchar(20) not null,
    movie_country varchar(28) not null,
    movie_plotsummary text,
    movie_boxoffice bigint , 
    primary key(movie_id)) 
    """
    c.execute(sql)
    connect.commit()
    # print("Movies Table Created")
except Error as e:
    print("Error : ",e)





# Create Table for MovieReview

try:
    sql="""create table if not exists MovieReview(review_id int auto_increment,
    movie_name varchar(50) not null,
    u_name varchar(30) not null,
    u_email varchar(50) not null,
    review_comment text,
    review_rating tinyint(2) not null,
    review_time date not null,
    primary key(review_id))
    """
    c.execute(sql)
    connect.commit()
    print("Establishing Connection .....")
    # clearscr()
    print("Connected.".center(40))
except Error as e:
    print("Error : ",e)





# insert user data 

def Insert_user(insert):
    try:

        c=connect.cursor()
        sql="insert into  MRUsers(u_name,u_email,u_contact,u_pass) values(%s,%s,%s,%s)"
        data=(insert.u_name,insert.u_email,insert.u_contact,insert.u_pass)
        c.execute(sql,data)
        connect.commit()
        c.close()
        
        # print("User Added")
    except Error as e:
        print("Error : ",e)


def verify_user(email,password):
    sql=f"select u_email,u_pass from  MRUsers where u_email='{email}'"
    c.execute(sql)
    data=c.fetchone()
    if data:
        verify_pass=data[1]
        if verify_pass==password:

            return True
        else:
            return "\nInvalid Password "
    else:
        return "\nEmail Does Not Exists"



# fetch User Name

def fetchName(email):
    
    sql=f"select u_name from  MRUsers where u_email = '{email}'" 
    c.execute(sql)
    name=c.fetchone()
    return name[0]





# Return user data

def Show_User():
    try:
        sql="select u_id,u_name,u_email,u_contact from  MRUsers"
        c.execute(sql)
        user=c.fetchall()
        # df=pd.DataFrame(user,columns=["ID","User Name","User Email","Contact Number"])
        # pd.set_option("display.colheader_justify","center")
        # pd.set_option("display.width",None)
        table=PrettyTable()
        table.field_names=["ID","User Name","User Email ID","Contact Number"]
        for i in user:
            table.add_row([i[0],i[1],i[2],i[3]])
        print( table)

    except Error as e:
        print("Error : ",e)





# insert admin data

def insert_admin(admin):
    try:
        sql="insert into MRAdmin(a_name,a_email,a_contact,a_pass) values(%s,%s,%s,%s)"
        data=(admin.a_name,admin.a_email,admin.a_contact,admin.a_pass)
        c.execute(sql,data)
        print(f"Admin {admin.a_name} registered succesfully.")
        connect.commit()
    except Error as e:
        print("Error : ",e)






# insert movie  names data
#  
def insert_movie(movies):
    try:
        sql="insert into MoviesTable(movie_name,movie_genre,movie_cast,movie_year,movie_director,movie_runtime,movie_language,movie_country,movie_plotsummary,movie_boxoffice) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        data=(movies.movie_name,movies.movie_genre,movies.movie_cast,movies.movie_year,movies.movie_director,movies.movie_runtime,movies.movie_language,movies.movie_country,movies.movie_plotsummary,movies.movie_boxoffice)
        c.execute(sql,data)
        connect.commit()
        print(f"\nMovie {movies.movie_name} added Succsfully\n")
    except Error as e:
        print("Error : ",e)
    





# Delete  MRUsers From User Table


def DelUser(id):
    try:
        sql="delete from  MRUsers where u_id =%s"
        c.execute(sql,(id,))
        connect.commit()
    except Error as e:
        print("Error : ",e)





# Show Movies Table 

def ShowMovie():
    sql="select movie_id,movie_name,movie_cast,movie_genre,movie_year from MoviesTable "
    c.execute(sql)
    data=c.fetchall()
    table=PrettyTable()
    table.field_names=["Id","Movie Name","Movie Cast","Genre","Release Date"]
    for i in data:
        table.add_row([i[0],i[1],i[2],i[3],i[4]])
    return table

 



# Show Only Ten Movies

def ShowMovieUser():
    sql="select movie_id,movie_name,movie_cast,movie_genre,movie_year from MoviesTable limit 10"
    c.execute(sql)
    data=c.fetchall()
    table=PrettyTable()
    
    table.field_names=["Id","Movie Name","Movie Cast","Genre","Release Date"]
    for i in data:
        table.add_row([i[0],i[1],i[2],i[3],i[4]])
    return table

# print(ShowMovieUser(),ShowMovie())

     


    


# Search Movies With Respective Data
def SearchMovie(keyword,choice):
    if choice==0:
        sql="select * from MoviesTable where movie_id=%s"
        c.execute(sql,(keyword,))
        data=c.fetchone()
        
        if data:
            return "*"*140+f"""\nMovie ID-{data[0]}\n\nMovie Name - {data[1]}\t\t\t\t\t               Genre - {data[2]}\n\nCast - {data[3]}\t\t\t\tRelease Date - {data[4].strftime('%d-%m-%Y')}\n\nPlot Summary - {data[9]}\n\nDirector - {data[5]} \t\t\t\t\t\t\t\tRuntime - {"--" if data[6] is None else data[6]}\n\nLanguage - {data[7]}\n\nCountry - {data[8]}\n\nBox Office Collection in INR - {data[10]}\n"""+"*"*140
        else:
            return f"\nMovie ID -{keyword} Not Avaliable in Database. "
    elif choice==1:
        sql="select * from MoviesTable where movie_name like %s"
        c.execute(sql,(keyword,))
        data=c.fetchall()
        
        if len(data)==1:
            data=data[0]
            return "*"*140+f"""\nMovie ID-{data[0]}\n\nMovie Name - {data[1]}\t\t\t\t\t               Genre - {data[2]}\n\nCast - {data[3]}\t\t\t\tRelease Date - {data[4].strftime('%d-%m-%Y')}\n\nPlot Summary - {data[9]}\n\nDirector - {data[5]} \t\t\t\t\t\t\t\tRuntime - {"--" if data[6] is None else data[6]}\n\nLanguage - {data[7]}\n\nCountry - {data[8]}\n\nBox Office Collection in INR - {data[10]}\n"""+"*"*140
        elif len(data)>1:
            table=PrettyTable()
            table.field_names=["ID","Movie Name","Genre","Cast","Released Date","Country"]
            for i in data:
                table.add_row([i[0],i[1],i[2],i[3],i[4],i[8]])
            return table
        else:
            return f"\nMovie {keyword} Not Avaliable in Database. "
    elif choice==2:
        sql="select * from MoviesTable where year(movie_year) = %s"
    elif choice==3:
        sql="select * from MoviesTable where movie_genre like %s"
    elif choice==4:
        sql="select * from MoviesTable where movie_language = %s"
    elif choice==5:
        sql="select * from MoviesTable where movie_country = %s"
    elif choice==6:
        sql="select * from MoviesTable where movie_cast like %s"
    
    c.execute(sql,(keyword,))
    data=c.fetchall()
    
    if data :
        table=PrettyTable()
        table.field_names=["ID","Movie Name","Genre","Cast","Released Date","Country"]
        for i in data:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[8]])
        return table

        
    else:
        return "\n********Movies are Currently Unavailable.*********"    







# Delete Movies

def DeleteMovie(movie_id):
    try:
        sql="delete from MoviesTable where movie_id = %s"
        c.execute(sql,(movie_id,))
        connect.commit()
    except Error as e:
        print("Error : ",e)




# Insert Reviews By  MRUsers

def insertReview(review):
    try:
        sql="insert into MovieReview(movie_name,u_name,u_email,review_comment,review_rating,review_time) values(%s,%s,%s,%s,%s,%s)"
        c.execute(sql,(review.movie_name,review.u_name,review.u_email,review.review_comment,review.review_rating,review.review_time))
        print(f"Review Added Successfully for {review.movie_name}.")
        connect.commit()
        
    except Error as e :
        print("Error : ",e)





# ####################Show Reviews with Name ;###

def ShowReview(mov_name):
    sql="select review_id,review_comment,review_rating,u_name from MovieReview where movie_name=%s"
    c.execute(sql,(mov_name,))
    rows=c.fetchall()
    # print(rows)
    if rows is not None and rows:
        table=PrettyTable()
        table.field_names=["ID","Reviewer","Comments","Ratings"]

        for i in rows:
            table.add_row([i[0],i[3],"--" if i[1] is None else i[1],i[2]])
        return table
    else:
        return False
    



# Show Review to User

def ShowReviewUser(mov_name):
    sql="select movie_name,review_comment,review_rating,u_name,review_time from MovieReview where movie_name=%s"
    c.execute(sql,(mov_name,))
    rows=c.fetchall()
    # print(rows)
    if rows is not None and rows:
        table=PrettyTable()
        table.field_names=["Reviewer","Comments","Ratings","Uploaded"]

        for i in rows:
            table.add_row([i[3],"--" if i[1] is None else i[1],i[2],i[4]])
        return table
    else:
        return False


# print(ShowReview("1917"))


# Show Ratings to the User

              
def ShowRatingUser(mov_name):
    sql="select avg(review_rating) from MovieReview where movie_name=%s"
    c.execute(sql,(mov_name,))
    data=c.fetchone()
    for i in data:
        if i is not None:
            return f"\nMovie Name: {mov_name} \n\nMovie Rating: {round(data[0],2)}"
        else:
            return False





# Edit MovieDetails 

def EditMovie(id,field,new,name):
    
    try:
        
        sql=f"update MoviesTable set {field}='{new}' where movie_id='{id}'"
        c.execute(sql)
        connect.commit()
        print(f"Movie {name} Updated in the Table")
    
    except Error as e:

        print("Error : ",e)






# Deleling Review By Review Id:----

def DelReview(id):
    try:
        sql=f"delete from MovieReview where review_id ='{id}'"
        c.execute(sql)
        connect.commit()
        print(f"Review Id - {id} has been deleted")
    except Error as e:
        print("Error : ",e)





# Show Reviews to Logged in  MRUsers just of that User

def ShowOnlyUserReview(u_name):
    sql=f"select review_id,movie_name,review_comment,review_rating from MovieReview where u_email='{u_name}'"
    c.execute(sql)
    data=c.fetchall()
    if data:
        table=PrettyTable()
        table.field_names=["ID","Movie Name","Comments","Ratings"]
        for i in data:
            table.add_row([i[0],i[1],i[2],i[3]])
        return table
    else:
        return f"\nUser {u_name} has made no reviews."
    





# SUb Function for Edit And Delete By  MRUsers Login

def checkUserReview(email):
    sql=f"select review_id from MovieReview where u_email='{email}'"
    c.execute(sql)
    
    userids=c.fetchall()
    if userids:
        return userids
    else:
        return False




# # delete User Reviews

def DelUserReview(email,id):
    
    userids=checkUserReview(email)
    if userids==False:
        return f"\nReview not available for {email} "
    else:
        if (id,) in userids:
            sql=f"delete from MovieReview where review_id='{id}'"
            c.execute(sql)
            connect.commit()
            return f"\nReview Id - {id} for User - {email} has been deleted."

        else:
            
            return f"\nReview Id {id} Not exists for {email}"






# edit User Reviews

def EdirUserReview(email,id):
    userids=checkUserReview(email)
    if userids==False:
        return f"\nReviews Not Available for User - {email}"
    else:
        if (id,) in userids:
            ch=input("\nChoose What To Update :\n1.Comment.\n2.Rating.   \n:=")
            if ch=="1":
                newdata=input("\nEnter New Comment : ")
                boolyn=input(f"\nAre you sure you want to Edit review_id - {id} (y or n) : " )
                if boolyn=="y":
                    
                    sql=f"update MovieReview set review_comment='{newdata}' where review_id='{id}'"

                    c.execute(sql)
                    connect.commit()
                    return f"\nReview Comment Updated for {id} "
                elif boolyn=="n":
                    return "\nAction Teminated"
                else:
                   return "\nInvalid Choice !"


                
            elif ch=="2":
                newdata=input("\nEnter New Rating : ")
                boolyn=input(f"\nAre you sure you want to Edit review_id - {id} (y or n) : " )
                if boolyn=="y":
                    sql=f"update MovieReview set review_rating='{newdata}' where review_id='{id}'"

                    c.execute(sql)
                    connect.commit()
                    return f"\nReview Rating Updated for Id - {id} "
                elif boolyn=="n":
                    return "\nAction Teminated"
                else:
                   return "\nInvalid Choice !"

            else:
                return "\nInvalid Choice"
        else:
            
            return f"\nReview Id {id} Not exists for {email}"    
        





# Show Top Rated Movies

def ShowTopRatedMovies():
    sql="""select m.movie_id,m.movie_name,avg(r.review_rating) from MoviesTable as m join MovieReview as r on m.movie_name =r.movie_name group by m.movie_id order by avg(r.review_rating) desc limit 10
    """
    c.execute(sql)
    data=c.fetchall()
    if data:
        table=PrettyTable()
        table.field_names=["ID","Movie Name","Average Rating"]
        for i in data:
            table.add_row([i[0],i[1],round(i[2],2)])
        return table
    else:
        return"No Ratings Currently Availables"





# show Upcoming Movies 

def ShowUpcomingMovies():
    sql="SELECT * FROM MoviesTable WHERE movie_year > now() order by movie_year asc"
    c.execute(sql)
    data=c.fetchall()
    if data :
        table=PrettyTable()
        table.field_names=["ID","Movie Name","Genre","Cast","Released Date"]

        for i in data:
            table.add_row([i[0],i[1],i[2],i[3],i[4]])
        return table
    else:
        return "\nNo Upcoming Movies in Database."

# print(ShowUpcomingMovies())



# Create SearchLog Table ...

try:
    sql="create table if not exists SearchLog(search_id int auto_increment primary key,movie_id int not null,foreign key (movie_id) references MoviesTable(movie_id))"
    c.execute(sql)
    connect.commit()

except Error as e:
    print("Error : ",e)





# Add to Search Log 

def InsertSearchLog(movie_id):
    try:
        sql="insert into SearchLog(movie_id) values(%s)"
        c.execute(sql,(movie_id,))
        connect.commit()

    except Error as e:
        print("Error : ",e)





# Most Searched Movie

def MostSearchedMovie():
    sql="select m.movie_id,m.movie_name,m.movie_cast,m.movie_genre,m.movie_year , count(s.movie_id)as scount from MoviesTable as m join SearchLog as s on m.movie_id=s.movie_id group by m.movie_id order by scount desc limit 10"
    c.execute(sql)
    data=c.fetchall()
    if data:
        table=PrettyTable()
        table.field_names=["ID","Movie Name","Movie Cast","Movie Genre","Released Date"]
        for i in data:
            
            table.add_row([i[0],i[1],i[2],i[3],i[4]])
        print(table)
    else:
        print("\nMovies Not Available.!")




# Display Data Visualization with matplotlib
# import 
def DisplayPie():
    print("\nPie Chart On Different Window .")
    sql="select m.movie_id,m.movie_name,avg(r.review_rating) from MoviesTable as m join MovieReview as r on m.movie_name =r.movie_name group by m.movie_id order by avg(r.review_rating) desc limit 5"
    c.execute(sql)
    data=c.fetchall()
    plt.title("\nMost Rated Movies")

    values=[ float(i[2]) for i in data]

    names=[f"{i[0]}.{i[1]}" for i in data]

    plt.pie(values,labels=names,startangle=0,autopct='%1.1f%%')
    plt.show()

    
#################################################################################################################################
#################################################################################################################################

############################    Verification Section            #################################################################

#################################################################################################################################


# 

def check_movie_id(id):
    sql="select movie_name from MoviesTable where movie_id = %s"
    c.execute(sql,(id,))
    ids=c.fetchone()
    if ids :
        return ids[0]
    else:
        return False
    




# check if Contact Already Exists

def check_contact(contact,choice):
    if choice==0:
        sql="select u_contact from  MRUsers where u_contact=%s"
    if choice==1:
        sql="select a_contact from MRAdmin where a_contact=%s"
    c.execute(sql,(contact,))
    contactdata=c.fetchone()
    if contactdata:
        return True
    else:
        return False






# Check if the Email Exists int the Database

def check_email(email,choice):
    if choice==0:
        sql="select u_email from  MRUsers where u_email =%s"
    if choice==1:
        sql="select a_email from MRAdmin where a_email =%s"
    c.execute(sql,(email,))
    data=c.fetchone()
    
    if data:
        return True
    else:
        return False



    


# ANother User Login 

def verify_user(email,password):
    sql=f"select u_email,u_pass from  MRUsers where u_email='{email}'"
    c.execute(sql)
    data=c.fetchone()
    if data:
        verify_pass=data[1]
        if verify_pass==password:

            return True
        else:
            return "\nInvalid Password "
    else:
        return "\nEmail Does Not Exists"






# Verify If ADmin Email and PAssword Match

def verify_admin(email,password):
    sql="select a_email,a_pass from MRAdmin where a_email=%s and a_pass=%s"
    c.execute(sql,(email,password))
    data=c.fetchone()
    if data:
        return True
    else:
        if check_email(email,choice=1):
            return False

        else:
            return "Email Does Not Exists."    






# check if movie exists in the table

def check_movie(rmovie_name):
    rmovie_name=rmovie_name.capitalize()
    sql="select movie_name from MoviesTable where movie_name = %s"
    c.execute(sql,(rmovie_name,))
    data=c.fetchone()
    if data:
        return True
    else:
        return False  






# check if review is available for the movie

def check_review(movie):
    movie=movie.capitalize()
    sql="select movie_name from MovieReview where movie_name=%s"
    c.execute(sql,(movie,))
    data=c.fetchone()
    if data :
        return True
    else:
        return False





# check review id

def check_review_id(id):
    sql=f"select u_name from MovieReview where review_id = '{id}'"
    c.execute(sql)
    data=c.fetchone()
    if data is not None:
        return data[0]
    else:
        return False
    




# Cehck User Id for delfunction for Admin.

def check_user(user):
    sql="select u_name from  MRUsers where u_id=%s"
    c.execute(sql,(user,))
    u=c.fetchone()
    if u :
        return u[0]
    else:
        return False
    




# Check Movie Id if available....

def check_Movie_id(id):
    sql=f"select movie_name from MoviesTable where movie_id='{id}'"
    c.execute(sql)
    data=c.fetchone()
    if data:
        return data[0]
    else:
        return False




def insertintoAdmin():
    sql="insert into MRAdmin(a_name,a_email,a_contact,a_pass) values('Prajwal Surve','praju@gmail.com','9146346867','password')"
    c.execute(sql)
    connect.commit() 
def insertintoSearchLog():
    sql="insert into searchlog (movie_id) values(3),(3),(3),(3),(5),(5),(5),(1),(1),(10),(3),(1),(10),(11)"
    c.execute(sql)
    connect.commit()
def insertintoMoviesTable():
    sql="""insert into moviestable(movie_name,movie_genre,movie_cast,movie_year,movie_director,movie_runtime,movie_language,movie_country,movie_plotsummary,movie_boxoffice) values( 'Heropanti', 'Comedy,Action,Romance', 'Tiger Shroff,Kriti Sanon,Prakash Raj',"2014-5-23", 'Sabbir Khan', 146, 'Hindi', 'India', "When Renu elopes with her lover, her father, Chowdhary, kidnaps Bablu, who knows Renu's whereabouts, along with two of his friends. But Bablu falls in love with Dimpy, Chowdhary's younger daughter.", 250000000), ( 'Student of the year', 'Romance,Sports,Comedy', 'Varun Dhawan,Sidharth Malhotra,Alia Bhatt,Rishi Kapoor', '2012-10-19', 'Karan Johar', 146, 'Hindi', 'India', "Abhimanyu and Rohan are good friends. However, their friendship is affected after they compete to win a title and Abhimanyu falls in love with Shanaya, Rohan's girlfriend.", 560000000), ('Fast X', 'Action,Adventure', 'Vin Diesel,Jason Mamoa,Alan Ritchson', "2023-05-19", 'Louis Leterrier', 141, 'English', 'USA', "Over many missions and against impossible odds, Dom Toretto and his family have outsmarted and outdriven every foe in their path. Now, they must confront the most lethal opponent they've ever faced. Fueled by revenge, a terrifying threat emerges from the shadows of the past to shatter Dom's world and destroy everything -- and everyone -- he loves.", 99406560000), ( 'Brahmastra', 'Action,Fantasy', 'Ranbir Kapoor,Shah Rukh Khan,Alia Bhatt', "2022-09-09", 'Ayan Mukerji', 167, 'Hindi', 'India', 'Shiva and Isha, a young couple, learn about the secrets of the Brahmastra. Together, they must stop the forces of evil from destroying the universe.', 4310000000), ( 'Shamshera', 'Action,Adventure', 'Ranbir Kapoor,Sanjay Dutt,Vaani Kapoor',"2022-07-22", 'Karan Malhotra', 159, 'Hindi', 'India', 'In an attempt to save his tribe, Shamshera is killed by Shudh Singh and termed a traitor. Years later, his son decides to take revenge and reunite his tribe.', 1444000000), ( 'Tu Jhoothi Main Makkaar', 'Romance,Comedy', 'Ranbir Kapoor,Shraddha Kapoor',"2023-03-08", 'Luv Ranjan', 165, 'Hindi', 'India', 'To earn extra cash, Mickey helps couples break up. However, life gets complicated when he falls for Tinni, a career woman with an independent streak.', 1444000000), ( 'Ved', 'Romance,Drama', "Ritesh Deshmukh,Genelia D'Souza,Salman Khan", "2022-12-30", 'Riteish Deshmukh', 148, 'Marathi', 'India', 'Satya lives in a railway colony who dreams of playing for the railway cricket team and eventually representing Team India. Soon he falls madly in love with Nisha. However, Satya`s life takes a drastic change when a local Politician Bhaskar creates havoc in his personal and professional life. 12 Years Later, Satya is a drunk miserable man hopelessly waiting for his love. He is married to Shravani who has been crazily in love with Satya since her childhood. Who`s love has more madness - Satya or Shravani?', 750000000), ( 'Shehzada', 'Action,Drama', 'Kartik Aaryan,Kriti Sanon', "2023-02-17", 'Rohit Dhawan', 145, 'Hindi', 'India', 'The life of the nonchalant Bantu is turned upside down when he discovers that a dastardly father switched him at birth and he is actually the heir to a billionaire.', 474300000), ( 'Freddy', 'Psychological,Thriller', 'Kartik Aaryan,Alaya F',"2022-12-02", 'Shashanka Ghosh', 124, 'Hindi', 'India', 'After falling in love with a woman in an abusive marriage, a socially awkward dentist goes to great lengths to win her affection. However, hidden secrets set him off on a dark path.', 3450000000), ( 'Satyaprem Ki Katha', 'Drama,Romance', 'Kartik Aaryan,Kiara Advani',"2023-06-29", 'Satyaprem Ki Katha', Null, 'Hindi', 'India', 'Satyaprem Ki Katha is an upcoming Indian Hindi-language musical romantic drama film directed by Sameer Vidwans. Jointly produced by Nadiadwala Grandson Entertainment and Namah Pictures, it stars Kartik Aaryan and Kiara Advani. The film was announced in June 2021.', Null), ( 'Yodha', 'Action,Thriller', 'Sidharth Malhotra,Rashi Khanna,Disha Patani',"2023-09-15", 'Pushkar Ojha', Null, 'Hindi', 'India', 'Yodha is an upcoming Hindi language action thriller film directed by Sagar Ambre and Pushkar Ojha. Produced by Karan Johar under Dharma Productions, The film stars Sidharth Malhotra, Disha Patani and Raashii Khanna. Yodha is scheduled for theatrical release on 15 September 2023.', Null), ('Spider Man Across The Spider Verse', 'Action,Adventure', 'Hailee Steinfeld,Oscar Isaac',"2023-06-02", 'Joaquim Dos Santos', Null, 'English', 'USA', "After reuniting with Gwen Stacy, Brooklyn's full-time, friendly neighborhood Spider-Man is catapulted across the Multiverse, where he encounters a team of Spider-People charged with protecting its very existence.", Null), ('Transformers Rise of the Beasts', 'Action,Adventur', 'Anthony Ramos,Pete Davidson,Lisa Koshy', "2023-06-09", 'Steven Caple Jr.', 127, 'English', 'USA', 'During the 1990s, the Maximals, Predacons and Terrorcons join the existing battle on Earth between Autobots and Decepticons.', Null), ( 'The Flash', 'Action,Adventure', 'Ezra Miller,Ben Affleck,Sasha Calle,Kiersey Clemons', "2023-06-16", 'Andrés Muschietti', 144, 'English', 'USA', "Worlds collide when the Flash uses his superpowers to travel back in time to change the events of the past. However, when his attempt to save his family inadvertently alters the future, he becomes trapped in a reality in which General Zod has returned, threatening annihilation. With no other superheroes to turn to, the Flash looks to coax a very different Batman out of retirement and rescue an imprisoned Kryptonian -- albeit not the one he's looking for.", Null), ( 'Adipurush', 'Drama,Fantasy', 'Prabhas,Kriti Sanon,Sunny Singh,Saif Ali Khan', "2023-06-16", 'Om Raut', 174, 'Hindi', 'India', 'Adipurush is an upcoming Indian Hindu mythological film based on the Hindu epic Ramayana. The film is written and directed by Om Raut and produced by T-Series and Retrophiles. Shot simultaneously in Hindi and Telugu languages, the film stars Prabhas, Kriti Sanon, Saif Ali Khan, Sunny Singh and Devdatta Nage.', Null), ( 'Bloody Daddy', 'Thriller,Action', 'Shahid Kapoor,Diana Penty,Sanjay Kapoor', "2023-06-09", 'Ali Abbas Zafar', Null, 'Hindi', 'India', 'Bloody Daddy is an upcoming Indian Hindi-language action thriller film directed by Ali Abbas Zafar who co-wrote the film with Aditya Basu and Siddharth–Garima, and produced by Jio Studios. It features Shahid Kapoor, Sanjay Kapoor, Diana Penty.', Null), ( 'Mission Impossible Dead Reckoning Part One', 'Action,Adventure', 'Tom Cruise,Hayley Atwell,Vanessa Kirby',"2023-07-12", 'Christopher McQuarrie', Null, 'English', 'USA', 'Ethan Hunt and the IMF team must track down a terrifying new weapon that threatens all of humanity if it falls into the wrong hands. With control of the future and the fate of the world at stake, a deadly race around the globe begins.', Null), ( 'Spider Man Far From Home', 'Action,Adventure', 'Tom Holland,Zendaya,Jacob Batalon', "2021-12-17", 'Jon Watts', 148, 'English', 'USA', "Spider-Man seeks the help of Doctor Strange to forget his exposed secret identity as Peter Parker. However, Strange's spell goes horribly wrong, leading to unwanted guests entering their universe.", 158846938000), ( 'Heropanti 2', 'Action,Romance', 'Tiger Shroff,Tara Sutaria,Nawazuddin Siddiqui', "2022-04-29", 'Ahmed Khan', 150, 'Hindi', 'India', 'RJ enters the glamourous life of Inaaya and Laila, a notorious cyber-criminal. Action and trouble multiply tenfold when Inaaya believes RJ is her former lover.', 351300000), ( 'Edit Testing', 'Trail', 'Me', "2023-5-20", 'Prajwal', 1, 'English', 'India', 'Test ing Test ing', 0)"""
    c.execute(sql)
    connect.commit()
def insertintoMovieReview():
    sql="""insert into MovieReview(movie_name,u_name,u_email,review_comment,review_rating,review_time) values("Spider man Far From Home","Shivansh More","more@gmail.com","Amazing role of Peter Parker by Tom Holland",8,current_date()),("Shamshera","Pauras Jadhav","pauras@gmail.com","Despite a weak storyline and a weaker screenplay and dialogues, the actors deliver honest performances.",7,current_date()),("Shamshera","Kedar Pawar","kedar@gmail.com"," Shamshera is an intolerable and tedious period drama.",6,current_date()),("Freddy","Prajwal Surve","survepraju@gmail.com","Freddy is an engaging thriller indeed.",8,current_date()),("Freddy","Shubham Sawant","shubham@gmail.com","It is a romantic thriller packed with sharp twists and turns.",8,current_date()),("Freddy","Tinu","tinu@gmail.com","I loved the art style and careful, clever treatment of the film.",7,current_date()),("Brahmastra","Tinu","tinu@gmail.com","Totally disappointed. There's no special plot in the movie.",5,current_date()),("Brahmastra","Prajwal Surve","survepraju@gmail.com","Other than VFX, there is no storyline, no engaging screenplay and cringy dialogs.",6,current_date()),("Heropanti 2","Prajwal Surve","survepraju@gmail.com","Heropanti 2 is full of cringe moments, and believe me, they are unbearable.",6,current_date())"""
    c.execute(sql)
    connect.commit()
sql="select * from MRAdmin"
c.execute(sql)
x=c.fetchone()
if x==None:
    insertintoAdmin()
    insertintoMovieReview()
    insertintoMoviesTable()
    insertintoSearchLog()

    
    
    

