from dependencies import validations as valid,verification as verify
from model import Users,Admin,MoviesTable,MovieReview
import database as db
import maskpass,time

projtitle="\n\n**************Movies Reviews **************".center(40)

# Application Start---

while True:
    print(projtitle)
    print("\n1.Show Movies.\n2.Login\n3.Sign Up.\n4.Exit.\n")

    ch=input("\nEnter Your Choice : ")
    
    if ch=="1":
        print("\n***************************** Movies ***********************************\n")
        # AS Trail 
        x=db.ShowMovieUser()
        print(x)
    elif ch =="2":
        while True:
            #db.clearscr()
            print(projtitle)
            print("\nLogin \n")
            print("\n1.Login as User\n2.Login as Admin.\n3.Back\n")
            ch=input("\nEnter Your Choice : ")
            if ch=="1":
                #db.clearscr()
                print(projtitle)
                print("\nLogin as User")
                login_status=False
                while True:
                    while True :
                        email=input("\nEnter Your Email : ")
                        if valid.EmailValidation(email):
                            break
                        else:
                            print("\nInvalid Email ! ,Try Again .")
                                
                    password=maskpass.askpass(mask="*")
                    x=db.verify_user(email,password)
                    if x==True:
                        u_name=db.fetchName(email)
                        print("\nLogging In .....")
                    #     #db.clearscr()       
                    #     print(projtitle)       
                        print(f"\nUser {email} Logged in succesfully")
                        login_status=True
                        break
                    else:
                        print(x)
                    #     #db.clearscr()
                        break
                        
                        

                    

                
                if login_status==True:
                    #db.clearscr()
                    print(projtitle)
                    print(f"\n********User {u_name}")
                    print("\nSelect From Below :")
                    while True:
                        
                        print("\n1.Top Rated Movies.\n2.Most Searched Movies.\n3.Upcoming Movies.\n4.Search Movie.\n5.View Reviews And Ratings.\n6.Add Reviews.\n7.Edit Review.\n8.Delete Review.\n9.Logout\n")
                        # print("\n1.Show Most Searched Movies \n2.Search Movie \n3.View Review.\n4.Add Reviews\n5.Top Rated Movies.\n6.Logout")
                        ch=input("\nEnter Your Choice :")

                        # Top Rated Movies
                        if ch =="1":
                            print(projtitle)
                            print("\nTop Rated Movies -")
                            dis=db.ShowTopRatedMovies()
                            print(dis)
                            db.DisplayPie()
                            while True:
                                garbage=input("\nPress Enter to Exit .")
                                break


                        # Most Searched Movies
                        elif ch =="2":
                            print(projtitle)
                            print("\nMost Searched Movies -\n")
                            db.MostSearchedMovie()
                            while True:
                                garbage=input("\nPress Enter to Go Back.\n")
                                break


                        # Upcoming Movies
                        elif ch=="3":
                            print(projtitle)
                            print("\nUpcoming Movies - \n")
                            dis=db.ShowUpcomingMovies()
                            print(dis)
                            while True:
                                garbage=input("\nPress Enter to Go Back.")
                                break



                        # Search MOvies --
                        elif ch =="4":
                            while True:
                                #db.clearscr()
                                print(projtitle)
                                print(f"\n****User {u_name}")
                                print("\n1.Search By ID.\n2.Search by Name.\n3.Search by Cast.\n4.Search by Year.\n5.Search by Genres.\n6.Search by Language.\n7.Search by Country.\n8.Exit")
                                ch=input("\nEnter Your Choice : ")
                                if ch=="1":
                                    idd=input("\nEnter Movie ID : ")
                                    x=db.check_Movie_id(idd)
                                    if x==False:
                                        print(f"\nMovie id - {idd} Not Available .")
                                    else:
                                        db.InsertSearchLog(idd)
                                        dis=db.SearchMovie(idd,choice=0)
                                        print(dis)
                                elif ch=="2":
                                    movie_name=input("\nEnter the Movie Name : ")
                                    # movie_name=movie_name.capitalize()
                                    movie_name="%"+movie_name+"%"
                                    
                                    dis=db.SearchMovie(movie_name,choice=1)
                                    print(dis)

                                elif ch=="3":
                                    movie_cast=input("\nEnter the Cast Name : ")
                                    movie_cast="%"+movie_cast+"%"

                                    x=db.SearchMovie(movie_cast,choice=6)
                                    print(x)

                                elif ch=="4":
                                    movie_year=input("\nEnter the Year :")
                                    if movie_year.isdigit():

                                        dis=db.SearchMovie(movie_year,choice=2)
                                        print(dis)
                                    else:
                                        print("\nInvalid Year !")

                                elif ch=="5":
                                    movie_genre=input("\nEnter the Genre of the Movie : ")
                                    wcm_genre="%"+movie_genre+"%"
                                    dis=db.SearchMovie(wcm_genre,choice=3)
                                    print(dis)



                                elif ch=="6":
                                    movie_lang=input("\nEnter the Movie Language to Search : ")

                                    dis=db.SearchMovie(movie_lang,choice=4)
                                    print(dis)


                                elif ch =="7":
                                    movie_org=input("\nEnter the Country Where Movie was Realeased from : ")
                                    dis=db.SearchMovie(movie_org,choice=5)
                                    print(dis)


                                elif ch=="8":
                                    #db.clearscr()
                                    
                                    break
                                else:
                                    print("\nInvalid Choice !")





                        # View Reviews and Ratings--
                        elif ch =="5":
                            
                            while True:
                                print(projtitle)
                                print("\n***View Reviews And Ratings :\n")
                                
                                print("\n1.View Reviews by Movie Name.\n2.View Rating by movie name.\n3.Back")
                                ch=input("\nEnter your Choice : ")
                                #db.clearscr()
                                print(projtitle)

                                # SHow Movie Review To USers
                                if ch=="1":
                                    
                                    
                                    print("\nSearch Reviews by Movie Name \n")
                                    mov_name=input("\nEnter the Movie Name : ")
                                    mov_name=" ".join([word.capitalize() for word in mov_name.split()])
                                    x=db.ShowReviewUser(mov_name)
                                    if x!=False:
                                        print(x)
                                    else:
                                        print(f"\nMovie - {mov_name} has No Reviews. ")
                                    # if db.check_review(mov_name):
                                    #     db.ShowReview(mov_name)
                                        
                                    # else:
                                    #     print(f"{mov_name} has no review availabe.! Sorry for Inconvinence. ")
                                    while True:
                                        garbage=input("\nGO Back ? Press Any Key.")
                                        #db.clearscr()
                                        break


                                # Show Average Rating To USer
                                elif ch=="2":
                                    
                                    print("\nAverage Rating -\n")
                                    mov_name=input("\nEnter the Movie Name : ")
                                    mov_name=" ".join([word.capitalize() for word in mov_name.split()])
                                    # if db.check_review(mov_name):
                                    #     avg=db.ShowRating(mov_name)
                                    #     print(avg)
                                    # else:
                                    #     print(f"{mov_name} has no available ratings .")
                                    x=db.ShowRatingUser(mov_name)
                                    if x!=False:
                                        print(x)

                                    else:
                                        print(f"\nMovie {mov_name} has No Avialble Rating .")
                                    while True:
                                        garbage=input("\nGO Back ? Press Any Key.")
                                        #db.clearscr()
                                        break


                                elif ch=="3":
                                    #db.clearscr()
                                    break
                                else:
                                    print("Invalid Choice")

                            

                        # Add Reviews 

                        elif ch=="6":
                            
                            print(projtitle)
                            print("\n\nAdd Reviews ")

                            while True:
                                rmovie_name=input("\nEnter the Movie Name : ")
                                rmovie_name=rmovie_name.capitalize()
                                if db.check_movie(rmovie_name):
                                    pass
                                else:
                                    print(f"\nMovie -{rmovie_name} is not Available in the Database yet.\nTry Other Movie ?\n")
                                    break
                            #u_name
                            #u_email
                                review_comment=input(f"\nAdd Comment for {rmovie_name} : ")
                                if review_comment=="":
                                    review_comment=None
                                else:
                                    pass

                                while True:

                                    review_rating=int(input("\nRate the Movie (1-10) : "))
                                    if review_rating>=0 and review_rating<10:
                                        break
                                    else:
                                        print("\nRating Can't be Greater than 10 ")
                                review_time=time.strftime("%Y-%m-%d   %H:%M:%S")
                                review=MovieReview(movie_name=rmovie_name,u_name=u_name,u_email=email,review_comment=review_comment,review_rating=review_rating,review_time=review_time)
                                db.insertReview(review)
                                break


                        # Edit Reviews   
                        #  
                        elif ch=="7":
                            print(projtitle)
                            print("\n\n***Edit Review -")
                            print(f"\nReviews Made By {u_name}")
                            userreview=db.ShowOnlyUserReview(email)
                            print(userreview)
                            editid=int(input("\nEnter the id you want to Edit : "))
                            
                            x=db.EdirUserReview(id=editid,email=email)
                            print(x)
                            


                        # delete reviews
                        
                        elif ch=="8":
                            print(projtitle)
                            print("\n\n***Delete Review -" )
                            userreview=db.ShowOnlyUserReview(email)
                            print(userreview)
                                                

                            delid=int(input("\nEnter the Review Id You Want to delete : "))
                            boolyn=input(f"\nAre you sure you want to delete review_id - {delid} (y or n) : " )
                            if boolyn=="y":
                                x=db.DelUserReview(id=delid,email=email)
                                print(x)
                            elif boolyn=="n":
                                print("\nAction terminated .")
                            else:
                                print("\nInvalid Choice.!")
                    

                # Logged Out User ---
                        elif ch=="9":
                            print(f"\nUser {u_name} Logged out .")
                            login_status=False
                            break

                        else:
                            print("\nInvalid Choice ! Try Again .")
                else:
                    print("\nUser Login Unsuccesfull ! Try Again .")

                        
                        
            elif ch=="2":


                #db.clearscr()
                print(projtitle)
                print("\nLogin as Admin \n")

                login_status=False
                while True:
                    a_email=input("\nEnter your Email : ")
                    if valid.EmailValidation(a_email):
                        break
                    else:
                        print("\nInvalid Input ! Please Check your Email ")

                
                password=maskpass.askpass(mask="*")
                x=db.verify_admin(a_email,password)
                if x==True:
                    print(f"\nAdmin {a_email} has succesfully logged in")
                    #db.clearscr()
                    login_status=True
                elif x==False:
                    print("\nInvalid Password.")
                    
                else:
                    print(x)
                    
                if login_status==True:

                    while True :
                        print(projtitle)
                        print(" "*20+f"Admin {a_email} ")
                        print("\nSelect  From Below : \n")
                        print("""\n1.Show Users.\t\t\t\t\t\t\t\t\t2.Delete Users.\n3.Show Movies.\t\t\t\t\t\t\t\t\t4.Search Movies.\n5.Add Movies.\t\t\t\t\t\t\t\t\t6.Edit Movies.\n7.Delete Movies.\t\t\t\t\t\t\t\t8.Show Reviews.\n9.Delete Reviews.\t\t\t\t\t\t\t\t10.Exit.""")
                        ch=input("\nEnter Your Choice : ")
            # SHow Users            
                        if ch=="1":
                            #db.clearscr()
                            print("****Users****".center(50))
                            db.Show_User()
                            while True:
                                garbage=input("\nEnter any key to go back : ")
                                break
                            #db.clearscr()

            # Delete Users
                        elif ch =="2":
                            

                                selectid=input("\nEnter User ID of The User you want to delete : ")
                                x=db.check_user(selectid)
                                if x!=False:
                                    while True:

                                        yesorno=input("\nAre You Sure You Want to Delete it - y or n : ")
                                        if yesorno =="y":
                                            db.DelUser(selectid)
                                            print(f"\nUser id -{selectid} ,{x} has been deleted.")
                                            break
                                        elif yesorno=="n":
                                            print("\nAction Terminated")
                                            break
                                        else:
                                            print("\nInvalid Choice .")
                                else:
                                    print(f"\nUser Id - {selectid} Does Not Exists.")
            
            # Display All Movies  
            # Still Pending Not Efficients#################################################333#############################################

                        elif ch=="3":
                            print("\nAll Movies \n")
                            display=db.ShowMovie()
                            print(display)
                            while True:
                                garbage=input("\nEnter Any Key To GO BAck .")
                                break



            # Search Movies
                        elif ch=="4":
                            print("\n*******Search Movies********* ")
                            while True:
                                print("\n1.Search By ID.\n2.Search by Name.\n3.Search by Cast.\n4.Search by Year.\n5.Search by Genres.\n6.Search by Language.\n7.Search by Country.\n8.Exit")
                                ch=input("\nEnter Your Choice : ")
                                if ch=="1":
                                    mov_id=input("\nENter the Movie Id : ")
                                    x=db.SearchMovie(mov_id,choice=0)
                                    print(x)

                                elif ch=="2":
                                    movie_name=input("\nEnter the Movie Name : ")
                                    
                                    x=db.SearchMovie(movie_name,choice=1)
                                    print(x)

                                elif ch=="3":
                                    movie_cast=input("\nEnter the Cast Name : ")
                                    movie_cast="%"+movie_cast+"%"

                                    x=db.SearchMovie(movie_cast,choice=6)
                                    print(x)

                                elif ch=="4":
                                    movie_year=input("\nEnter the Year :")
                                    if movie_year.isdigit():

                                        x=db.SearchMovie(movie_year,choice=2)
                                        print(x)
                                    else:
                                        print("\nInvalid Year !")

                                elif ch=="5":
                                    movie_genre=input("\nEnter the Genre of the Movie : ")
                                    wcm_genre="%"+movie_genre+"%"
                                    x=db.SearchMovie(wcm_genre,choice=3)
                                    print(x)



                                elif ch=="6":
                                    movie_lang=input("\nEnter the Movie Language to Search : ")
                                    x=db.SearchMovie(movie_lang,choice=4)
                                    print(x)
                                elif ch =="7":
                                    movie_org=input("\nEnter the Country Where Movie was Realeased from : ")
                                    x=db.SearchMovie(movie_org,choice=5)
                                    print(x)
                                elif ch=="8":
                                    break
                                else:
                                    print("\nInvalid Choice !")

                        # Insert Movies

                        elif ch=="5":
                            #db.clearscr()
                            print(projtitle)
                            m_name=input("\nEnter Movie Name : ")
                            m_genre=input("\nEnter movie genres seperated by ',' : ")
                            m_cast=input("\nEnter Movie Cast sepearted by ',' : ")
                            m_year=input("\nEnter Movie released year - (YYYY-MM-DD): ")
                            m_director=input("\nEnter Movie Director : ")
                            m_runime=input("\nEnter Movie Runtime : ")
                            if m_runime=="":
                                m_runime=None
                            m_language=input("\nEnter Movie Original Language : ")
                            m_country=input("\nEnter Movies Origin Country : ")
                            m_plotsummary=input("\nEnter Movie Plot Summary : ")
                            if m_plotsummary=="":
                                m_plotsummary=None
                            m_boxoffice=input("\nEnter Movie Box Office Collection : ")
                            if m_boxoffice=="":
                                m_boxoffice=None
                            
                            movies=MoviesTable(m_name,m_genre,m_cast,m_year,m_director,m_runime,m_language,m_country,m_plotsummary,m_boxoffice)
                            db.insert_movie(movies)

                    # Edit Movies ------With out Yes or No Question
                        elif ch =="6":
                            #db.clearscr()
                            print(projtitle)
                            print("\nEdit Movie")
                            
                            
                            mov_id=input("\nEnter the Movie ID you want to edit :")
                            editname=db.check_Movie_id(mov_id)

                            if editname!=False:
                                while True:
                                
                                    choice=input(f"\nChoose What you want to Edit from {editname} :\n\n1.Cast\n2.Genre\n3.Release Date\n4.Back\n\nEnter your Choice : ")
                                    if choice=="1":
                                        newdata=input("Enter the updated Cast : ")
                                        db.EditMovie(id=mov_id,field="movie_cast",new=newdata,name=editname)
                                    elif choice=="2":
                                        newdata=input("Enter the updated Genre : ")
                                        db.EditMovie(id=mov_id,field="movie_genre",new=newdata,name=editname)
                                    elif choice=="3":
                                        newdata=input("Enter the updated Date -(YYYY-MM-DD) : ")
                                        db.EditMovie(id=mov_id,field="movie_year",new=newdata,name=editname)
                                    elif choice=="4":
                                        break
                                    else:
                                        print("I\nnvalid Choice !")
                            else:
                                print("\nMovie  ID is not available .")
                                
                            
                                

                    # Delete Movie with ID as input
                        elif ch=="7":
                            print("\nDelete Movie ")
                            while  True:
                                movie_id=input("\nEnter the Movie Id you want to delete : ")
                                x=db.check_Movie_id(movie_id)
                                if x!=False:
                                    boolyn=input(f"\nAre you Sure you want to delete movie id {movie_id} - (y or n): ")
                                    if boolyn=="y":
                                        db.DeleteMovie(movie_id)
                                        print(f"\nMovie id - {movie_id} ,{x} is deleted succesfully .\n")
                                        break
                                    elif boolyn=="n":
                                        print("\nAction Terminated ")
                                        break
                                    else:
                                        print("\nInvalid Input .!")
                                else:
                                    print(f"\nMovie Id - {movie_id} not available .")

                                
                    # View Reviewss

                        elif ch=="8":

                            print(projtitle)
                            print("\nView Review")
                            while True:                                
                                
                                print("\n1.View Reviews by Movie Name.\n2.View Rating by movie name.\n3.Back")
                                ch=input("\nEnter your Choice : ")
                                #db.clearscr()
                                

                                # SHow Movie Review To ADmin
                                if ch=="1":
                                    
                                    
                                    print("\nSearch Reviews by Movie Name \n")
                                    mov_name=input("\nEnter the Movie Name : ")
                                    mov_name=" ".join([word.capitalize() for word in mov_name.split()])
                                    x=db.ShowReview(mov_name)
                                    if x!=False:
                                        print(x)
                                    else:
                                        print(f"\nMovie - {mov_name} has No Reviews. ")
                                    # if db.check_review(mov_name):
                                    #     db.ShowReview(mov_name)
                                        
                                    # else:
                                    #     print(f"{mov_name} has no review availabe.! Sorry for Inconvinence. ")
                                    while True:
                                        garbage=input("\nGO Back ? Press Enter.")
                                        #db.clearscr()
                                        break


                                # Show Average Rating To USer
                                elif ch=="2":
                                    
                                    print("\nAverage Rating -\n")
                                    mov_name=input("\nEnter the Movie Name : ")
                                    mov_name=" ".join([word.capitalize() for word in mov_name.split()])
                                    # if db.check_review(mov_name):
                                    #     avg=db.ShowRating(mov_name)
                                    #     print(avg)
                                    # else:
                                    #     print(f"{mov_name} has no available ratings .")
                                    x=db.ShowRatingUser(mov_name)
                                    if x!=False:
                                        print(x)

                                    else:
                                        print(f"\nMovie {mov_name} has No Avialble Rating .")
                                    while True:
                                        garbage=input("GO Back ? Press Any Key.")
                                        #db.clearscr()
                                        break


                                elif ch=="3":
                                    # Go Back
                                    #db.clearscr()
                                    break
                                else:
                                    print("Invalid Choice")
                            

                    # Delete Reviewss

                        elif ch =="9":
                            delid=input("\nEnter the Review ID You want to Delete : ")
                            x=db.check_review_id(delid)
                            if x==False:
                                print(f"\nReview id - {delid} does not exists in database.")
                            else:
                               
                                yesorno=input(f"\nAre you sure you want to delete Review by {x} -(y or n) : ")
                                if yesorno=="y":
                                    db.DelReview(delid)
                                elif yesorno=="n":
                                    print("\nAction Terminated .")
                                    
                                else:
                                    print("\nInvalid Choice !")





                                
                        elif ch=="10":
                            login_status=False
                            break
                        else:
                            print("Invalid Choice !")
                else:
                    #db.clearscr()
                    print("Admin Login Unsuccesfull ! Try Again")    

            elif ch=="3":
                #db.clearscr()
                break
            else:
                print("Invalid Choice ! Try Again .")
