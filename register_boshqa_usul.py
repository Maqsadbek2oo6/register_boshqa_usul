class Registretion_form():
    royxat = {"Ali| Vali": '1234'}
    def __init__(self) -> None:
        pass
    @classmethod
    def check_pwd(self, p1, p2):
        if p1==p2:
            return True
        else:
            return False
    
    def register(self, name, surname, pwd, pwd_again):
        self.name = name
        self.surname = surname
        self.pwd = pwd
        self.pwd_again = pwd_again
        self.tekshiruv = Registretion_form.check_pwd(self.pwd, self.pwd_again)
        self.full = f"{self.name} | {self.surname}"
        if self.tekshiruv and self.full not in list((Registretion_form.royxat).keys()):
            Registretion_form.royxat[self.full] = self.pwd
            print("Siz muvaffaqiyatli ro'yxatdan o'tdingiz")
        elif self.tekshiruv == False:
            print("Kiritilgan parollaringiz bir xil emas")
        elif self.full in list((Registretion_form.royxat).keys()):
            print("Siz ro'yxatdan o'tgansiz")
        else:
            print("Kutilmagan xatolik yuz berdi")

royx = Registretion_form()
royx.register('Ali', 'Aliyev', 'parol123', 'parol123')
print("Xatolik yuz berdi")


royx1 = Registretion_form()
royx1.register('Ali', 'Aliyev', 'parol123', 'parol123')
print("Ro'yxatdan o'tgansiz")

royx2 = Registretion_form()
royx2.register('Ali', 'Aliyev', 'parol123', 'parol13')
print("Parol hatoligi")

