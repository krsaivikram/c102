import cv2
import dropbox
import time
import random
time = time.time()
def Takesnapshot():
    number = random.randint(0,100)
    videocaptureobject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videocaptureobject.read()
        imagename = "img"+str(number)+".png"
        cv2.imwrite(imagename,frame)
        time=time.time
        result=False
    return imagename
    print("snapshot taken")
    videocaptureobject.release()
    cv2.destroyAllWindows()
def uploadfile(imagename):
    accesstoken='HuWVLHLTviQAAAAAAAAAAT8O_c3QrSM1R5Kh_RLl61AOsRy6Vtwa4Ibm_MVe7jcS'
    file=imagename
    filefrom = file
    fileto = "/testfolder/"+(imagename)
    dbx = dropbox.Dropbox(accesstoken)
    with open (filefrom,'rb')as f:
        dbx.files_upload(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
        print('file uploaded')
def main():
    while(True):
        if((time.time()-time)>=5):
            name=Takesnapshot()
            uploadfile(name)
main()                            