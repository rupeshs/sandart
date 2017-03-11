# sandart
Converts photos to sand artworks.


I started with some pixel manipulations/Feature detection and the result is Sand Art

### Demos 
![All examples](https://raw.githubusercontent.com/rupeshs/sandart/master/samples/all.jpg)  

###Dependencies
* Python 3.x 
* PIL

```
usage: sandart.py [-h] -i IMAGE [-s STRENGTH] [-c SANDCOLOR SANDCOLOR SANDCOLOR] [-n INVERT] -o SAVEPATH

SandArt v1.0

optional arguments:
  -h, --help            show this help message and exit
  -i IMAGE, --image IMAGE 
                    Source image path
  -s STRENGTH, --strength STRENGTH 
                          Sand art strength [1-20]
  -c SANDCOLOR SANDCOLOR SANDCOLOR, --sandcolor SANDCOLOR SANDCOLOR SANDCOLOR
                                                 Sand art strength,RGB value eg: 255 30 50
  -tc USETOPCOLOR, --usetopcolor USETOPCOLOR
                       Use top image color as sand color | use 1 to enable 0 to disable | default 0                                       
  -n INVERT, --invert INVERT Invert 
                      style use 1 to enable 0 to disable | default 0
  -o SAVEPATH, --savepath SAVEPATH 
                          Sand art path with file extension
      
```
  
### Differnt options and styles
![Styles](https://raw.githubusercontent.com/rupeshs/sandart/master/samples/styles.jpg) 

