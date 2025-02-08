import EmployeesManager

class FrontendManager:
    def __init__ (self):
        self.employeeManager = EmployeesManager.EmployeesManager()
        self.running = True

    def login (self):
        while self.running:
            username = input ("Podaj nazwę użytkownika: ")
            password = input ("Podaj hasło: ")
            if username == "admin" and password == "admin":
                self.menu()
            else: 
                print ("Nieprawidłowe hasło i/lub nazwa użytkownika. Spróbuj ponownie.")

    def menu(self):
        while True:
            print ("\nOpcje:")
            print ("1. Dodaj pracownika...")
            print ("2. Wyświetl pracowników")
            print ("3. Usuń pracowników z przedziału wiekowego...")
            print ("4. Podwyżka dla...")
            print ("5. Wyjście")

            choice = input ("Wybierz opcję: ")

            if choice == "1":
                name = input ("Podaj imię i nazwisko: ")

                while True:
                    try:
                        age = int(input ("Podaj wiek: "))
                        if age <= 15:
                            raise ValueError("za młody.")
                        break
                    except ValueError as e:
                        print("Błąd: ", e)

                while True:
                    try:
                        salary = float(input ("Podaj wynagrodzenie: "))
                        if salary <= 0:
                            raise ValueError("wynagrodzenie musi być dodatnie.")
                        break
                    except ValueError as e:
                        print ("Błąd: ", e)
                
                self.employeeManager.addEmployee(name, age, salary)

            elif choice == "2":
                self.employeeManager.printEmployees()

            elif choice == "3":
                while True:
                    try:
                        min = int(input ("Podaj dolną granicę: "))
                        if min <= 15:
                            raise ValueError("wiek poza obsługiwanym przedziałem.")
                        break
                    except ValueError as e:
                        print("Błąd: ", e)
                        
                while True:
                    try:
                        max = int(input ("Podaj górną granicę: "))
                        if max<min:
                            raise ValueError("wartość górnej granicy nie może być mniejsza od dolnej.")
                        elif max > 120:
                            raise ValueError("wiek poza obsługiwanym przedziałem.")
                        break
                    except ValueError as e:
                        print("Błąd: ", e)
                        
                self.employeeManager.removeAgeRangeFromList(min, max)

            elif choice == "4":
                name = input ("Podaj imię i nazwisko: ")

                while True:
                    try:
                        salaryRaise = float(input ("Podaj o ile zwiększyć wynagrodzenie: "))
                        break
                    except ValueError as e:
                        print("Błąd: ", e)

                self.employeeManager.raiseByName(name, salaryRaise)

            elif choice == "5":
                self.running = False
                break

            else:
                print ("Nieprawidłowa opcja, spróbuj ponownie.")