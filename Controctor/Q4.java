package Controctor;

public class Q4 {

    int empId;  
    String empName;  
         
    //parameterized constructor with two parameters
    Q4(int id, String name){  
        this.empId = id;  
        this.empName = name;  
    }  
    void info(){
         System.out.println("Id: "+empId+" Name: "+empName);
    }  
        
    public static void main(String args[]){  
     Q4 obj1 = new Q4(10245,"Chaitanya");  
     
     Q4 obj2 = new Q4(92232,"Negan");  
     obj1.info();  
     obj2.info();  
    }  
 }