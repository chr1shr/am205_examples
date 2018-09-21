#version 3.6;

// Specify a right-handed coordinate system in which the z-axis points upwards
camera {
	location <30,-50,40>
	sky z
	right -0.045*x*image_width/image_height
	up 0.045*z
	look_at <0,0,0>
}

// Two lights with slightly different colors
light_source{<-8,-20,30> color rgb <0.77,0.75,0.75>}
light_source{<25,-12,12> color rgb <0.38,0.40,0.40>}

union{

    // Specify the superellipsoid as the surface x^4+y^4+z^4=1
    polynomial {4,
        xyz(4,0,0):1,
        xyz(0,4,0):1,
        xyz(0,0,4):1,
        xyz(0,0,0):-1
    }

    // The pigment sets the color of the object. Here we use a color map of
    // blues, reds, and yellows
    pigment {
   		bozo
        turbulence 0.3
		color_map {
			[0 color rgb <0,0,0.6>]
			[0.15 color rgb <0.2,0.4,1>]
			[0.5 color rgb <0.6,0.1,0.7> ]
			[0.85 color rgb <1,0.1,0.1>]
			[1 color rgb <1,1,0>]
		}
        scale 0.1
    }

    // The finish controls the surface properties and how it interacts with the
    // light
    finish{reflection 0.24 specular 0.55 ambient 0.25}
}
