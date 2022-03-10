import speech_recognition as sr
import pyttsx3
import nltk
from nltk.corpus import stopwords
import os
import cv2
from PIL import Image
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

a=True
r = sr.Recognizer()

path="D:/data/WLASL/WLASL/frames"

def SpeakText(command):
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()

def generate_video(root):
        image_folder = path
        video_name = 'D:/data/WLASL/WLASL/generated/mygeneratedvideo.avi'
        images = []
        for folders in root:
                if folders in os.listdir(path):
                        new_path = path +"/"+str(folders)
                        images.append(new_path+"/"+str(os.listdir(new_path)[0]))
        print(images)
        #frame= cv2.imread(os.path.join(image_folder, images[0]))
        height , width , layers = 256 , 256, 3
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video = cv2.VideoWriter(video_name,0,1,(width,height))

        for image in images:
                img = cv2.imread(image)
                cv2.imshow("image",img)
                cv2.waitKey(0)
                video.write(img)
                print(video)
        video.write(img)
        cv2.destroyAllWindows()
        video.release()
        cap = cv2.VideoCapture('D:/data/WLASL/WLASL/generated/mygeneratedvideo.avi')
        cv2.namedWindow('Video' , cv2.WINDOW_AUTOSIZE)
        success , img = cap.read()
        cv2.imshow("Video",img)
        cv2.waitKey(1)
        cv2.destroyAllWindows()
while a:
        try:
                with sr.Microphone() as source2:
                        r.adjust_for_ambient_noise(source2,duration=0.2)
                        print("Speak....")
                        audio2 = r.listen(source2,10, 5)
                        print("Processing..")
                        MyText = r.recognize_google(audio2)
                        print("Processing..")
                        MyText = MyText.lower()
                        print("Did you say "+MyText)
                        #sentences = nltk.sent_tokenize(str(MyText))
                        sentences = MyText.split(" ")
                        sentences=nltk.pos_tag(sentences)
                        sentence = []
                        for i in sentences:
                                if i[1]=='VBG':
                                        sentence.append(i[0][:-3])
                                else:
                                        sentence.append(i[0])
                                        
                        print(sentences)
                        print(sentence)
                        root = []
                        wnl = nltk.WordNetLemmatizer()
                        ps = PorterStemmer()
                        for i in sentence:
                                #root.append(i)
                                root.append(wnl.lemmatize(i))
                        print(root)
                        dir_list= os.listdir(path)
                        generate_video(root)
                        a=False
        except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
                print("unknow value error occured")
                
                        
                
