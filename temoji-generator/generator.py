import cv2
import pandas as pd
import emoji


def generate_letters():
    img = cv2.imread('a.png', 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # apply thresholding to transform into binary image
    # threshold(img, threshold, when it passes the threshold which value should it be assigned (white, 255) and the type of threshold)
    thresh, bw_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    #print(emoji.emojize('Python is :new_moon:'))
    #print(emoji.emojize('Python is :full_moon:'))

    # Convert to pandas dataframe (table)
    df = pd.DataFrame(data=bw_image)





    print(len(df.values[(df == 0).values]))
    df.values[df == 0] = 0.5
    #df.values[(df == 0).values] = 0.5
    print(df.values[(df == 0.5).values])
    print(len(df.values[(df == 0.5).values]))
    
    # All values equal to 0 are going to be full_moon
    df.values[(df == 0).values] = emoji.emojize(':full_moon:')

    # All values higher then 0 are going to be new_moon
    df.values[(df > 0).values] = emoji.emojize(':new_moon:')

    print(df)

    #cv2.imshow("Normal", img)
    #cv2.imshow("B&W Image",bw_image)
    #cv2.waitKey(0)

generate_letters()
