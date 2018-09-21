#!/usr/bin/perl
mkdir "super_frames";

# To make the movie, the different parameters in the POV-Ray file are linearly
# interpolated between different sets of paremeters. Each row in array below is
# a different set.
@a=(0.07,         1, 0, 0,         0, -360, 
    0.07,         1, 0, 0,         0,    0,
    0.07+0.04/3., 0, 1, 360./3*2,  0,    0,
    0.11,         0, 3, 360*2,     0,    0,
    0.11,         0, 3, 360*6+360, -360, 0);

# Number of frames between each parameter set
@fr=(15,5,10,30);           # 60 total for testing
#@fr=(330,110,220,660);     # 1320 total for complete movie

# POV-Ray rendering options
$pov_opts="+W640 +H480 -J";                 # Low resolution/quality
#$pov_opts="+W1024 +H768 -J +A0.1 +R3";     # Medium resolution/quality
#$pov_opts="+W1025 +H768 -J +A0.01 +R5";    # High resolution/quality
#$pov_opts="+W1200 +H900 -J +A0.001 +R9";   # X-treme resolution/quality

# Frame number
$n=0;

foreach $s (0..3) {
    foreach $o (0..($s==3?$fr[$s]:$fr[$s]-1)) {

        # Compute the linear interpolation of the parameters for this frame
        $z=6*$s;
        $g=$o/$fr[$s];
        $p[$_]=$a[$z+$_]*(1-$g)+$a[$z+6+$_]*$g foreach 0..5;

        # Open the POV-Ray template and replace the markers like "AAA", etc.
        # with the corresponding parameter
        open A,"s_template.pov" or die "Can't open POV template\n";
        open B,">render.pov" or die "Can't open temporary file\n";
        while(<A>) {
            s/AAA/$p[0]/;
            s/BBB/$p[1]/;
            s/CCC/$p[2]/;
            s/DDD/$p[3]/;
            s/EEE/$p[4]/;
            s/FFF/$p[5]/;
            print B;
        }
        close A;
        close B;

        # System call to run POV-Ray and output a frame of the movie
        print "Frame $n: @p\n";
        $of=sprintf "super_frames/fr_%04d.png",$n++;
        system "nice -n 19 povray $pov_opts +O$of render.pov >/dev/null 2>/dev/null";
    }
}
