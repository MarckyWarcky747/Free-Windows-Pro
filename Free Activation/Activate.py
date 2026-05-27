import os
from time import time

from click import echo, pause


def finish():
    print("Congratulations! Windows has been activated, and you just need to restart your computer to apply the changes! If you chose not embedded, please restart your computer then choose ")

print("Welcome to the Activate Windows For Free Setup Wizard!")
print("Before we start, we need to know if the current key is embedded into your motherboard, or not. Please make sure you run this as an administrator!!")
print("If you do not have a product key, select Not Embedded.")
print("[(H)ow do I know?] [(E)mbedded] [(N)ot Embedded] [(I) have restarted my computer and want to continue with the non-embedded method]")
key = input(">").lower()
os.system("cls")
if key == "h":
    print("Coordinating with CMD...")
    os.system("powershell -Command \"(Get-WmiObject -query 'select * from SoftwareLicensingService').OA3xOriginalProductKey\"")
    print("Please restart the setup wizard and then select if the key was embedded or not.")
    print('If nothing was seen, select "Not Embedded". If a key was seen, select "Embedded".')
    key = input(">").lower()
elif key == "e":
    print("Great! We will now proceed with the embedded key activation method.")
    print("Cooperating with CMD...")
    answer = input(
        "This will delete your current product key! This means you may not be able to reactivate it later. Continue? (y/n) "
    ).strip().lower()
    if answer == "y":
        os.system("backupactivate.bat")
        finish()
    else:
        print("Activation canceled.")
elif key == "n":
    print("Great! We will now proceed with the non-embedded key activation method.")
    print("Cooperating with CMD...")
    answer = input(
        "This will delete your current product key! This means you may not be able to reactivate it later. Continue? (y/n) "
    ).strip().lower()
    print("Note: If any pop-ups appear, click on [OK].")
    if answer == "y":
        os.system("smgr.vbs /upk")
        os.system("slmgr.vbs /cpky")
        os.system("slmgr.vbs /ckms")
        os.system("DISM /online /Get-TargetEditions")
        if input("Do you see Professional? (y/n) ").strip().lower() == "y":
            os.system("sc config LicenseManager start= auto & net start LicenseManager")
            os.system("sc config wuauserv start= auto & net start wuauserv")
            os.system("changepk.exe /productkey VK7JG-NPHTM-C97JM-9MPGT-3V66T")
            print("TIP: If you see an error, this is normal! Click on [Exit].")
        finish()
    else:
        print("Activation canceled.")
elif key == "i":
    print("Great! We will now proceed with the non-embedded key activation method. (Part 2)")
    print("Cooperating with CMD...")
    answer = input(
        "Please ensure you are not choosing this for no reason. This is only for people who have already restarted their computer after running the embedded key method. Continue? (y/n) "
    ).strip().lower()
    print("Note: If any pop-ups appear, click on [OK].")
    if answer == "y":
        os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
        print("All CMD's have been executed! Now you can have fun!")
        finish()
    else:
        print("Activation canceled.")
