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
    df2 = pd.DataFrame(data=bw_image)


    x, y = bw_image.shape
    img_size = x*y
    print("Tamanho da imagem (numero de pixels):", img_size)
    print("Numero de zeros: ", len(df.values[(df == 0).values]))
    print("Numero de 255: ", len(df.values[(df > 0).values]))

    # Since it comes from opencv function, the data type is uint8, we have to implement it to be ...?
    #print(df.dtypes)
    # Mudando para ser string, assim conseguimos assinalar como os emojis
    #df = df.astype(str)

    print("-- Aplicando mudança --")
    
    # All values equal to 0 are going to be full_moon
    #df.values[(df == 0).values] = emoji.emojize(':full_moon:')

    # All values higher then 0 are going to be new_moon
    #df.values[(df > 0).values] = emoji.emojize(':new_moon:')

    #df.values[(df > 0).values] = emoji.emojize(':new_moon:')

    # For some reason the following attempt did not work to find all the strings on the data frame:
    # df.values.str.contains('255') or df.values[df.values.str.contains('255')]

    # Com a função lambda nao funciona pois nao conseguimos fazer assignment
    #for i in df.columns:
    #    df[i].astype('str').apply(lambda x: df[ if x.startswith('255') else 'pass')

    # usar tabela auxiliar? df2..

generate_letters()
