#-----------------------------------------------------------------------------------------------------
# Модуль:      module1
# Назначение:
#
# Автор:       Сергей Софиенко
#
# Создано:     Пн 17.05.2021 11:59:49
# Изменено:
# Права:       (c) Софиенко
#-----------------------------------------------------------------------------------------------------

#msg = [6, 113, 40, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 96, 84, 0, 0, 32, 78, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#RMC:
#msg = [6, 1, 3, 0, 240, 4, 0]


CK_A = 0
CK_B = 0

for i in range(len(msg)):
    CK_A = CK_A + msg[i]
    CK_B = CK_B + CK_A

print (CK_A)

print (CK_B)
