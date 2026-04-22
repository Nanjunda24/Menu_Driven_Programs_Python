public class Customer {

    private String cName ;
    private long accNo ;
    private double balance ;

    public Customer(String n, long accountNumber,double balance){

        cName = n;
        accNo = accountNumber ;
        this.balance = balance ;
    }

    // Encapsulation : methods --> getter()--> used to read data and setter()--> modufy or update data .
  

    public String getName(){
        return cName ;
    }

    public long getAccNumber(){
        return accNo;
    } 

    double  getBalance(){
        return balance ;
    }


  //modify or update 

    void setName(String name ){
        cName = name ;
    }

    void setAccountNumber(long number){

        accNo = number ;
    }


     void setBalance(int balance){

        if(balance > 0 ){

            this.balance = balance ;
        }
    }   
    
}
