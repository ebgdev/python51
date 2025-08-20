# Ogrenci Sistemi

# kisi_sayisi = int(input("Kac kisinin puani girilecek? "))
# dersler = ["mat","fizik","kimya"]
# sinif_toplami = 0
# ogrenci_bilgileri = {}
# for i in range(kisi_sayisi):
# 	kisi_toplami = 0
# 	ogrenci_bilgileri[i] = {}
# 	for ders in dersler:
# 		puan = int(input(f"{i+1}.kisinin {ders} puanini giriniz: "))
# 		ogrenci_bilgileri[i][f'{ders}'] = puan
# 		kisi_toplami += puan
# 	ogrenci_bilgileri[i]['ortalama'] = kisi_toplami/len(dersler)
# 	sinif_toplami += kisi_toplami
# print(ogrenci_bilgileri)
# print(f"\n\nsinif ortalamasi :{sinif_toplami/(kisi_sayisi*len(dersler))}")
# for key, value in ogrenci_bilgileri.items():
# 	print(f"{key}.ogrencinin not ortalamasi: {value['ortalama']}")

# ------------------------------------

# Insertion Sort

# def insertion_sort(arr):
#     for current_index in range(1, len(arr)):
#         current_value = arr[current_index]  # The element to be placed correctly
#         previous_index = current_index - 1

#         # Shift elements to the right to create the correct position for current_value
#         while previous_index >= 0 and current_value < arr[previous_index]:
#             arr[previous_index + 1] = arr[previous_index]
#             previous_index -= 1

#         # Insert the current_value at the correct position
#         arr[previous_index + 1] = current_value


# # Example usage
# numbers = [9, 5, 1, 4, 3]
# insertion_sort(numbers)
# print("Sorted Array in Ascending Order:")
# print(numbers)