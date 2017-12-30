from app import route,pages,app


route.GET("/",pages.index)


app.run(port=8010,debug=True)
