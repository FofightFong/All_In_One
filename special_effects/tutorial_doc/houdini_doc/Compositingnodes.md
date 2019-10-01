

[Add]()

Adds two images together.


[Anaglyph]()

Creates an anaglyph from a pair of input images.


[Atop]()

Composites the first input (Foreground) over the second (background), but only where the background alpha exists.


[Average]()

Averages the foreground image and the background image.


[Blend]()

Blends frames from two sequences together using a simple linear blend.


[Blur]()

Blurs an image.


[Border]()

Adds a border to the image.


[Bright]()

Applies a brightness factor and bright shift to the first input.


[Bump]()

Builds a bump map from a plane.


[Channel Copy]()

Copy channels from any of inputs into the output image.


[Chromakey]()

Mask or "key" an image based on its color.


[Color]()

Creates a constant color image.


[Color Correct]()

Applies a variety of color corrections to the image


[Color Curve]()

Adjusts the R,G,B and/or A channels based on a user-defined curve.


[Color Map]()

Maps a range of color to a new range.


[Color Replace]()

Replace a color region in an image with another region.


[Color Wheel]()

Generates a simple HSV color wheel.


[Composite]()

Does a composite (over, under, inside, add, etc) between two images.


[Contrast]()

Increases or decreases the contrast of an image.


[Convert]()

Changes the data format of a plane.


[Convolve]()

Performs a generic convolve on the source image.


[Corner Pin]()

Fits an image into an arbitrary quadrilateral.


[Corner Ramp]()

Generates a four corner ramp.


[Crop]()

Crops an image and changes its resolution.


[Cryptomatte]()

Extracts matte from Cryptomatte image.


[DSM Flatten]()

Flattens a Deep Shadow/Camera Map into a flat 2D raster.


[Defocus]()

Defocuses an image similar to a real camera defocus.


[Deform]()

Deforms an image by moving the underlying UV coordinates.


[Degrain]()

Removes film grain from an image.


[Deinterlace]()

De-interlaces a frame of video by either averaging scanlines or copying a scanline.


[Delete]()
Removes planes or components from an input sequence.


[Denoise]()

Removes white noise from an image.


[Depth Darken]()

Darkens depth boundaries in an image.


[Depth of Field]()

Creates a depth-of-field mask, which describes how out of focus parts of the image are.


[Diff]()

Computes the difference between the foreground image and the background image.


[Dilate/Erode]()

Expands and shrinks mattes.


[Drop Shadow]()

Creates a blurred shadow offset of an image.


[Edge Blur]()

Blurs the edges of an image.


[Edge Detect]()

Detects edges in the input image.


[Emboss]()

Adds a lighting effect to the image by using a bump map.


[Environment]()

Applies an environment map to an image.


[Equalize]()

Equalizes colors by stretching or shifting the image histogram.


[Error Function Table Generator]()

Creates an image containing precomputed error function terms for hair albedo computation


[Expand]()

Expands and shrinks mattes.


[Extend]()

Extends the length of a sequence so that it can be animated beyond its frame range.


[Fetch]()

Fetches a sequence of images from another COP, even in another network.


[Field Merge]()

Merges two fields into one Interlaced Frame.


[Field Split]()

Splits an interlaced frame into two fields per frame (odd and even fields).


[Field Swap]()

Swaps the two fields containing the even and odd scanlines of the frame.


[File]()

Loads image files into Houdini.


[Flip]()

Flips the image horizontally and/or vertically.


[Fog]()

Adds a variety of atmospheric effects to an image, including fog, haze and heat waves.


[Font]()

Renders anti-aliased text.


[Front Face]()

Cleans up flipped normals by making them face the camera.


[Function]()

Performs a variety of mathematical functions on the input image.


[Gamma]()

Applies gamma correction to the image.


[Geokey]()

Keys out parts of the image based on pixel position or normal direction.


[Geometry]()

Renders geometry from a SOP as a single color image.


[Gradient]()

Computes the gradient of an image.


[Grain]()

Adds grain to an image.


[HSV]()

Converts between RGB and HSV color spaces, or applies hue and saturation modifications.


[Hue Curve]()

Adjusts the saturation or luminance of the image based on hue.


[Illegal Pixel]()

Detects illegal pixels, like NAN and INF, in images.


[Inside]()

Restricts the foreground color to the area of the background’s alpha matte.


[Interleave]()

Interleaves image sequences.


[Invert]()

Applies a photographic pixel inversion to the image.


[Layer]()

Layers a series of inputs together by compositing them one by one on the background image (input 1).


[Levels]()

Adjusts black point, white point, and midrange to increase, balance, or decrease contrast.


