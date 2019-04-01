## Approach

For Camera Calibration we need to find some parameters.
1. intrinsic 
2. extrinsic

*Intrinsic parameters are specific to a camera like focal length(fx,fy) and optical centers(Cx,Cy). They are used to find the camera matrix viz 

camera matrix =[[fx,0,Cx],[0,fy,Cy],[0,0,1]]*

*Extrinsic parameters corresponds to rotational and translational vectors which translates a coordinates of 3D pt. to a Coordinate system*

*For stereo applications, these distortions need to be corrected first. To find all these parameters, what we have to do is to provide some sample images of a well defined pattern (eg, chess board). We find some specific points in it ( square corners in chess board). We know its coordinates in real world space and we know its coordinates in image. With these data, some mathematical problem is solved in background to get the distortion coefficients.*
