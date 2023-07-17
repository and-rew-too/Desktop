import serial
import time
#ser = serial.Serial('/dev/COM9')
#

ser = serial.Serial('COM9',115200, timeout=1)
#line =  ser.readline()
#print(line)
while True:
    data = ""
    data_raw = ser.read(1)
    data_raw = ser.read_until(b'\n') #separates continuous stream of numbers by the "delimiter" \r\n
    print(str(data_raw))
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    time.sleep(.5)
ser.close()
#ser.baudrate = 9600
#ser.port = 'COM9'
#ser_bytes = ser.readline()

# ser.flushInput()
# while True:
#     try:
#         ser_bytes = ser.readline()
#         decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
#         print(decoded_bytes)
#     except:
#         print("Keyboard Interrupt")
#         break
