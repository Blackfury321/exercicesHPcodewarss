data = input()
values_list = data.split(",")

var1 = int(values_list[0])
var2 = int(values_list[1])
var3 = int(values_list[2])
var4 = int(values_list[3])
var5 = int(values_list[4])
var6 = int(values_list[5])
var7 = int(values_list[6])


#diferencias

dif1 = var3 - var1 
dif2 = var4 - var2 
dif3 = var5 - var3 
dif4 = var6 - var4 


print(f"MouseMove({dif1},{dif2})") 
print(f"While(True)") 
print(f'    Click(1,"Left")') 
print(f"    MouseMove({dif3},{dif4})") 
print(f'    Click(1,"Left")') 
print(f"    Wait({var7*1000})") 
print(f"    MouseMove({dif3*-1},{dif4*-1})")


