
import os
import cv2
cap=cv2.VideoCapture(0)
directory='Image/'
while True:
    _,frame=cap.read()
    count = {
             'a': len(os.listdir(directory+"/pataka")),
             'b': len(os.listdir(directory+"/tripataka")),
             'c': len(os.listdir(directory+"/arthapataka")),
             'd': len(os.listdir(directory+"/karthareemukha")),
             'e': len(os.listdir(directory+"/mayura")),
             'f': len(os.listdir(directory+"/arthachandra")),
             'g': len(os.listdir(directory+"/arala")),
             'h': len(os.listdir(directory+"/sukhatunda")),
             'i': len(os.listdir(directory+"/mushti")),
             'j': len(os.listdir(directory+"/sikhara")),
             'k': len(os.listdir(directory+"/kapidha")),
             'l': len(os.listdir(directory+"/katakamukha")),
             'm': len(os.listdir(directory+"/suchi")),
             'n': len(os.listdir(directory+"/chandrakala")),
             'o': len(os.listdir(directory+"/padmakosa")),
             'p': len(os.listdir(directory+"/sarpaseesha")),
             'q': len(os.listdir(directory+"/mrugaseesha")),
             'r': len(os.listdir(directory+"/simhamukha")),
             's': len(os.listdir(directory+"/langula")),
             't': len(os.listdir(directory+"/alapadma")),
             'u': len(os.listdir(directory+"/chatura")),
             'v': len(os.listdir(directory+"/brahmara")),
             'w': len(os.listdir(directory+"/hamsasya")),
             'x': len(os.listdir(directory+"/hamsapaksha")),
             'y': len(os.listdir(directory+"/samdamsa")),
             'z': len(os.listdir(directory+"/mukula")),

             }
    # cv2.putText(frame, "a : "+str(count['a']), (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "b : "+str(count['b']), (10, 110), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "c : "+str(count['c']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "d : "+str(count['d']), (10, 130), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "e : "+str(count['e']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "f : "+str(count['f']), (10, 150), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "g : "+str(count['g']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "h : "+str(count['h']), (10, 170), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "i : "+str(count['i']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "k : "+str(count['k']), (10, 190), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "l : "+str(count['l']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "m : "+str(count['m']), (10, 210), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "n : "+str(count['n']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "o : "+str(count['o']), (10, 230), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "p : "+str(count['p']), (10, 240), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "q : "+str(count['q']), (10, 250), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "r : "+str(count['r']), (10, 260), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "s : "+str(count['s']), (10, 270), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "t : "+str(count['t']), (10, 280), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "u : "+str(count['u']), (10, 290), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "v : "+str(count['v']), (10, 300), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "w : "+str(count['w']), (10, 310), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "x : "+str(count['x']), (10, 320), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "y : "+str(count['y']), (10, 330), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    # cv2.putText(frame, "z : "+str(count['z']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame,(0,40),(300,400),(255,255,255),2)
    cv2.imshow("data",frame)
    cv2.imshow("ROI",frame[40:400,0:300])
    frame=frame[40:400,0:300]
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(directory+'pataka/'+str(count['a'])+'.png',frame)
    if interrupt & 0xFF == ord('b'):
        cv2.imwrite(directory+'tripataka/'+str(count['b'])+'.png',frame)
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(directory+'arthapataka/'+str(count['c'])+'.png',frame)
    if interrupt & 0xFF == ord('d'):
        cv2.imwrite(directory+'karthareemukha/'+str(count['d'])+'.png',frame)
    if interrupt & 0xFF == ord('e'):
        cv2.imwrite(directory+'mayura/'+str(count['e'])+'.png',frame)
    if interrupt & 0xFF == ord('f'):
        cv2.imwrite(directory+'arthachandra/'+str(count['f'])+'.png',frame)
    if interrupt & 0xFF == ord('g'):
        cv2.imwrite(directory+'arala/'+str(count['g'])+'.png',frame)
    if interrupt & 0xFF == ord('h'):
        cv2.imwrite(directory+'sukhatunda/'+str(count['h'])+'.png',frame)
    if interrupt & 0xFF == ord('i'):
        cv2.imwrite(directory+'mushti/'+str(count['i'])+'.png',frame)
    if interrupt & 0xFF == ord('j'):
        cv2.imwrite(directory+'sikhara/'+str(count['j'])+'.png',frame)
    if interrupt & 0xFF == ord('k'):
        cv2.imwrite(directory+'kapidha/'+str(count['k'])+'.png',frame)
    if interrupt & 0xFF == ord('l'):
        cv2.imwrite(directory+'katakamukha/'+str(count['l'])+'.png',frame)
    if interrupt & 0xFF == ord('m'):
        cv2.imwrite(directory+'suchi/'+str(count['m'])+'.png',frame)
    if interrupt & 0xFF == ord('n'):
        cv2.imwrite(directory+'chandrakala/'+str(count['n'])+'.png',frame)
    if interrupt & 0xFF == ord('o'):
        cv2.imwrite(directory+'padmakosa/'+str(count['o'])+'.png',frame)
    if interrupt & 0xFF == ord('p'):
        cv2.imwrite(directory+'sarpaseesha/'+str(count['p'])+'.png',frame)
    if interrupt & 0xFF == ord('q'):
        cv2.imwrite(directory+'mrugaseesha/'+str(count['q'])+'.png',frame)
    if interrupt & 0xFF == ord('r'):
        cv2.imwrite(directory+'simhamukha/'+str(count['r'])+'.png',frame)
    if interrupt & 0xFF == ord('s'):
        cv2.imwrite(directory+'langula/'+str(count['s'])+'.png',frame)
    if interrupt & 0xFF == ord('t'):
        cv2.imwrite(directory+'alapadma/'+str(count['t'])+'.png',frame)
    if interrupt & 0xFF == ord('u'):
        cv2.imwrite(directory+'chatura/'+str(count['u'])+'.png',frame)
    if interrupt & 0xFF == ord('v'):
        cv2.imwrite(directory+'brahmara/'+str(count['v'])+'.png',frame)
    if interrupt & 0xFF == ord('w'):
        cv2.imwrite(directory+'hamsasya/'+str(count['w'])+'.png',frame)
    if interrupt & 0xFF == ord('x'):
        cv2.imwrite(directory+'hamsapaksha/'+str(count['x'])+'.png',frame)
    if interrupt & 0xFF == ord('y'):
        cv2.imwrite(directory+'samdamsa/'+str(count['y'])+'.png',frame)
    if interrupt & 0xFF == ord('z'):
        cv2.imwrite(directory+'mukula/'+str(count['z'])+'.png',frame)


cap.release()
cv2.destroyAllWindows()
