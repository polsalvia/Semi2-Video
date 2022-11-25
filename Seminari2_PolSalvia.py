from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip, clips_array

import os

#exercici 1
def exercice_1(video, save_as):
    N_seconds = int(input("En quants segons vols retallar el video?    ")) #input dels segons que que volem retallar del video
    ffmpeg_extract_subclip(video,0, N_seconds, targetname=save_as)   # el video el retallarem de 0 (escollim 0 de manera predeterminada, també es podria fer un input per el segon d'inici)
                                                                     # a N_seconds (escollits en el input)

#exercici 2
def exercice_2():

    os.system("ffmpeg -i 'BBB_Ex1.mp4' -vf histogram BBB_histogram.mp4") #Aquí obtenim el histograma yuv i el guardem
    os.system("ffmpeg -i BBB_histogram.mp4 -vf scale=1280:720 BBB_histogram_scaled.mp4") # Escalem l'histograma
    os.system("ffmpeg \
      -i BBB_histogram_scaled.mp4 \
      -i BBB_Ex1.mp4 \
      -filter_complex '[0:v]pad=iw*2:ih[int];[int][1:v]overlay=W/2:0[vid]' \
      -map '[vid]' \
      -c:v libx264 \
      -crf 23 \
      -preset veryfast \
      Histogram_and_Video_BBB.mp4") # guardem el video en que es pot veure el histograma i el video simultaneament com: Histogram_and_Video_BBB.mp4





#exercici 3
# De input fiquem BBB video i l'escalem a diferentes mesures i les guardem
def exercice_3():
    os.system("ffmpeg -i BBB_Ex1.mp4 -vf scale=1280:720 BBB_720p.mp4")
    os.system("ffmpeg -i BBB_Ex1.mp4 -vf scale=852:480 BBB_480p.mp4")
    os.system("ffmpeg -i BBB_Ex1.mp4 -vf scale=360:240 BBB_360x240.mp4")
    os.system("ffmpeg -i BBB_Ex1.mp4 -vf scale=160:120 BBB_160x120.mp4")








#exercici 4
def exercice_4():
    INPUT = input(" Escriu 'm' si vols passar de stereo a mono, i escriu 's' si vols passar de mono a stereo")
    if(INPUT == 'm'):
        os.system("ffmpeg -i BBB_Ex1.mp4 -ac 1 BBB_mono.mp4")  # canviem el auio de stereo a mono i ho guardem com BBB_mono.mp4

    if(INPUT == 's'):
        os.system("ffmpeg -i BBB_mono.mp4 -ac 2 BBB_stereo.mp4")  # canviem el auio de MONO a STEREO i ho guardem com BBB_stereo.mp4

    else:
        print("error")










#AQUÍ TENIM ELS DIFERENT EXERCICIS, PER EXECUTAR CADA EXERCICI CAL DESCOMENTAR LA LINEA CORRESPONENT A LA FUNCÓ DEL EXERCICI

#Exercici 1
#exercice_1('BBB.mp4', 'BBB_Ex1.mp4')


#EN AQUESTS EXERCICIS, UTILITZEM EL VIDEO CREAT EN EL EXERCICI 1

#Exercici 2
#exercice_2()


#Exercici 3
#exercice_3()

#Exercici 4
exercice_4()


