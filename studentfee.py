//PF-Exer-8
//This verification is based on string match.

package main
import ("fmt")
func main(){
    var finalFee int
    //Write your program logic here
    //Populate the variable: finalFee
    var coursefee float32
    coursefee=25000
    var marks float32
    marks=70 
    var extrafee float32
    extrafee=1500
    var scholarship_percentage float32
    scholarship_percentage=marks/2
    var scholarship float32
    scholarship=(coursefee*(scholarship_percentage/100))
    coursefee=coursefee-scholarship
    finalFee=int(coursefee+extrafee)


     //Do not modify the below print statement for verification to work
     fmt.Println(finalFee) 
}
