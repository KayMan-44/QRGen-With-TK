import qrcode

def Generate_QR(data, file_name):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color = "black", back_color = "white")
    img.save(file_name)
    
    print("QR code generated successfully!: ", file_name)

# Below was just for testing the function above
    
# link_Entry = input("Enter a link: ")    
# Link_Link = link_Entry
# name_Entry = input("Enter a name: ")
# file_Name = name_Entry + ".png"


# Generate_QR(Link_Link, file_Name)
