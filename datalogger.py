# reading arduino serial output and saving to .csv file
import serial,time,csv
ser = serial.Serial('/dev/ttyACM0') # read from arduino
ser.flushInput() # clear buffer before reading

while True:
    try:
        # read and decode bytes
        ser_bytes = ser.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        print(decoded_bytes)
        with open('test_data.csv','a',newline='') as f:
            writer = csv.writer(f,delimiter=',')
            writer.writerow([time.time(),decoded_bytes])
    # if keyboard interrupt, stop code
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        break
    # if other error, stop code
    except:
        print("Other Error")
        break
