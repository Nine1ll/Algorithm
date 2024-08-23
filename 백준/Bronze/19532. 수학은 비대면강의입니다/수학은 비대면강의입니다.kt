import java.util.*
fun process(a:Int,b:Int,c:Int,d:Int,e:Int,f:Int){
    // code
    var x = (c*e-f*b)/(a*e-b*d)
    var y = (c*d-f*a)/(b*d - e*a)
    print("$x $y")
    }
    fun main(args: Array<String>) = with(Scanner(System.`in`)) {
        var a = nextInt()
        var b = nextInt()
        var c = nextInt()
        var d = nextInt()
        var e = nextInt()
        var f = nextInt()
        process(a,b,c,d,e,f)
    }