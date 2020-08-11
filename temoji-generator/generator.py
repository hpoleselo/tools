import cv2
import pandas as pd
import emoji


def generate_letters():
    img = cv2.imread('a.png', 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # apply thresholding to transform into binary image
    # threshold(img, threshold, when it passes the threshold which value should it be assigned (white, 255) and the type of threshold)
    thresh, bw_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    resized_img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR) 
    print(resized_img.shape)
    # Convert to pandas dataframe (table)
    df = pd.DataFrame(data=bw_image)


    x, y = bw_image.shape
    #x2, y2 = resized_img.shape
    cv2.imshow('aipayn', resized_img)
    cv2.waitKey(0)
    img_size = x*y
    #res = x2*y2

    # Dar um resize se não teremos muitos emojis..
    print("Colunas: ", x)
    print("Linhas: ", y)
    print("Tamanho da imagem (numero de pixels):", img_size)
    print("Tamanho da imagem resized (numero de pixels):", resized_img)
    print("Numero de zeros: ", len(df.values[(df == 0).values]))
    print("Numero de 255: ", len(df.values[(df > 0).values]))

    # Since it comes from opencv function, the data type is uint8, we have to implement it to be ...?
    #print(df.dtypes)
    # Mudando para ser string, assim conseguimos assinalar como os emojis
    #df = df.astype(str)
    print(df.head(100))
    print("-- Aplicando mudança --")
    
    # All values equal to 0 are going to be full_moon
    #df.values[(df == 0).values] = emoji.emojize(':full_moon:')
    df.values[(df == 0).values] = 0

    # All values higher then 0 are going to be new_moon
    #df.values[(df > 0).values] = emoji.emojize(':new_moon:')
    df.values[(df > 0).values] = 1
    #df.values[(df > 0).values] = emoji.emojize(':new_moon:')



    # USAR A FUNCAO REPLACE()?
    # para usar o replace, precisamos converter as colunas para string
    # data['A'] = data['A'].astype(str) 
    #pega todos os 0 e da replace pelo emoji
    df = df.astype(str) 
    print(df.dtypes)
    #df.['0'] = df.['0'].astype(str)
    df.replace('0',emoji.emojize(':full_moon:'))
    #df.replace('1',emoji.emojize(':new_moon:'))
    #print(df.head(100))



    # For some reason the following attempt did not work to find all the strings on the data frame:
    # df.values.str.contains('255') or df.values[df.values.str.contains('255')]

    # Com a função lambda nao funciona pois nao conseguimos fazer assignment
    #for i in df.columns:
    #    df[i].astype('str').apply(lambda x: df[ if x.startswith('255') else 'pass')

    # usar tabela auxiliar? df2..

    """
    for i in df.columns:
        #df3 = df[i].str.contains('255')
        emoji.emojize(':new_moon:') = df[i].str.contains('255')
    print(df3)
    """
generate_letters()
