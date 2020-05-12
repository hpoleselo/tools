## Quick Notes on Video Conversion
I was using at principle ``` ffmpeg ```, but since i was having too much trouble (getting the video but the audio wouldn't play on iPhone, despite playing on PC), i decided to use ``` Handbrake ```, which did work on iPhone X.
Anyway i'm using this ``` .md ``` as a way to document what i've read in order to TRY to convert it correctly.


### Basics

What we actually call the file extension (mp4, mkv etc) can be a media container, the video format is dictated by the video codec. The container synchronises sound and image (subtitle as well) in one piece.

Media Container = video format (video codec) + audio format (audio codec) + subtitle + chapter-information + meta-data

MPEG-4 is the method of defining compression of audio and video, so in order to compress audio and video we have: ``` MPEG-4 part 3 = AAC audio codec ```, ``` MPEG-4 part 10 = Advanced Video Coding (AAC) = H.264 video codec ``` and ``` MPEG-4 part 14 = MP4 media container```.

Codecs: libraries that encode a video, today the best one is h.265 or HEVC, but the broadly used one is h.264

#### Containers:
Example of containers (file formats) are: ```.mp4```,``` .m4v```, ```.mkv```, ```.avi```, ```.flv``` and ```.avchd``` (digital cameras, usually contains h.264 videos with ```.ac3``` audio).

*MKV is better because it has more features than MP4 and it’s open source*
*The M4V file format is a video container format developed by Apple and is very similar to the MP4 format. But M4V files may optionally be protected by DRM copy protection.*

### Handbrake vs FFmpeg

Both programs use the same encoders on back-end. H264 is encoded using a software library called x264 and HEVC uses a software library called x265.
Handbrake has a nice GUI and hides advanced options that are available in ffmpeg, so in fact you have more control in ffmpeg. Speed and quality would be the same supposing we're using the same settings.


### Personal Experience with ffmpeg

``` $ $ mediainfo video.mp4 ```

Apesar do profile de video estar correto pro iPhone (h264, Format/Info: Advanced Video Codec, Format profile: Main@L4), o audio profile creio que nao estava correto:

Command that generated normal audio to PC but without audio on iPhone:

``` $ ffmpeg -i teste.mkv -c:v libx264 -profile:v main -level:v 4.0 -c:a copy output.mp4 ```

O problema parece ser com a componente de audio que foi simplesmente copiada e que provavelmente é colocada como ``` .ogg``` e nao ``` .aac```

Didn't work (without Audio):

```
Audio
ID                                       : 2
Format                                   : Ogg
Codec ID                                 : DD
Duration                                 : 4s 488ms
```

Audio component that did work on iPhone X:

```
Audio
ID                                       : 2
Format                                   : AAC
Format/Info                              : Advanced Audio Codec
Format profile                           : LC
Codec ID                                 : 40
Duration                                 : 4s 459ms
```

No final das contas o comando que eu usei para TENTAR incluir o AAC e não funcionou, principalmente pelo pacote libfdk_aac não ser free, ou seja, nao vem built-in com o ffmpeg, foi esse:

```$ ffmpeg -i teste.mkv -c:v libx264 -profile:v main -level:v 4.0 -c:a libfdk_aac -profile:a lc output.mp4 ```

Taken from FFmpeg documentation:

```
iOS Compatability ([ source][2])
Profile  Level Devices                                                     Options
Baseline 3.0  All devices                                                  -profile:v baseline -level 3.0
Baseline 3.1  iPhone 3G and later, iPod touch 2nd generation and later     -profile:v baseline -level 3.1
Main     3.1  iPad (all vers), Apple TV 2 and later, iPhone 4 and later    -profile:v main -level 3.1
Main     4.0  Apple TV 3 and later, iPad 2 and later, iPhone 4s and later  -profile:v main -level 4.0
High     4.0  Apple TV 3 and later, iPad 2 and later, iPhone 4s and later  -profile:v high -level 4.0
High     4.1  iPad 2 and later, iPhone 4s and later, iPhone 5c and later   -profile:v high -level 4.1
High     4.2  iPad Air and later, iPhone 5s and later                      -profile:v high -level 4.2
```


### Source
https://canaltech.com.br/software/o-que-sao-codecs-quais-sao-os-tipos-pra-que-servem-saiba-mais-sobre-esse-tema/
https://www.videosolo.com/tutorials/mpeg4-vs-mp4.html