# SolarTracking
Author: Alex Rogers \
Email: alr021@bucknell.edu

## Description
This project calculates the Sun's current elevation and azimuth in degrees for 
a given latitude and longitude. The user can specify their location in the
`get_coordinates()` method in `Util.py` by changing the city and country
variables. 

Output of program:

![alt text][logo1]

[logo1]: https://i.gyazo.com/2cb8719378dc693d57eb7409feaeb7d1.png

The PySolar data is used as a reference to check my calculated results. The 
calculated results are within hundredths of the PySolar results.

A potential future project with this is using a microcontroller to adjust the
angles of a small solar panel so that it always faces the sun at the optimal
angle for maximum power output.

## Run
To run the program, run `main.py`.

## References

<https://www.pveducation.org/pvcdrom/properties-of-sunlight/solar-time>
<https://www.pveducation.org/pvcdrom/properties-of-sunlight/declination-angle>
<https://www.pveducation.org/pvcdrom/properties-of-sunlight/elevation-angle>
<https://www.pveducation.org/pvcdrom/properties-of-sunlight/azimuth-angle>
<https://www.pveducation.org/pvcdrom/properties-of-sunlight/the-suns-position>