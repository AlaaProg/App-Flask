from app import route,view,app

# route. ( GET POST PUT DELETE )

route.get("/",view.Pages.home)


app.run(port=8010)