###############
# Sign UP Options....
    elif ch =="3":

        while True:
            # #db.clearscr()
            print(projtitle)
            print("\nSign Up\n")
            print("\n1.Sign Up as User.\n2.Back.\n")
            ch=input("Enter Your Choice : ")
            if ch=="1":
                #db.clearscr()
                print("\nSign In As User.\n")

                while True:
                    u_name=input("\nEnter Your Name : ")
                    if valid.NameValidation(u_name):
                        break
                    else:
                        print("\nInvalid Name ")

                # Valid Email 
                while True:
                    u_email=input("\nEnter your Email : ")
                    if valid.EmailValidation(u_email):
                        if db.check_email(u_email,choice=0):
                            print("\nUser Already Exists Try Different Email !")
                        else:
                    
                            break
                    else:
                        print("\nInvalid Email !")
                # contaact Validation
                while True:
                    u_contact=input("\nEnter Your Contact : ")
                    if valid.ContactValidation(u_contact):
                        if db.check_contact(u_contact,choice=0):
                            print("\nContact Already Exists Try Different Number . ")
                        else:
                            break
                    else:
                        print("\nInvalid Contact Number ,Must be 10 digits and start with (6-9) !")

                while True:
                    while True:
                        u_pass=maskpass.askpass(mask="*",prompt="\nEnter Password : ")
                        check=valid.PasswordValidation(u_pass)
                        if check==True:
                            break
                        else:
                            print(check)
                        
                
                    u_pass2=maskpass.askpass(mask="*",prompt="\nConfirm Password : ")
                    if u_pass==u_pass2:
                        print(f"\nUser {u_name} has signed up Succesfully")
                        break
                    else:
                        print("\nPassword Does Not Match")
                insert=Users(u_name,u_email,u_contact,u_pass)
                #db.clearscr()
                db.Insert_user(insert)



            # elif ch=="2":
            #     #db.clearscr()
            #     print(projtitle)
            #     print("\nSign Up as Admin\n")
            #     # NAMe Validation
            #     while True:
            #         a_name=input("Enter Your Name : ")
            #         if valid.NameValidation(a_name):
            #             break
            #         else:
            #             print("Invalid Name, Check Your Format.")
            #     # VAlid Email ID 
            #     # And Check IF already Exists
            #     while True:
            #         a_email=input("Enter your Email : ")
            #         if valid.EmailValidation(a_email):
            #             if db.check_email(a_email,choice=1):
            #                 print("Email ALready Exists. Try Different Email ID.")
            #             else:
            #                 break
            #         else:
            #             print("Invalid Email ID.")

            #     # cOntacat Validation
            #     while True:
            #         a_contact=input("Enter Your Contact : ")
            #         if valid.ContactValidation(a_contact):
            #             if db.check_contact(a_contact,choice=1):
            #                 print("Contact Already Exists Try Different Number . ")
            #             else:
            #                 break
            #         else:
            #             print("Invalid Contact Number , Starts with (6-9) !")
            #     # Pass word Validation
            #     while True:
            #         while True:
            #             a_pass=maskpass.askpass(mask="*")
            #             check=valid.PasswordValidation(a_pass)
            #             if check==True:
            #                 break
            #             else:
            #                 print(check)
            #         a_pass2=maskpass.askpass(mask="*",prompt="Confirm Password: ")    
            #         if a_pass!=a_pass2:
            #             print("Password Does Not MAtch.")
            #         else:
            #             break

            #     admin=Admin(a_name,a_email,a_contact,a_pass)
            #     #db.clearscr()
            #     db.insert_admin(admin)

            elif ch=="2":
                #db.clearscr()
                break
                
            else:
                print("\nInvalid Choice ! Try Again .")
# Exit Here
    elif ch=="4":
        #db.clearscr()
        print("\nThank You !")
        #db.clearscr()

        break

    else:
        print("\nInvalid Choice ! Try Again .")
