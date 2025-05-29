#
from View.Routes import Route_Index, Route_Login, Route_Register




#
def outline_app_routes(app, app_database, User, Classification):
    
    #
    @app.route("/", methods=["GET","POST"])
    def index_page():
        return Route_Index.index_page()
    
    #
    @app.route("/register", methods=["GET","POST"])
    def register_page():
        return Route_Register.register_page(app_database,User,Classification)
    
    #
    @app.route("/login", methods=["GET","POST"])
    def login_page():
        return Route_Login.login_page()