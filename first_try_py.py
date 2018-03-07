import numpy as np
import cv2
import statistics
import math
import matplotlib.pyplot as plt
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        #frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()



"""
cap = cv2.VideoCapture('output.avi')
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

"""



cap = cv2.VideoCapture('output.avi')
num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
if(num_frames%2==1):
    num_frames=num_frames-1
i=1
ret1, frame1 = cap.read()
gray1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
hist1 = cv2.calcHist([gray1],[0],None,[256],[0,256])
correl=[]
chisqr=[]
intersec=[]
bhattacharyya=[]
hellinger=[]
while(i<num_frames):
    ret2, frame2 = cap.read()
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    hist2 = cv2.calcHist([gray2],[0],None,[256],[0,256])
    correl.append(cv2.compareHist(hist1, hist2, 0))
    chisqr.append(cv2.compareHist(hist1, hist2, 1))
    intersec.append(cv2.compareHist(hist1, hist2, 2))
    bhattacharyya.append(cv2.compareHist(hist1, hist2, 3))
    hellinger.append(cv2.compareHist(hist1, hist2, 4))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    ret1=ret2
    frame1=frame2
    gray1=gray2
    hist1=hist2
    i=i+1


cap.release()
cv2.destroyAllWindows()
#print("correl : ",correl,"chisqr : ",chisqr,"intersec : ",intersec,"bhatta : ",bhattacharyya,"hellinger : ",hellinger)

x=range(num_frames-1)

m_correl=math.floor(statistics.mean(correl))+1
m_chi=math.floor(statistics.mean(chisqr))+1
m_inter=math.floor(statistics.mean(intersec))+1
m_bhatta=math.floor(statistics.mean(bhattacharyya))+1
m_hell=math.floor(statistics.mean(hellinger))+1

sd_correl=statistics.stdev(correl)
sd_chi=statistics.stdev(chisqr)
sd_inter=statistics.stdev(intersec)
sd_bhattacharyya=statistics.stdev(bhattacharyya)
sd_hellinger=statistics.stdev(hellinger)

norm_correl=[c - m_correl for c in correl]
norm_chisqr=[c - m_chi for c in chisqr]
norm_intersec=[c - m_inter for c in intersec]
norm_bhattacharyya=[c - m_bhatta for c in bhattacharyya]
norm_hellinger=[c - m_hell for c in hellinger]

"""
"""
plt.scatter(x,norm_correl,label='correlation')

"""
plt.scatter(x,norm_chisqr,label='chi square')
plt.scatter(x,norm_intersec,label='intersection')
plt.scatter(x,norm_bhattacharyya,label='bhattacharyya')
plt.scatter(x,norm_hellinger,label='hellinger')
plt.legend(['correl','chisqr','intersection','bhatta','hellinger'], loc='upper left')
"""
plt.show()

plt.plot(x,norm_correl,label='correlation')
plt.plot(x,norm_chisqr,label='chi square')
plt.plot(x,norm_intersec,label='intersection')
plt.plot(x,norm_bhattacharyya,label='bhattacharyya')
plt.plot(x,norm_hellinger,label='hellinger')
plt.legend(['correl','chisqr','intersection','bhatta','hellinger'], loc='upper left')
plt.show()



cap = cv2.VideoCapture('output.avi')
i=0
while(cap.isOpened() and i<num_frames):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ##if norm_corel[i]<sd_correl+4*m_correl:#################
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()












