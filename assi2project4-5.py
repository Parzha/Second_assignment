import datetime

print("entekhab konid")
print("1-tabdile zaman be sanie")
print("2-tabdile sanie be zaman be sorate hours:minutes:seconds")

flag=True
while(True):
    userinput=int(input())
    if userinput == 1 or userinput ==2:
     if userinput ==1 :
        print("zaman khod dar ghabele hours:minutes:seconds vared konid")
        time_input = input()
        date_time = datetime.datetime.strptime(time_input, "%H:%M:%S")
        timeoutput = date_time - datetime.datetime(1900,1,1)
        seconds = timeoutput.total_seconds()
        print(seconds , "seconds")
        flag=False
     elif userinput == 2:
        print("sanie hara vared konid")
        time_input = int(input())
        time_conversion = datetime.timedelta(seconds=time_input)
        converted_time =str(time_conversion)
        print("requested time ",converted_time)
        flag=False

    else:
        print("invalid input try again")