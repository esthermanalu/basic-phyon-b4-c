a = input ("Nilai Ujian Teori: ")
b = input ("Nilai Ujian Praktek: ")

if a and b >= 70: 
	print("Selamat, anda lulus!")

if a >= 70 and b < 70:
	print ("Anda harus mengulangi ujian praktek.")

if a <70 and b>=70:
	print("Anda harus mengulangi ujian teori.")

if a <70 and b < 70: 
	print ("Anda harus mengulangi ujian teori dan praktek.")
