from fdfgen import forge_fdf
forge_fdf.
fields = [('name','John Smith'),('telephone','555-1234')]
fdf = forge_fdf("",fields,[],[],[])
fdf_file = open("data.fdf","w")
fdf_file.write(str(fdf))
fdf_file.close()
