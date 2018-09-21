#version 3.6;

// Specify a right-handed coordinate system in which the z-axis points upwards
camera {
	location <30,-50,40>
	sky z
	right -AAA*x*image_width/image_height
	up AAA*z
	look_at <0,0,0>
}

// Two lights with slightly different colors
light_source{<-8,-20,30> color rgb <0.77,0.75,0.75>}
light_source{<25,-12,12> color rgb <0.38,0.40,0.40>}

// Declare five parameters that control the shapes
#declare b=BBB;         // Color saturation (0=full color, 1=white)
#declare c=CCC;         // Radial position of colored superellipsoids
#declare d=DDD;         // Angular placement of colored superellipsoids
#declare e=EEE;         // Rotation the colored superellipsoids
#declare f=FFF;         // Rotation of the central superellipsoid

// Pre-declare the superellipsoid shape and finish
#declare super=polynomial{4,
    xyz(4,0,0):1,
    xyz(0,4,0):1,
    xyz(0,0,4):1,
    xyz(0,0,0):-1
}
#declare f0=finish{reflection 0.25 specular 0.55 ambient 0.22}

// Make the central white superellipsoid
polynomial{super pigment {rgb 1} rotate <0,0,f> scale 1.001 finish{f0}}

// Make the six colored superellipsoids
polynomial{super pigment {rgb <1,b,b>} finish{f0} rotate <0,0,f-d> translate <c,0,0> rotate <0,0,d+e>}
polynomial{super pigment {rgb <0.95+0.05*b,0.5+0.5*b,b>} finish{f0} rotate <0,0,f-d-60> translate <c,0,0> rotate <0,0,d+e+60>}
polynomial{super pigment {rgb <0.9+0.1*b,0.9+0.1*b,b>} finish{f0} rotate <0,0,f-d-120> translate <c,0,0> rotate <0,0,d+e+120>}
polynomial{super pigment {rgb <b,0.8+0.2*b,b>} finish{f0} rotate <0,0,f-d-180> translate <c,0,0> rotate <0,0,d+e+180>}
polynomial{super pigment {rgb <b,b,1>} finish{f0} rotate <0,0,f-d-240> translate <c,0,0> rotate <0,0,d+e+240>}
polynomial{super pigment {rgb <1,b,1>} finish{f0} rotate <0,0,f-d-300> translate <c,0,0> rotate <0,0,d+e+300>}
