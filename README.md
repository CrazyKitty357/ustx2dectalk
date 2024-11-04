# ustx2dectalk
this is a python script I made mostly for stream. I wanted to have an easier way to use the phoneme support that dectalk has.

## Requirements
python 3.12  
#### Packages
```
pip install pykakasi
```

## Usage
```
python conv.py <song.ustx>
```
## Limitations
Dectalk only supports one singer at a time, so please match that in OpenUtau. Also I haven't tried what would happen if I had multiple singers, so there's that.  
### Note
If your song is over 120 bpm timings won't work right. To fix this you can go to `Project => Adjust Tempo (Preserve Timings)`

## Links
[OpenUtau](https://www.openutau.com/)  
[DECTALK Github repo](https://github.com/dectalk/dectalk)  
[source of hiragana.json](https://gist.github.com/mdzhang/899a427eb3d0181cd762)