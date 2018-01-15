from app import route,view,app

# route. ( GET POST PUT DELETE )

route.get("/",view.Pages.home)

# route.PostGet("/login",view.Pages..login)

# route.PostGet("/register",view.Pages..register)


# route.get("/<name>/<age>",html="home.html",work="Developer")


# app.run(port=8010)
