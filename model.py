class Users:
    def __init__(self,u_name,u_email,u_contact,u_pass):
        self.u_name=u_name
        self.u_email=u_email
        self.u_contact=u_contact
        self.u_pass=u_pass

    def __repr__(self):
        return f"Table Users [{self.u_name},{self.u_email},{self.u_contact},{self.u_pass}]"




class Admin:
    def __init__(self,a_name,a_email,a_contact,a_pass):
        self.a_name=a_name
        self.a_email=a_email
        self.a_contact=a_contact
        self.a_pass=a_pass

    def __repr__(self):
        return f"Table Admin[{self.a_name},{self.a_email},{self.a_contact},{self.a_pass }]"


#country,runtime,language,plot summary,

class MoviesTable:
    def __init__(self,movie_name,movie_genre,movie_cast,movie_year,movie_director,movie_runtime,movie_language,movie_country,movie_plotsummary,movie_boxoffice):
        self.movie_name=movie_name
        self.movie_genre=movie_genre
        self.movie_cast=movie_cast
        self.movie_year=movie_year
        self.movie_director=movie_director
        self.movie_runtime=movie_runtime
        self.movie_language=movie_language
        self.movie_country=movie_country
        self.movie_plotsummary=movie_plotsummary
        self.movie_boxoffice=movie_boxoffice


    def __repr__(self):
        return f"Movies [{self.movie_name},{self.movie_genre},{self.movie_cast},{self.movie_year},{self.movie_director},{self.movie_runtime},{self.movie_language},{self.movie_country},{self.movie_plotsummary},{self.movie_boxoffice}]"
    

class MovieReview:
    def __init__(self,movie_name,u_name,u_email,review_comment,review_rating,review_time):
        
        self.movie_name=movie_name
        self.u_name=u_name
        self.u_email=u_email
        self.review_comment=review_comment
        self.review_rating=review_rating
        self.review_time=review_time
    
    def __repr__(self):
        return f"Reviews [{self.movie_name},{self.u_name},{self.u_email},{self.review_comment},{self.review_rating},{self.review_time}]"