[Lighting]()

Adds a light to the image.


[Limit]()

Limits the pixel range at the high end, low end or both.


[Lookup]()

Applies a lookup table to the input.


[Loop]()

Cooks the subnet COPs multiple times in a loop, accumulating the results.


[Luma Matte]()

Sets the alpha to the luminance of the color.


[Lumakey]()

Keys the image based on luminance (or similar function).


[Mask]()

Masks out an area of an image.


[Max]()

Outputs the maximum value of the foreground and background images for each pixel, which tends to lighten the image.


[Median]()

Applies a 3 x 3 or 5 x 5 median filter to the input image.


[Merge]()

Merges the planes of several inputs together.


[Metadata]()

Applies metadata to an image sequence.


[Min]()

Outputs the minimum value of the foreground and background images for each pixel, which tends to darken the image.


[Mono]()

Converts a color or vector into a scalar quantity, like luminance or length.


[Mosaic]()

Takes a sequence of images and combines them into 1 image by tiling them.


[Multiply]()

Multiplies the foreground image with the background image.


[Noise]()

Generates continuous noise patterns.


[Null]()

Does nothing.


[Outside]()

Restricts the foreground color to the area outside of the background’s alpha matte.


[Over]()

Composites the first input (Foreground) over the second (background).


[Pixel]()

Modifies an image’s pixels using expressions.


[Premultiply]()

Allows colour to be converted to or from a premultiplied form.


[Pulldown]()

Performs a pulldown (cine-expand) on the input sequence.


[Pushup]()

Performs a pushup (cine-expand) on the input sequence.


[Quantize]()

Quantizes input data into discrete steps.


[ROP File Output]()

Renders frames out to disk.


[Radial Blur]()

Does a radial or angular blur.


[Ramp]()

Generates a variety of linear and radial ramps, which are fully keyframable.


[Reference]()

Copies the sequence information from its input.


[Rename]()

Change the name a plane.


[Render]()

Renders a mantra output driver directly into a composite network.


[Reverse]()

Simply reverses the frames in the sequence.


[Rotoshape]()

Draws one or more curves or shapes.


[SOP Import]()

Imports a 2d Volume from SOPs as planes into a composite network.


[Scale]()

Changes the resolution of the image.


[Screen]()

Adds two images together, saturating at white like photographic addition.


[Sequence]()

Sequences two or more inputs end to end.


[Shape]()

Generates simple shapes, such as circles, stars and regular N-sided polygons.


[Sharpen]()

Sharpens an image by enhancing the contrast of edges.


[Shift]()

Shifts an image sequence in time.


[Shuffle]()

Shuffle frames around to do out-of-order editing.


[Sky Environment Map]()

Creates sky and ground images for use as environment maps.


[Snip]()

Either removes frames from a sequence or allows you to order them in a user-defined order.


[Streak Blur]()

Streaks an image, adding a motion blur effect.


[Subnetwork]()

Contains networks of other COPs.


[Subtract]()

Subtracts the foreground image from the background image.


[Switch]()

Passes the input of one of its connected inputs through, acting like an exclusive switch.


[Switch Alpha]()

Replaces input 1's alpha with input 2's alpha.


[Terrain Noise]()

Generate noise suitable for terrain height maps.


[Tile]()

Tiles the image sequence with multiple copies of the input image.


[Time Filter]()

Blurs a pixel through several frames.


[Time Machine]()

Uses a second input to time warp the first input on a per pixel basis.


[Time Scale]()

Stretches or compresses a sequence in time.


[Time Warp]()

Warps time by slowing or speeding it up throughout the sequence.


[Transform]()

Translates, rotates and/or scales the input image without changing the image resolution.


[Trim]()

Trims an input sequence in time by adjusting the beginning or the end of the sequence.


[UV Map]()

Creates a UV map.


[Under]()

Composites the first input (Foreground) under the second (background).


[Unpin]()

Extracts an arbitrary quadrilateral area out of the input image.


[VEX Filter]()

Runs a VEX script on its input planes.


[VEX Generator]()

Runs a VEX script on the planes it generates.


[VOP COP2 Filter]()

Contains a VOP network that filters input image data.


[VOP COP2 Generator]()

Contains a VOP network that generates image data.


[Vector]()

Performs vector operations on the input.


[Velocity Blur]()

Blurs an image by using pixel velocity to produce a motion blur effect.


[Window]()

Cuts a small window out of a larger image.


[Wipe]()

Does a wipe between two input sequences.


[Xor]()

Makes two elements mutually exclusive; if their alpha mattes overlap, the overlap is removed.


[Z Comp]()

Does a Z composite of two images.
