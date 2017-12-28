
vehical_num=[];
reg_place=[];
reg_name=[];
roadworthness_cert=[];
reg_cert=[];
license=[];
vehical_num=[1,2,3,4,5,6,7,8,9,10];
reg_place=['a','b','c','d','e','f','g','h','i','j'];
reg_name=['k','l','m','n','o','p','q','r','s','t'];
roadworthness_cert=["yes","no","yes","no","yes","no","yes","no","yes","no"];
reg_cert=["yes","yes","no","yes","yes","no","yes","yes","no","yes"];
license=["yes","yes","yes","yes","yes","yes","yes","yes","yes","yes"];
i=0
j=9
var=0
b=1
b=input("press 1 to continue press 6 to exit")
while b!=1:
        
	vehical_num1=input("enter the vehical number")
	for i in range(i,j):
		if vehical_num1==vehical_num[i]:
			var=i
			break
	if var>=0:
		print('vehical number %s'%vehical_num[i])
		print('registration place %s'%reg_place[i])
		print('name %s'%reg_name[i])
		print('roadworthness certificate %s'%roadworthness_cert[i])
		print('registration certificate %s'%reg_cert[i])
		print('license %s'%license[i])
	else:
		print("not registred")
	a=input("for registration press 1")
	if a==1:
		x=input("enter vehical no")
		vehical_num.append(x)
	     #   y=raw_input("enter registration place")
		reg_place.append(y)
		z=raw_input("enter registration name")
		reg_name.append(z)
		u=raw_input("enter roadworthness cartificate details")
		roadworthness_cert.append(u)
		v=raw_input("c-artificate details")
		reg_cert.append(v)
		t=raw_input("enter license details")
		license.append(t)
	j=j+1;
	print("thank you your registration is successfull")
	print('vehical number %s'%vehical_num[j])
	print('registration place %s'%reg_place[j])
	print('name %s'%reg_name[j])
	print('roadworthness certificate %s'%roadworthness_cert[j])
	print('registration certificate %s'%reg_cert[j])
	print('license %s'%license[j])
vehical_num=[];
reg_place=[];
reg_name=[];
roadworthness_cert=[];
reg_cert=[];
license=[];
vehical_num=[1,2,3,4,5,6,7,8,9,10];
reg_place=['a','b','c','d','e','f','g','h','i','j'];
reg_name=['k','l','m','n','o','p','q','r','s','t'];
roadworthness_cert=["yes","no","yes","no","yes","no","yes","no","yes","no"];
reg_cert=["yes","yes","no","yes","yes","no","yes","yes","no","yes"];
license=["yes","yes","yes","yes","yes","yes","yes","yes","yes","yes"];
i=0
j=9
var=0
b=1
b=input("press 1 to continue press 6 to exit")
while b!=1:
        
	vehical_num1=input("enter the vehical number")
	for i in range(i,j):
		if vehical_num1==vehical_num[i]:
			var=i
			break
	if var>=0:
		print('vehical number %s'%vehical_num[i])
		print('registration place %s'%reg_place[i])
		print('name %s'%reg_name[i])
		print('roadworthness certificate %s'%roadworthness_cert[i])
		print('registration certificate %s'%reg_cert[i])
		print('license %s'%license[i])
	else:
		print("not registred")
	a=input("for registration press 1")
	if a==1:
		x=input("enter vehical no")
		vehical_num.append(x)
	     #   y=raw_input("enter registration place")
		reg_place.append(y)
		z=raw_input("enter registration name")
		reg_name.append(z)
		u=raw_input("enter roadworthness cartificate details")
		roadworthness_cert.append(u)
		v=raw_input("c-artificate details")
		reg_cert.append(v)
		t=raw_input("enter license details")
		license.append(t)
	j=j+1;
	print("thank you your registration is successfull")
	print('vehical number %s'%vehical_num[j])
	print('registration place %s'%reg_place[j])
	print('name %s'%reg_name[j])
	print('roadworthness certificate %s'%roadworthness_cert[j])
	print('registration certificate %s'%reg_cert[j])
	print('license %s'%license[j])