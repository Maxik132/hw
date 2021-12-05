class Customer:
 def __init__(self, surname=None, name=None, patronymic=None, address=None, CreditCardNumber=None, BankAccountNumber=None) :
     self.__Customer = {"Имя" : name ,
      "Фамилия" : surname ,
      "очестро" : patronymic ,
      "Адресс": address ,
      "Номер Кредитки" : CreditCardNumber ,
      "Номер Банковского Счёта" :  BankAccountNumber }

 def info(self) :
     for item in (self.__Customer):
         print(item)

someCustomer = Customer(
    name=input("Имя : "),
    surname=input("Фамилия : "),
    patronymic=input("Очество : "),
    address=input("Адресс : "),
    CreditCardNumber=input("Номер кредитки : "),
    BankAccountNumber=input("Номер банковского счёта : ")
)

someCustomer.info()
 