# import pdb
# pdb.set_trace()
def Image_Editor():
    import os
    from PIL import Image,ImageEnhance,ImageFilter
    while True:
        print("========= Commands =========")
        print('📌 Change Image Extension ----->> 1\n📌 Resize images ----->> 2\n📌 sharpness ----->>> 3\n📌 color ----->> 4\n📌 Brightness ----->> 5\n📌 Contrast ----->> 6\n📌 Blur ----->> 7\n📌 Exit ----->> Anything except(0-7)')
        
        path = input("📌 Enter the image path : ")
        path_split = path.split(".")
        try:
            if path_split[1]:
                while True:
                    try:
                        Command = int(input("📌 Enter your Command : "))
                        break
                    except ValueError:
                        print("📌 You can only enter integer value  ")
                if Command == 1:
                    img1 = Image.open(f"{path}")
                    extension = input("Enter extension (png,jpg,pdf, etc.) : ").strip().lower()
                    img1.save(f"{path.split('.')[0]}.{extension}")
                    print("Done ✅")
                elif Command == 2:
                    while True:
                        img1 = Image.open(f"{path}")
                            
                        size1 = float(input("Enter length : "))            
                        while True:
                            try:
                                size2 = float(input("Enter breadth : "))
                                break
                            except ValueError:
                                print("💀 Must be numeric value : ")
                        max_size = (size1,size2)
                        img1.thumbnail(max_size)
                        show = input("If you want to see,, press 'Enter' : ")
                        if show == "":
                            img1.show()
                        resize = input("📌 Want to resize (Y or N) : ").strip().lower()
                        if resize == "n":
                            break
                elif Command == 3:
                    while True:
                        img1 = Image.open(f"{path}")
                        enhance1 = ImageEnhance.Sharpness(img1)
                        sharp = float(input("Enter the strength (0,1,2,3,4 etc) : "))
                        split_path = path.split(".")
                        enhance1.enhance(sharp).show()
                        # save = input("Do you want to save ? (Y or N) : ").strip().lower()

                        save = int(input("📌 For Save --->> 0\n📌 Don't Save--->> 1\n📌 Resharp--->> 2 : "))
                        if save == 0:
                            enhance1.enhance(sharp).save(f"{split_path[0]}_edited_{Command}_{sharp}.{split_path[1]}")
                            print("✅ Saved")
                            break
                        elif save == 2:
                            continue
                        else:
                            print("Thank You !!!!💖💖💖`")
                            break

                elif Command == 4:
                    image_edited = False
                    while not image_edited:
                        print("📌 B&W ----> 0\n📌 Real ----> 1\n📌 Enhance color -----> 2,3,4,5")
                        code = int(input("✨ Enter what you want : "))
                        img1 = Image.open(f'{path}')
                        enhance1 = ImageEnhance.Color(img1)
                        split_path = path.split(".")
                        enhance1.enhance(code).show()
                        save = int(input("📌 For Save --->> 0\n📌 Don't Save--->> 1\n📌 Recolor--->> 2 : "))
                        if save == 0:
                            enhance1.enhance(code).save(f"{split_path[0]}_edited_{Command}{code}.{split_path[1]}")
                            print("✅ Saved!!")
                            image_edited = True
                        elif save == 2:
                            continue
                        else:
                            print("Thank You !!!!💖💖💖")
                            image_edited = True
                
                elif Command == 5:
                    while True:
                        img1 = Image.open(f"{path}")
                        enhance1 = ImageEnhance.Brightness(img1)
                        strength = int(input("✨ Enter Strength of brightness : "))
                        enhance1.enhance(strength).show()
                        split_path = path.split(".")
                        save = int(input("📌 For Save --->> 0\n📌 Don't Save--->> 1\n📌 Rebright--->> 2 : "))
                        if save == 0:
                            enhance1.enhance(code).save(f"{split_path[0]}_edited_{Command}{strength}.{split_path[1]}")
                            print("✅ Saved!!")
                            break
                        elif save == 2:
                            continue
                        else:
                            print("Thank You !!!!💖💖💖")
                            break
                elif Command == 6:
                    while True:
                        img1 = Image.open(f"{path}")
                        enhance1 = ImageEnhance.Contrast(img1)
                        strength = int(input("✨ Enter Strength of contrastness : "))
                        split_path = path.split(".")
                        enhance1.enhance(strength).show()
                        save = int(input("📌 For Save --->> 0\n📌 Don't Save--->> 1\n📌 Recontrast --->> 2 : "))
                        if save == 0:
                            enhance1.enhance(strength).save(f"{split_path[0]}_edited_{Command}{strength}.{split_path[1]}")
                            print("✅ Saved!!")
                            break
                        elif save == 2:
                            continue
                        else:
                            print("Thank You !!!!💖💖💖")
                            break
                elif Command == 7:
                    while True:
                        img1 = Image.open(f"{path}")
                        split_path = path.split(".")
                        img1.filter(ImageFilter.GaussianBlur()).show()
                        save = int(input("\n📌 For Save --->> 0\n📌 Don't Save--->> 1\n📌 Re_do --->> 2 : "))
                        if save == 0:
                            img1.filter(ImageFilter.GaussianBlur()).save(f"{split_path[0]}_edited_{Command}.{split_path[1]}")
                            print("✅ Saved")
                            break
                        elif save == 2:
                            continue
                        else:
                            print("Thank You !!!!💖💖💖")
                            break
                            

        except IndexError:
            print("Enter proper image_path 😓😓 ")

        Editagain = input("📌 Do You Want to Continue (Y or N):: ").strip().lower()
        if Editagain == "n":
            print("Thank You for using this system !!! 💖💖💖💖")
            break
Image_Editor()

