#oo programming test
#1/31/2014


#class definition
setClass("polygon", representation(x = "numeric", y = "numeric"))

setMethod("plot", "polygon", function (x,y, ...){
	plot(x@x, x@y, type = "n", ...)
	xp <- c(x@x, x@x[1])
	yp <- c(x@y, x@y[1])
	lines(xp, yp)
})



#instance test
p <- new("polygon", x=c(1,2,3,4), y = c(1,2,3,1))
plot(p)
