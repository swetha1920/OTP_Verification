import random
import smtplib

digits = random.randint(100000, 999999)
# print(digits)
digits = str(digits)


def otp_verify(reciever_email, digits):
    sender_email = "theemailadress@gmail.com"
    sender_password = "the_password_of_emailID"
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(user=sender_email, password=sender_password)
        server.sendmail(from_addr=sender_email, to_addrs=reciever_email, msg=f"Otp is sent to your email {digits}")
        server.close()
        print("OTP sent")
    except Exception as e:
        print("Some error ")
        print(str(e))
    finally:
        server.quit()


r_email = input("Enter your email : ")
otp_verify(r_email,digits)
otp = input("Please enter the otp: ")

if digits == otp:
    print("OTP VERIFIED")
else:
    if digits != otp:
        print("Wrong otp")
    else:
        print("Error in email. Check Email!")
