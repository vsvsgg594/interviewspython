// .Print gender (Male/Female) program according to given M/F using switch

import java.util.Scanner;
public class Q12{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter choice");
        int n=sc.nextInt();
        System.out.println("are you male/female:press M/F");
        String ch=sc.next();
        switch(n){
            case 1  : if(ch=="M"){
                System.out.println("male");
            }
            break;
            case 2 : if(ch=="F"){
                System.out.println("female");

            }
            break;
            default : System.out.println("wrong options");

        }
    }
}