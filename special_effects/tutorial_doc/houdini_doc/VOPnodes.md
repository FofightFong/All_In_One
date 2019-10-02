

[Absolute]()

Computes the absolute value of the argument.


[Add]()

Outputs the sum of its inputs.


[Add Attribute]()

Adds a new attribute.


[Add Constant]()

Adds the specified constant value to the incoming integer, float, vector or vector4 value.

[Add Point]()

Adds points to the geometry.


[Add Point to Group]()

Adds the point specified to the group given.

[Add Primitive]()

Adds primitives to the geometry.


[Add Steer Force]()

Multiply steerforce by steerweight attributes and normalize results by total steerweight.

[Add Vertex]()

Adds vertices to the geometry.


[Add Wind Force]()

Layers a wind force onto a simulation.


[Advect by Volumes]()

Advects a position by a set of volume primitives stored in a disk file.

[Agent Clip Catalog]()

Returns all of the animation clips that have been loaded for an agent primitive.

[Agent Clip Length]()

Returns the length (in seconds) of an agent’s animation clip.

[Agent Clip Names]()

Returns an agent primitive’s current animation clips.

[Agent Clip Sample]()

Samples an agent’s animation clip at a specific time.

[Agent Clip Sample Rate]()

Returns the sample rate of an agent’s animation clip.

[Agent Clip Times]()

Returns the current times for an agent primitive’s animation clips.

[Agent Clip Weights]()

Returns the blend weights for an agent primitive’s animation clips.

[Agent Convert Transforms]()

Converts transforms between local space and world space for an agent primitive.

[Agent Layer Bindings]()

Returns the transform that each shape in an agent’s layer is bound to.

[Agent Layer Name]()

Returns the name of the current layer or collision layer of an agent.

[Agent Layer Shapes]()

Returns the names of the shapes referenced by an agent primitive’s layer.

[Agent Layers]()

Returns all of the layers that have been loaded for an agent primitive.

[Agent Rig Children]()

Returns the child transforms of a transform in an agent primitive’s rig.

[Agent Rig Find]()

Finds the index of a transform in an agent primitive’s rig.

[Agent Rig Parent]()

Returns the parent transform of a transform in an agent primitive’s rig.

[Agent Transform Count]()

Returns the number of transforms in an agent primitive’s rig.

[Agent Transform Names]()

Returns the name of each transform in an agent primitive’s rig.

[Agent Transforms]()

Returns the current local or world space transforms of an agent primitive.


[Align]()

Computes a matrix representing the rotation around the axes normal to two vectors by the angle which is between the two vectors.


[Alpha Mix]()

Takes two values for alpha based on the surface orientation relative to the camera and blends between the two with a rolloff as the bias control, effectively removing the silhouettes of the geometry edges.

[Ambient]()

Generates a color using ambient lighting model calculation.


[And]()

Performs a logical "and" operation between its inputs and returns 1 or 0.


[Anti-Aliased Flow Noise]()

Generates anti-aliased (fractional brownian motion) noise by using the derivative information of the incoming position to compute band-limited noise.


[Anti-Aliased Noise]()

Generates anti-aliased noise by using the derivative information of the incoming position to compute band-limited noise.

[Anti-Aliased Ramp Parameter]()


[Append]()

Adds an item to an array or string.


[Arctangent]()

Performs the atan2() function


[Array Contains]()

Checks whether a value exists in an array.


[Array Find Index]()

Finds the first location of an item in an array or string.


[Array Find Indices]()

Finds all locations of an item in an array or string.


[Array Length]()

Produces the length of an array.


[Attenuated Falloff]()

Computes attenuated falloff.


[Average]()

Outputs the average of its inputs.


[Average Vector Component]()

Computes the average value of a vector argument.

[BSDF Tint]()

Tints a BSDF with separate control over colorization and luminance.

[Bake Exports]()

Export shading for use in bake image planes


[Bias]()


[Bind]()

Represents an attribute bound to VEX.


[Blend Regions]()

Takes a float input as a bias to blend between three input regions.


[Block Begin]()

Marks the start of a code block.


[Block Begin For]()

Marks the start of a for loop block.


[Block Begin For-Each]()

Marks the start of a for-each loop block.


[Block Begin If]()

Marks the start of an if code block.


[Block End]()

Marks the end of a code block.


[Block End Break-If]()

Marks the end of a code block.


[Block End While]()

Marks the end of a while code block.


[Bounding Box]()

Returns two vectors representing the minimum and maximum corners of the bounding box for the specified geometry.


[Box Clip]()

Clips the line segment defined by p1 and p2 to the bounding box specified by the min and max corner points.


[Boxes]()

Generates repeating filtered squares.


[Bricker]()

Generates a brick pattern based on the parametric s and t coordinates.

[Brushed Circles]()

Outputs an angle that gives the appearance of a circular brush pattern when used with anisotropy direction.

[Brushed Metal Shader]()

A basic brushed metal shader.


[Build Array]()

Outputs the array consisting of its inputs as array elements.


[Bump Noise]()

Displaces surfaces along their normal using anti-aliased noise, and returns the displaced surface position, normal, and displacement amount.

[Bump To Normal Map]()

Compute a tangent-space normal map from a bump map


[Burlap]()

Generates a burlap displacement pattern useful for simulating rough cloth or weave patterns.

[Burlap Pattern]()

Returns float between 0 and 1 which defines a burlap pattern useful for simulating rough cloth or weave patterns.


[COP Input]()

Returns a pixel value in one of the 4 input COPs connected to the VEX COP.


[CVEX Shader Builder]()

A node that implements a CVEX shader using its children VOPs.

[Car Paint Shader]()

Simulates car paint with embedded metallic flakes and a coat layer.


[Cavities]()

Produces a surface displacement that simulates small surface damage using anti-aliased noise of various frequencies.


[Ceiling]()

Returns the smallest integer greater than or equal to the argument.


[Cellular Cracks]()

Generates a cellular crack displacement suitable for simulating skin, leather, dried earth, and all kinds of crusts.


[Cellular Noise]()

Computes 2D, anti-aliased cellular noise suitable for shading.


[Character to String]()

Converts an unicode codepoint to a UTF8 string.

[Checkered]()

Returns number between 0 and 1 which defines a checkered pattern useful for visualizing parametric or texture coordinates.


[Clamp]()

Clamps the input data between the minimum and maximum values.


[Class Cast]()

Downcasts a generic (anonymous) co-shader object to a specific co-shader


[Classic Shader]()

Flexible material including multiple reflection layers, subsurface scattering, refractions and displacement.


[Classic Shader Core]()

A powerful, highly flexible, generic surface shader with displacement.

[Collect]()

[Color Correction]()

Provides a means to change the hue, saturation, intensity, bias, gain and gamma of the input color.


[Color Map]()

Looks up a single sample of RGB or RGBA color from a disk image.


[Color Mix]()

Computes a blend (or a mix) of its two color inputs, and outputs the resulting color.

[Color Transform]()


[Compare]()

Compares two values and returns true or false.


[Complement]()

Computes the complement of the argument by subtracting the argument from 1.

[Composite]()

[Compute Lighting]()

Computes lighting using Physically Based Rendering.

[Compute Normal]()

This node gives finer control over handling of the normal attribute in VOPs.

[Compute Tangents]()

Compute surface tangents in different ways.

[Conductor Fresnel]()

Outputs a physically correct reflection factor for conductive materials.

[Conserve Energy]()

Clamp the reflectivity of a bsdf to 1.


[Constant]()

Outputs a constant value of any VEX data type.

[Contour]()

Increases or decreases contrast for values at the bottom of the input range.


[Copy]()

Takes a single input of any data type.


[Cosine]()

Performs a cosine function.

[Crackle]()

Returns float between 0 and 1 which defines a crackle pattern useful for simulating the fine grain texture in skin or on a much larger scale dried mudflats.


[Create Point Group]()

Creates a new point group with the name specified.


[Cross Product]()

Computes the cross product between two vectors, defined as the vector perpendicular to both input vectors.

[Curl Noise]()

Creates divergence-free 3D noise using a curl function.

[Curl Noise 2D]()

Creates divergence-free 2D noise using a curl function.


[Curvature]()

Computes surface curvature.

[Decal]()

An OTL that performs composting of texture maps.


[Degrees to Radians]()

Converts degrees to radians.


[Delayed Load Procedural]()


[Delayed Read Archive]()


[Depth Map]()

Works on an image which was rendered as a z-depth image, returning the distance from the camera to the pixel (or plane) in question.


[Determinant]()

Computes the determinant of a 4×4 or 3×3 matrix.

[Direct Lighting]()

Internal VOP used to compute direct lighting.

[Displace]()

Displaces surface position and modifies surface normals.


[Displace Along Normal]()

Displaces the surface along the surface normal by a given amount.

[Displacement Texture]()

Modifies normals and/or positions based on a texture map.


[Distance]()

Returns the distance between two 3D or 4D points.


[Distance Point to Line]()

Returns the closest distance between a point and a line segment defined by two end points.


[Divide]()

Outputs the result of dividing each input value by the next.


[Divide Constant]()

Divides the incoming integer, float, vector or vector4 value by the specified constant value.


[Dot Product]()

Computes the dot product between two vectors.

[Dual Rest]()

Outputs sanitized dual rest values based.

[Dual Rest Solver]()

Sanitizes dual rest attribute data for easier use.


[Edge Falloff]()

Creates a smooth roll-off of the input color from the center of the geometry to the edges, based on the surface normal.

[Eggshell Pattern]()

Returns a new surface normal (N) which has a slight fine grained bump on it.

[Eigenvalues]()


[Ends With]()

Result 1 if the string ends with the specified string.


[Environment Map]()

Sets the environment map (on an infinite sphere) and returns its color.


[Euler to Quaternion]()

Builds a quaternion with the given euler rotation.


[Exponential]()

Computes the exponential function of the argument.


[Extract Transform]()

Extracts the translation, rotation, scale or shear component of a 4×4 transform matrix.

[Fake Caustics]()

Outputs and opacity value which can be used to approximate caustic lighting effects.


[Fast Shadow]()

Sends a ray from the position P along the direction specified by the direction D.

[Field Name]()

Provides a "fallback" value for a field/attribute if the field does not exist or the given field name is an empty string.

[Field Parameter]()

Provides a "fallback" value for a field/attribute if the field does not exist or the given field name is an empty string.

[Filament Sample]()

[Filter Pulse Train]()

Filters the input.


[Filter Shadow]()

Sends a ray from the position P along the direction specified by the direction D, a…


[Filter Step]()

Computes the anti-aliased weight of the step function.

[Filter Width]()

This function returns the square root of the area of a 3D input or the length of the derivative of a float input, such as s or t.

[Find Attribute Value]()

[Find Attribute Value Count]()

[Find Attribute Value by Index]()


[Fit Range]()

Takes the value in the source range and shifts it to the corresponding value in the destination range.


[Fit Range (Unclamped)]]()

Takes the value in the source range and shifts it to the corresponding value in the destination range.


[Float to Integer]()

Converts a float value to an integer value.


[Float to Matrix]()

Converts sixteen floating-point values to a 4×4 matrix value.


[Float to Matrix2]()

Converts four floating-point values to a matrix2 value.


[Float to Matrix3]()

Converts nine floating-point values to a matrix3 value.


[Float to Vector]()

Converts three floating-point values to a vector value.


[Float to Vector2]()

Converts two floating-point values to a vector2 value.


[Float to Vector4]()

Converts four floating-point values to a vector4 value.


[Floor]()

Returns the largest integer less than or equal to the argument.


[Flow Noise]()

Generates 1D and 3D Perlin Flow Noise from 3D and 4D data.


[Fraction]()

Computes the fractional component of the argument.


[Fresnel]()

Computes the Fresnel reflection/refraction contributions given a normalized incident ray, a normalized surface normal, and an index of refraction.


[From NDC]()

Transforms a position from normal device coordinates to the coordinates in the appropriate space.


[From NDC]()

Transforms a position from normal device coordinates to the coordinates in the appropriate space.


[From Polar]()

Converts polar coordinates to cartesian coordinates.


[Front Face]()

Returns the front facing normal of a surface, given a surface normal (N) and an incident ray (I).


[Fur Guide Global Variables]()

Provides outputs representing commonly used input variables of fur guide shader network.


[Fur Guide Output Variables and Parameters]()

Provides inputs representing the output variables of a fur guide shader network.

[Fur Procedural]()

Creates a set of hair-like curves across a surface at render time.


[Fur Skin Global Variables]()

Provides outputs representing commonly used input variables of fur skin shader network.


[Fur Skin Output Variables and Parameters]()

Provides inputs representing the output variables of a fur skin shader network.


[Furrows]()

Displaces the surface along the surface normal by an amount equal to the value of an anti-aliased cosine wave.


[Fuzzy And]()

Performs a fuzzy "and" operation between its inputs and returns a value between 0 and 1.

[Fuzzy Defuzz]()

Performs a defuzzify operation between its input fuzzy sets and returns a crisp value.

[Fuzzy Inference]()

Performs a fuzzy inference operation over each input to determine the truth of the fuzzy set defined on this node.

[Fuzzy Inference Mirror]()

"This node represents two inferred fuzzy sets that are mirrors of one another.

[Fuzzy Input]()

Performs a "fuzzify" operation that calculates a fuzzy value given a membership function and an input crisp value.


[Fuzzy Not]()

This operator performs a fuzzy not operation on an integer or float value.

[Fuzzy Obstacle Sense]()

Detects obstacles in an agent’s field of view.


[Fuzzy Or]()

Performs a fuzzy "or" operation between its inputs and returns a value between 0 and 1.


[Gain]()


[Gather Loop]()

Sends rays into the scene and contains a subnetwork of VOPs to operate on the information gathered from the shaders of surfaces hit by the rays.


[Gaussian Random]()

Generates a random number fitting a Gaussian distribution.


[Gaussian Random UV]()

Generates a random number fitting a Gaussian distribution.

[General Fresnel]()

Computes the Fresnel reflection/refraction contributions and vectors for objects with or without depth.

[Generic Shader]()

Represents a shader.


[Geometry VOP Global Parameters]()

Provides outputs that represent all the global variables for the Attribute VOP network types.


[Geometry VOP Output Variables]()

Simple output variable for Geometry VOP Networks.

[Get Attribute]()

[Get BSDF Albedo]()

Compute the reflectivity of a bsdf.

[Get Blur P]()


[Get CHOP Attribute]()

Returns a CHOP attribute value in one of the 4 input CHOPs connected to the Channel VOP.


[Get Channel Transform]()

Returns a transform value built from 9 channels from one of the 4 input CHOPs connected to the Channel VOP.


[Get Channel Value]()

Returns a sample value in one of the 4 input CHOPs connected to the Channel VOP.


[Get Channel Value by Name]()

Returns a sample value in one of the 4 input CHOPs connected to the Channel VOP.


[Get Element]()

Gets a specified element from array.


[Get Layer Export]()

Obtains a value of the export variable added to the Shader Layer struct.


[Get Matrix Component]()

Extracts a 4×4 matrix component.


[Get Matrix2 Component]()

Extracts a 2×2 matrix3 component.


[Get Matrix3 Component]()

Extracts a 3×3 matrix3 component.


[Get Object Transform]()

Gets the transform matrix of a named object in camera (current) space.

[Get PTexture ID]()

[Get Primitive ID]()


[Get Vector Component]()

Extracts a vector component.


[Get Vector2 Component]()

Extracts a vector2 component.


[Get Vector4 Component]()

Extracts a vector4 component.


[Get a CHOP Channel Value]()

Evaluates a CHOP channel and return its value.


[Get a Channel or Parameter Value]()

Evaluates a channel (or parameter) and return its value.


[Get an Object Transform]()

Evaluates an OBJ node’s transform


[Gingham Checks]()

Generates anti-aliased gingham checks similar to a tablecloth pattern.


[Global Variables]()

Provides outputs that represent all the global variables for the current VOP network type.


[Gradient 3D]()

Returns the gradient of a single channel 3D texture image at a specified position within that image.


[HSV to RGB]()

Converts HSV color space to RGB color space.

[Hair Normal]()

Generates a normal vector which always faces the camera, parallel to the incidence vector.


[Hair Shader]()

A powerful, highly flexible, general model for hair/fur shading.


[Has Input]()

Returns 1 if the specified input (0-3) is connected.


[High-Low Noise]()

Computes a mix of high and low frequency, anti-aliased noise with a wide range of applications.


[Houdini Engine Procedural: Curve Generate]()

Cooks a SOP asset for each point in the source geometry and instances the generated curves onto the point.


[Houdini Engine Procedural: Point Generate]()

Cooks a SOP asset for each point in the source geometry and instances the generated points onto the point.

[Hue Shift]()

Uses the shift value to move the hue of the input color along the color wheel by the amount influenced by the amplitude.


[If Connected]()

Passes through the value of the first input if the first input is ultimately connected.


[Illuminance Loop]()

Only available in Surface VOP networks.


[Image 3D Iso-Texture Procedural]()

This procedural will generate an iso-surface from a 3D texture image (.i3d file).


[Image 3D Volume Procedural]()

This procedural will generate a volume from a 3D texture image (.i3d file).


[Import Attribute]()

Imports attribute data from the OP connected to the given input.

[Import Detail Attribute]()


[Import Displacement Variable]()

Imports the value of the specified variable from a displacement shader and stores it in var.


[Import Light Variable]()

Imports the value of the specified variable from a light shader and stores it in var.

[Import Point Attribute]()

[Import Primitive Attribute]()

[Import Properties from OpenColorIO]()

Imports a color space property from Open Color IO.


[Import Ray Variable]()

Imports the value of the specified variable sent from a trace() function and stores it in var.


[Import Surface Variable]()

Imports the value of the specified variable from a surface shader and stores it in var.

[Import Vertex Attribute]()


[In Group]()

Returns 1 if the point or primitive is in the group specified by the string.

[Indirect Lighting]()

Internal VOP used to compute indirect lighting.


[Inline Code]()

Write VEX code that is put directly into your shader or operator definition.


[Insert]()

Inserts an item, array, or string into an array or string.


[Instance with Hscript Procedural]()

Runs hscript for each point in the source geometry and instances the generated geometry to the point.


[Integer to Float]()

Converts an integer value to a float value.

[Integer to Vector]()


[Intersect]()

Computes the intersection of a ray with geometry.


[Intersect All]()

Computes all the intersections of a ray with geometry.


[Invert]()

If given a 3×3 or 4×4 matrix, this operator computes its inverse (or just returns the input matrix if it detects singularity).


[Irradiance]()

Computes the irradiance (the global illumination) at the point P with the normal N.


[Is Alphabetic]()

Result 1 if all the characters in the string are alphabetic.


[Is Connected]()

Outputs 1 if the input is ultimately connected, otherwise it outputs 0.


[Is Digit]()

Result 1 if all the characters in the string are numeric.


[Is Finite]()

Returns 1 if the number is a normal number, ie, not infinite or NAN.


[Is Fog Ray]()

Returns 1 if the shader is being evaluated from within a fog shader.


[Is Front Face]()

Returns true if the normal of the surface is forward facing, and false if it isn’t.


[Is NAN]()

Returns 1 if the number is not a number.


[Is Shadow Ray]()

Returns 1 if the shader is being evaluated for shadow rays.

[Jittered Hair Normal]()


[Join Strings]()

Concatenate all the strings of an array inserting a common spacer.

[Lambert]()

Generates a color using the Lambert diffuse lighting model calculation.

[Layer Composite]()

Combines two layers using standard compositing operations.

[Layer Mix]()

Outputs a mix of the two input layers, blended using the alpha value.


[Length]()

Computes the length of an array


[Length]()

Computes the length of a 3D or 4D vector.


[Lighting Model]()

Performs a lighting model calculation to generate a color.

[Limits]()

Selectively clamps values to a minimum and/or maximum value.


[Logarithm]()

Computes the natural logarithm function of the argument.


[Look At]()

Computes a 3×3 rotation matrix to orient the z-axis along the vector (to - from) under the transformation.


[Luminance]()

Computes the luminance of the RGB color specified by the input parameter.


[Make Instance Transform]()

Builds a general 4×4 transform matrix derived from the standard copy/instance attributes


[Make Space Transform]()

Returns the transformation matrix to transform from a transform space such as an object’s transform space to another space, such as world space.


[Make Transform]()

Builds a general 4×4 transform matrix.


[Mandelbrot Set]()

Generates a Mandelbrot pattern.


[Material shader builder]()

A higher-level shader that can contain one or more sub-shaders, such as surface shaders, displacement shaders, and rendering properties.


[Matrix to Float]()

Unpacks a 4×4 matrix into its sixteen components.


[Matrix to Vector4]()

Unpacks a 4×4 matrix into its rows.


[Matrix2 to Float]()

Unpacks a 2×2 matrix2 into its four components.

[Matrix2 to Matrix3]()

Converts a 2×2 matrix to a 3×3 matrix.

[Matrix2 to Matrix4]()

Converts a 2×2 matrix to a 4×4 matrix.


[Matrix2 to Vector2]()

Unpacks a 2×2 matrix into its rows.


[Matrix3 to Float]()

Unpacks a 3×3 matrix3 into its nine components.

[Matrix3 to Matrix2]()

Converts a 3×3 matrix to a 2×2 matrix.

[Matrix3 to Matrix4]()


[Matrix3 to Quaternion]()

Converts a matrix3, representing a rotation, to a quaternion representing the same rotation.


[Matrix3 to Vector]()

Unpacks a 3×3 matrix into its rows.

[Matrix4 to Matrix2]()

Converts a 4×4 matrix to a 2×2 matrix.

[Matrix4 to Matrix3]()


[Matte]()

Implements a matte shader that occludes geometry behind the surface being rendered.


[Max Vector Component]()

Computes the maximum value of a vector argument.


[Maximum]()

Outputs the maximum value from its inputs.


[Meta-Loop Import]()

Takes a handle generated by the Meta-Loop Start operator and will import attributes…


[Meta-Loop Next]()

Takes a handle generated by the Meta-Loop Start operator and will "iterate" to the …


[Meta-Loop Start]()

Opens a geometry file and initializes the handle to iterate through all metaballs at the position specified.


[Metaball Attribute]()

Returns the value of the given point attribute at the specified position in the metaball field.


[Metaball Density]()

Returns the density of the metaball field at the specified position.


[Metaball Space]()

Transforms the specified position into the local space of the metaball.


[Metaball Weight]()

Returns the metaweight of the geometry at a given position.


[Metadata]()

Returns true if the specified metadata exists.


[Metadata]()

Returns metadata from one of the 4 input COPs connected to the VEX COP.


[Method]()

Represents a method inside a class-based shader.


[Method Call]()

Invokes a given method on a given struct or co-shader object.


[Method Input]()

Represents a method argument list inside a class-based shader.


[Method Subner]()

Represents a method inside a class-based shader.


[Min Vector Component]()

Computes the minimum value of a vector argument.


[Minimum]()

Outputs the minimum value from its inputs.


[Minimum Position]()

Finds closest position on a primitive in a given geometry file.


[Mix]()

Computes a blend (or a mix) of its input values using linear interpolation.


[Modulo]()

Computes the modulo of two values.


[Multiply]()

Outputs the product of its inputs.


[Multiply Add Constant]()

Will take the input value, add the pre-add amount, multiply by the constant multiplier, then add the post-add amount.


[Multiply Constant]()

Multiplies the incoming value by a constant.


[Near Point]()

Finds closest point in a given geometry file.


[Negate]()

Negates the incoming integer, float, vector or vector4 value.


[Neighbor Count File]()

Count the number of connected points from a given point in a given geometry file (or op:path)


[Neighbor File]()

Finds the nth neighbouring point for a given point in a given geometry file.


[Neighbors]()

Retrieves an array of indices to the points connected to the given point.


[Non-Deterministic Random]()

A non-deterministic random number generator.

[Normal Clamp]()

Clamp shading normals to prevent bad reflection directions

[Normal Falloff]()

Generates a falloff value based on the relationship between the normal and incident vectors.


[Normalize]()

Normalizes a vector.


[Not]()

This operator performs a logical not operation on an integer value, returning 1 if the input is zero, and 0 if the input is non-zero.


[Null]()

Passes the inputs to the output with an optional name change.

[OCIO Color Transform]()

Transforms color spaces using Open Color IO.

[OSL Bias]()

[OSL Calculate Normal]()

[OSL Dx/Dy/Dz]()

[OSL Environment Map]()

[OSL Gain]()

[OSL Logarithm]()


[OSL Shader]()

Implements an OSL shader.

[OSL Step]()

[OSL Texture Map]()

[OSL Transform]()

[OSL Transform Color]()


[Occlusion]()

Computes ambient occlusion at the point P with the normal N.


[Ocean Sample Layers]()

Sample ocean values from layered ocean spectra at the specified position and time.


[OpenSubdiv Face Count]()

Returns the number of coarse faces in the subdivision hull


[OpenSubdiv First Patch]()

Returns the patch of the first patch for a given face in the subdivision hull.


[OpenSubdiv Limit Surface]()

Evaluates a point attribute on the limit of a subdivision surface.


[OpenSubdiv Lookup Face]()

Outputs the Houdini face and UV coordinates corresponding to the given coordinates on an OSD patch.


[OpenSubdiv Lookup Patch]()

Outputs the OSD patch and UV coordinates corresponding to the given coordinates on a Houdini polygon face.


[OpenSubdiv Patch Count]()

Returns the number of patches in the subdivision hull


[Or]()

This operator performs a logical "or" operation between its inputs and returns 1 or 0 .

[Oren-Nayar]()

Generates a color using the Oren-Nayar diffuse lighting model calculation.


[Orient]()

Reorients a vector representing a direction by multiplying it by a 4×4 transform matrix.


[Oscillations]()

Returns an anti-aliased cosine or sine wave.


[Outer Product]()

Computes the outer product of a pair of vectors.


[Output Variables and Parameters]()

Provides inputs representing the writable output variables of the shader network.


[PBR Emission]()

Makes a shaded surface emissive.

[PBR Hair Primary Reflection]()

Produce a hair BSDF.

[PBR Hair Secondary Reflection]()

Produce a hair BSDF.

[PBR Hair Transmission]()

Produce a hair BSDF.

[PBR Lighting]()

Evaluate Lighting Using PBR.


[PBR Metallic Reflection]()

Computes metallic reflections.


[PBR Non-Metallic]()

Computes reflections and refractions for dielectric (non-metallic) materials.

[PBR SSS]()

Creates an approximate SSS BSDF.

[PBR Single Scatter]()

Creates a Single Subsurface Scatter BSDF.


[PBR Volume Phase Function]()

[PRB Diffuse]()

Produce a normalized diffuse bsdf.


[Parameter]()

Represents a user-controllable parameter.


[Periodic Noise]()

Generates 1D and 3D Perlin noise from 1D, 3D and 4D data.


[Periodic Worley Noise]()

Computes 1D, 3D, and 4D tileable Worley noise, which is synonymous with "cell noise".


[Photon Output Variables]()

Performs photon russian roulette.

[Physical SSS]()

Outputs surface color based on a physically-based subsurface scattering model. This node an do physically correct single scattering and/or multiple scattering.


[Pixel Area]()

Returns the area of the current pixel after being transformed to the new UV coordinate uvpos.


[Pixel Derivative]()

Returns U and V derivatives of the current pixel.


[Plane Clip]()

Clips the line segment defined by p1 and p2 against the 3D plane defined by the following equation: plane.


[Plane Count]()

Returns the number of planes in the input.


[Plane Exists]()

Returns the name of the plane with the index plane_index in input input_index.


[Plane Index]()

Returns the index of the plane with the name plane_index in input input_index.


[Plane Name]()

Returns the name of the plane with the index plane_index in input input_index.


[Plane Size]()

Returns the number of components in the plane with the index plane_index in input input_index.


[Point Bounding Box]()

Returns two vectors representing the minimum and maximum corners of the bounding box for the specified geometry.

[Point Cloud Close]()

This node closes a point cloud handle opened by pcopen.

[Point Cloud Export]()

This node exports point data while inside a pcunshaded loop.

[Point Cloud Farthest]()

This node finds the farthest query point produced by pcopen.

[Point Cloud Filter]()

This node filters the points queried by pcopen.


[Point Cloud Find]()

Returns a list of closest points from a file


[Point Cloud Find Radius]()

Returns a list of closest points from a file taking into account their radii.

[Point Cloud Import]()

This node imports point data while inside a pciterate or pcunshaded loop.

[Point Cloud Import by Index]()

This node imports point data from a pcopen.

[Point Cloud Iterate]()

This node advances to the next iteration point returned by pcopen.

[Point Cloud Num Found]()

This node returns the number of points found by pcopen.

[Point Cloud Open]()

This node opens a point cloud file and searches for points around a source position.

[Point Cloud Unshaded]()

This node advances to the next unshaded iteration point returned by pcopen.

[Point Cloud Write]()

This function writes data for the current shading point out to a point cloud file.


[Point Count]()

Returns the number of points for all primitives in the given geometry.


[Point In Group]()

Returns 1 if the point specified by the point number is in the group specified by the string.


[Point Instance Procedural]()

The underlying procedural when using Fast Point Instancing with the instance render parameters.


[Point Loop]()

Only available in Image3D VOP networks.


[Point Replicate]()

The Point Replicate Procedural takes a number of input points and multiplies them, and processes the result using a CVEX script.


[Pop]()

Removes the last element of an array and returns it.


[Power]()

Raises the first argument to the power of the second argument.


[Primitive Attribute]()

Evaluates an attribute for a given primitive at the specified uv parametric location.


[Primitive Intrinsic]()

Evaluates an intrinsic on a given primitive.


[Primitive Normal]()

Returns the normal of a primitive (defined by its number) at the given uv parametric location.


[Principled Shader]()

An artist-friendly shader that can model a large number of materials realistically.


[Principled Shader]()

An artist-friendly shader that can model a large number of materials realistically.


[Print]()

Generate a formatted text string.

[Promote Layer Exports]()

Promotes the export variables from the Shader Layer struct to the parent shader

[Properties]()

[Pxr AOV Light]()

Pxr AOV Light shader

[Pxr Adjust Normal]()

Pxr Adjust Normal shader

[Pxr Area Light]()

Pxr Std Area Light light shader

[Pxr Attribute]()

Pxr Attribute shader

[Pxr Background Display Filter]()

Pxr Background Display Filter shader

[Pxr Background Sample Filter]()

Pxr Background Sample Filter shader

[Pxr Bake Point Cloud]()

Pxr Bake Point Cloud shader

[Pxr Bake Texture]()

Pxr Bake Texture shader

[Pxr Barn Light Filter]()

Pxr Barn Light Filter shader

[Pxr Black]()

Pxr Black shader

[Pxr Black Body]()

Pxr Black Body pattern shader

[Pxr Blend]()

Pxr Blend shader

[Pxr Blocker]()

Pxr Blocker light filter shader

[Pxr Blocker Light Filter]()

Pxr Blocker Light Filter shader

[Pxr Bump]()

Pxr Bump shader

[Pxr Bump Manifold 2d]()

Pxr Bump Manifold 2d shader

[Pxr Camera]()

Pxr Camera shader

[Pxr Checker]()

Pxr Checker shader

[Pxr Clamp]()

Pxr Clamp shader

[Pxr Color Correct]()

Pxr Color Correct shader

[Pxr Combiner Light Filter]()

Pxr Combiner Light Filter shader

[Pxr Constant]()

Pxr Constant shader

[Pxr Cookie Light Filter]()

Pxr Cookie Light Filter shader

[Pxr Copy AOV Display Filter]()

Pxr Copy AOV Display Filter shader

[Pxr Copy AOV Sample Filter]()

Pxr Copy AOV Sample Filter shader

[Pxr Cross]()

Pxr Cross shader

[Pxr DebugShadingContext]()

Pxr DebugShadingContext shader

[Pxr Default]()

Pxr Default integrator shader

[Pxr Direct Lighting]()

Pxr Direct Lighting integrator shader

[Pxr Dirt]()

Pxr Dirt shader

[Pxr Disk Light]()

Pxr Disk Light shader

[Pxr Disney]()

Pxr Disney bxdf shader

[Pxr Disp Transform]()

Pxr Disp Transform shader

[Pxr Disp Vector Layer]()

Pxr Disp Vector Layer shader

[Pxr Displace]()

Pxr Displace shader

[Pxr Displacement]()

Pxr Displacement shader

[Pxr Display Filter Combiner]()

Pxr Display Filter Combiner shader

[Pxr Disps Calar Layer]()

Pxr Disps Calar Layer shader

[Pxr Distant Light]()

Pxr Distant Light shader

[Pxr Dome Light]()

Pxr Dome Light shader

[Pxr Dot]()

Pxr Dot shader

[Pxr Envday Light]()

Pxr Envday Light shader

[Pxr Exposure]()

Pxr Exposure shader

[Pxr FacingRatio]()

Pxr FacingRatio shader

[Pxr Filmic Tone Mapper Display Filter]()

Pxr Filmic Tone Mapper Display Filter shader

[Pxr Filmic Tone Mapper Sample Filter]()

Pxr Filmic Tone Mapper Sample Filter shader

[Pxr Flakes]()

Pxr Flakes shader

[Pxr Fractal]()

Pxr Fractal pattern shader

[Pxr Fractialize]()

Pxr Fractialize shader

[Pxr Gamma]()

Pxr Gamma shader

[Pxr Geometric AOVs]()

Pxr Geometric AOVs shader

[Pxr Gobo]()

Pxr Gobo light filter shader

[Pxr Gobolight Filter]()

Pxr Gobolight Filter shader

[Pxr Grade Display Filter]()

Pxr Grade Display Filter shader

[Pxr Grade Sample Filter]()

Pxr Grade Sample Filter shader

[Pxr Hair Color]()

Pxr Hair Color shader.

[Pxr Half Buffer Error Filter]()

Pxr Half Buffer Error Filter shader.

[Pxr Hsl]()

Pxr Hsl shader

[Pxr Image Display Filter]()

Pxr Image Display Filter shader

[Pxr Image Plane Filter]()

Pxr Image Plane Filter shader

[Pxr Int Mult Light Filter]()

Pxr Int Mult Light Filter shader

[Pxr Invert]()

Pxr Invert shader

[Pxr Layer]()

Pxr Layer shader

[Pxr Layer Mixer]()

Pxr Layer Mixer shader

[Pxr Layered Texture]()

Pxr Layered Texture shader

[Pxr Layeredblend]()

Pxr Layeredblend shader

[Pxr Light Probe]()

Pxr Light Probe shader

[Pxr Lightemission]()

Pxr Lightemission shader

[Pxr Lmdiffuse]()

Pxr Lmdiffuse shader

[Pxr Lmglass]()

Pxr Lmglass shader

[Pxr Lmlayer]()

Pxr Lmlayer shader

[Pxr Lmmixer]()

Pxr Lmmixer shader

[Pxr Lmplastic]()

Pxr Lmplastic shader

[Pxr Lmsubsurface]()

Pxr Lmsubsurface shader

[Pxr Manifold 3D]()

Pxr Manifold 3D manifold shader

[Pxr Manifold2d]()

Pxr Manifold2d shader

[Pxr Manifold3dn]()

Pxr Manifold3dn shader

[Pxr Marschnerhair]()

Pxr Marschnerhair shader

[Pxr Matteid]()

Pxr Matteid shader

[Pxr Mesh Light]()

Pxr Mesh Light shader

[Pxr Mix]()

Pxr Mix shader

[Pxr Multi Texture]()

Pxr Multi Texture shader

[Pxr Normalmap]()

Pxr Normalmap shader

[Pxr Occlusion]()

Pxr Occlusion shader

[Pxr Omini Directional Stereo]()

Pxr Omini Directional Stereo

[Pxr Osl]()

Pxr Osl shader

[Pxr Path Tracer]()

Pxr Path Tracer integrator shader

[Pxr Portal Light]()

Pxr Portal Light shader

[Pxr Primvar]()

Pxr Primvar shader

[Pxr Projection Stack]()

Pxr Projection Stack shader

[Pxr Projectionlayer]()

Pxr Projectionlayer shader

[Pxr Projector]()

Pxr Projector shader

[Pxr Ptexture]()

Pxr Ptexture shader

[Pxr Ramp]()

Pxr Ramp shader

[Pxr Ramp Light Filter]()

Pxr Ramp Light Filter shader

[Pxr Random Texture Manifold]()

Pxr Random Texture Manifold shader.

[Pxr Rect Light]()

Pxr Rect Light shader

[Pxr Remap]()

Pxr Remap shader

[Pxr Rod Light Filter]()

Pxr Rod Light Filter shader

[Pxr Rolling Shutter]()

Pxr Rolling Shutter shader

[Pxr Roundcube]()

Pxr Roundcube shader

[Pxr Sample Filter Combiner]()

Pxr Sample Filter Combiner shader

[Pxr Seexpr]()

Pxr Seexpr shader

[Pxr Shaded Side]()

Pxr Shaded Side shader

[Pxr Shadow Display Filter]()

Pxr Shadow Display Filter shader

[Pxr Shadow Filter]()

Pxr Shadow Filter shader

[Pxr Sphere Light]()

Pxr Sphere Light shader

[Pxr Std Env Day Light]()

Pxr Std Env Day Light light shader

[Pxr Std Env Map Light]()

Pxr Std Env Map Light light shader

[Pxr Surface]()

Pxr Surface shader

[Pxr Tangentfield]()

Pxr Tangentfield shader

[Pxr Tee]()

Pxr Tee shader

[Pxr Texture]()

Pxr Texture shader

[Pxr Thinfilm]()

Pxr Thinfilm shader

[Pxr Threshold]()

Pxr Threshold shader

[Pxr Tile Manifold]()

Pxr Tile Manifold shader

[Pxr Tofloat]()

Pxr Tofloat shader

[Pxr Tofloat3]()

Pxr Tofloat3 shader

[Pxr UPBP]()

Pxr UPBP shader

[Pxr VCM]()

Pxr VCM integrator shader

[Pxr Validatebxdf]()

Pxr Validatebxdf shader

[Pxr Variable]()

Pxr Variable shader

[Pxr Vary]()

Pxr Vary shader

[Pxr Visualizer]()

Pxr Visualizer shader

[Pxr Volume]()

Pxr Volume shader

[Pxr Voronoise]()

Pxr Voronoise pattern shader

[Pxr White Point Display Filter]()

Pxr White Point Display Filter shader

[Pxr White Point Sample Filter]()

Pxr White Point Sample Filter shader

[Pxr Worley]()

Pxr Worley shader

[PxrLm Metal]()

PxrLm Metal shader

[Pyro Blackbody]()

Converts a temperature value into color (chroma) and intensity according to the blackbody radiation model.

[Pyro Color Correct]()

Provides color correction functions.

[Pyro Color Model]()

Provides constant, artistic, and physically correct (blackbody) tint as well as color correction functions.

[Pyro Color Volume]()

Provides functions for editing color fields by conditioning the field values, adding noise, filtering, and color correction.

[Pyro Density Volume]()

Provides functions for editing fields such as density by conditioning the field values, adding noise, and filtering.

[Pyro Displace]()

[Pyro Field]()

[Pyro Noise]()


[Pyro Shader]()

Flexible, production-quality fire and smoke shader.


[Pyro Shader Core]()

Provides the core functionality needed to build a high-quality volumetric shader.


[Quaternion]()

Takes an angle and an axis and constructs the quaternion representing the rotation about that axis.


[Quaternion Distance]()

Computes distance between quaternions in radians.


[Quaternion Invert]()

Takes an quaternion inverts it..


[Quaternion Multiply]()

Performs a quaternion multiplication with its two inputs.


[Quaternion to Angle/Axis]()

Converts a quaternion to angle/axis form.


[Quaternion to Matrix3]()

Converts a vector4, representing a quaternion, to a matrix3 value, representing the same rotation.


[RGB to HSV]()

Converts RGB color space to HSV color space.


[RSL Gather Loop]()

Sends rays into the scene and contains a subnetwork of VOPs to operate on the information gathered from the shaders of surfaces hit by the rays.


[RSL Material]()

Implements an RSL material.


[Radians to Degrees]()

Converts radians to degrees.


[Rainbow]()

Generates a non-repeating rainbow color ramp by modulating the hue over the range of the parametric coordinate s and using the given saturation and value to compute the HSV color.

[Ramp Filter]()

Adds anti-aliased analytical filtering to the output of a Ramp Parameter VOP.


[Ramp Parameter]()

Represents a user-editable ramp parameter.


[Ramps]()

Generates repeating filtered ramps.


[Random]()

Generates a random number based on the position in one, three, or four dimensions.


[Random Sobol]()

Generates a random number in a Sobol sequence.

[Random Value]()


[Ray Bounce Level]()

Returns the current ray-bounce level.


[Ray Bounce Weight]()

Returns the amount that the current bounce level will contribute to the final pixel color.


[Ray Hit]()

This operator sends a ray from the position P along the direction specified by the direction D, and returns the distance to the object intersected or a negative number if not object found.


[Ray Trace]()

Sends a ray starting at origin P and in the direction specified by the normalized vector D.


[Reflect]()

Returns the vector representing the reflection of the direction against the normal vector.


[Reflected Light]()

Computes the amount of reflected light which hits the surface.


[Refract]()

Computes the refraction ray given an incoming direction, the normalized normal and an index of refraction.


[Refracted Light]()

Sends a ray starting at origin P and in the direction specified by the normalized vector I.


[Regex Find]()

Finds the given regular expression in the string.


[Regex Findall]()

Finds all instances of the given regular expression in the string.


[Regex Match]()

Result 1 if the entire input string matches the expression.


[Regex Replace]()

Replaces instances of find_regex with replace_regex.


[Regex Split]()

Splits the given string based on regex match.


[Relative to Bounding Box]()

Returns the relative position of the point given with respect to the bounding box of the specified geometry.


[Relative to Point Bounding Box]()

Returns the relative position of the point given with respect to the bounding box of the specified geometry.


[Remove Index]()

Removes an item at the given index from an array.

[Remove Point]()

Removes points from the geometry.

[Remove Primitive]()


[Remove Value]()

Removes an item from an array.


[Render State]()

Gets state information from the renderer.

[RenderMan Bias]]()

[RenderMan Calculate Normal]()

[RenderMan Deriv]()

[RenderMan Du/Dv]()

[RenderMan Environment Map]()

[RenderMan Gain]()

[RenderMan Illuminance Loop]()

[RenderMan Illuminate Construct]()

[RenderMan Import Value]()

[RenderMan Indirect Diffuse]()

[RenderMan Logarithm]()

[RenderMan Occlusion]()

[RenderMan Ray Information]()

[RenderMan Render State Information]()

[RenderMan Shadow Map]()

[RenderMan Step]()

[RenderMan Surface Color]()

[RenderMan Texture Map]()

[RenderMan Texture Map Information]()

[RenderMan Transform]()

[RenderMan Transform Color]()

[RenderMan Z-Depth From Camera]()


[Reorder]()

Reorders items in an array or string.


[Report Error]()

Optionally report a custom VEX error or warning.

[Reshape Value]()

Modulates input value using a variety of methods.


[Resolution]()

Returns the pixel resolution of an input.


[Rest Position]()

Checks if the geometry attribute "rest" is bound and, if so, uses it as the rest position for shading.


[Return]()

Generates a return statement inside a method or a function defined by the parent subnet.


[Reverse]()

Adds an item to an array or string.


[Rings]()

Generates repeating filtered rings.


[Ripples]()

Generates repeating ripples.


[Rotate]()

Applies a rotation by 'angle' radians to the given 3×3 or 4×4 matrix.


[Rotate by Quaternion]()

Rotates a vector by a quaternion.


[Round to Integer]()

Rounds the argument to the closest integer.

[Rounded Edge]()

Blends the normals between faces within specified radius.


[Rounded Hexes]()

Generates repeating filtered rounded hexagons.


[Rounded Stars]()

Generates repeating filtered rounded five-pointed stars.


[Run External Program Procedural]()

This procedural will run an external application in order to generate geometry at render time.

[SSS Component]()

Adds energy conservation functionality and additional controls to the Physical SSS VOP.


[Sample Sphere]()

Samples the interior or surface of the unit circle, sphere, or hypersphere, within a max angle of a direction.


[Scale]()

Scales a 3×3 or 4×4 matrix by 'amount' units along the x,y, and z axes.


[Scales]()

Generates a scale-like pattern and returns the displaced position, normal, and displacement amount.


[Sensor Panorama Color]()

Requests the rendered color from a specified direction


[Sensor Panorama Cone]()

Returns an average direction, color, depth, and strength.


[Sensor Panorama Create]()

Renders the surrounding environment


[Sensor Panorama Depth]()

Requests the rendered depth from a specified direction


[Sensor Panorama Save]()

Saves the rendered panorama to a specified output file


[Sensor Save]()

Saves sensor data to image files.

[Set Agent Clip Names]()

Sets the current animation clips for an agent primitive.

[Set Agent Clip Times]()

Sets the current times for an agent primitive’s animation clips.

[Set Agent Clip Weights]()

Sets the blend weights for an agent primitive’s animation clips.

[Set Agent Layer]()

Sets the current layer or collision layer of an agent primitive.

[Set Agent Transforms]()

Overrides the transforms of an agent primitive.

[Set Attribute]()


[Set CHOP Attribute]()

Sets a CHOP attribute value.


[Set Channel Tranform]()

Sets a transform value when evaluating a Channel VOP in Tranlate/Rotate/Scale mode.


[Set Channel Value]()

Sets a channel value when evaluating a Channel VOP in Channel/Sample modes.


[Set Element]()

Sets the element at the specified index.


[Set Layer Export]()

Adds layer exports to the Shader Layer struct


[Set Matrix Component]()

Assigns a value to one of the matrix’s components.


[Set Matrix2 Component]()

Assigns a value to one of the matrix2's components.


[Set Matrix3 Component]()

Assigns a value to one of the matrix3's components.

[Set Primitive Vertex]()


[Set Vector Component]()

Assigns a value to one of the vector’s components.


[Set Vector2 Component]()

Assigns a value to one of the vector2's components.


[Set Vector4 Component]()

Assigns a value to one of the vector4's components.


[Shader Output Export Variables]()

Represents export parameters in a shader call.


[Shader Output Global Variables]()

Represents global variables that are bound as output parameters in a shader call.


[Shading Area]()

Computes the shading area of the given variable.


[Shading Derivative]()

Computes the derivative of a given variable with respect to the s or t parametric coordinate.


[Shading Layer Parameter]()

Creates a parameter to appear in the signature of the VEX function defined by the VOP network (VOPNET).


[Shading Normal]()

Computes the normal at the location specified by the P position.


[Shadow]()

This shader calls the shadow shader inside an illuminance loop.


[Shadow Map]()

Shadow Map treats the depth map as if the image were rendered from a light source.


[Shadow Matte]()

Implements a shadowmatte shader that occludes geometry behind the surface being rendered.


[Sign]()

Returns -1 if the input is less than 0, otherwise it returns 1.


[Sine]()

Performs a sine function.


[Skin Shader Core]()

A skin shader with three levels of subsurface scattering.


[Slice]()

Slices a sub-string or sub-array of a string or array.


[Smooth]()

Computes a number between zero and one.


[Smooth Rotation]()

Returns the closest equivalent Euler rotations to a reference rotation.


[Snippet]()

Runs a VEX snippet to modify the incoming values.

[Soft Clip]()

Increases or decreases contrast for values at the top of the input range.


[Soft Dots]()

Generates repeating soft dots.


[Sort]()

Returns the array sorted in increasing order.

[Specular]()

Generates a color using the selected specular lighting model calculation.

[Specular Sheen]()

Generates a color using a specular lighting model with a Fresnel falloff calculation.


[Spherical Linear Interp]()

Computes a spherical linear interpolation between its two quaternion inputs, and outputs the intermediate quaternion.


[Splatter]()

Generates a splatter pattern and returns the splatter amount.


[Spline]()

Computes either a Catmull-Rom (Cardinal) spline or a Linear spline between the specified key points, given an interpolant (u) in the domain of the spline.


[Split String]()

Splits a string into tokens.


[Sprites Procedural]()

This procedural will render points as sprites.


[Square Root]()

Computes the square root of the argument.


[Starts With]()

Result 1 if the string starts with the specified string.


[String Length]()

Returns the length of the string.


[String to Character]()

Converts an UTF8 string into a codepoint.


[Strip]()

Strips leading and trailing whitespace from a string.


[Stripes]()

Generates repeating filtered stripes.


[Struct]()

Creates, modifies, or de-structures an instance of a structured datatype.


[Struct Pack]()

Bundles input values into an instance of an ad-hoc struct.


[Struct Unpack]()

Extracts one or more values from a struct by member name.


[Sub Network]()

Contains other VOP operators.


[Subnet Connector]()

Represents an input or an output (or both) of the parent VOP subnet.


[Subnet Input]()

Allows the connection of operators outside a subnet to operators inside the subnet.


[Subnet Output]()

Allows the connection of operators inside a subnet to operators outside the subnet.


[Subtract]()

Outputs the result of subtracting all its inputs.


[Subtract Constant]()

Subtracts the specified constant value from the incoming integer, float, vector or vector4 value.

[Surface Color]()

Generates a basic color with a choice of tinting with the point color and/or a color map.


[Surface Distance]()

Finds the shortest distance between a point and a source point group.


[Switch]()

Switches between network branches based on the value of an input.

[Switch Lighting BSDF]()

Use a different bsdf for direct or indirect lighting.


[Swizzle Vector]()

Rearranges components of a vector.


[Swizzle Vector2]()

Rearranges components of a vector2.


[Swizzle Vector4]()

Rearranges components of a vector4.


[Tangent]()

Performs a tangent function.

[Tangent Normal]()

Transform an input normal to UV/tangent space

[Tangent Normal Remap]()

Transform an input normal from UV/tangent to current space

[Tangent Normals]()

Exports shader normals as a render plane.


[Tetrahedron Adjacent]()

Returns primitive number of an adjacent tetrahedron.


[Tetrahedron Adjacent]()

Returns vertex indices of each face of a tetrahedron.


[Texture]()

Computes a filtered sample of the texture map specified and returns an RGB or RGBA color.


[Texture 3D]()

Returns the value of a 3D image at a specified position within that image.


[Texture 3D Box]()

Queries the 3D texture map specified and returns the bounding box information for the given channel in the min and max corner vectors.


[Texture Map]()


[Thin Film Fresnel]()

Computes the thin film reflection and refraction contributions given a normalized incident ray, a normalized surface normal, and an index of refraction.


[Tiled Boxes]()

Generates staggered rectangular tiles.


[Tiled Hexagons]()

Generates staggered hexagonal tiles.


[Timing]()

Returns the frame range and rate of the given input.


[Title Case]()

Returns a string that is the titlecase version of the input string.


[To Lower]()

Returns a string that is the lower case version of the input string.


[To NDC]()

Transforms a position into normal device coordinates.

[To NDC]()


[To Polar]()

Converts cartesian coordinates to polar coordinates.


[To Upper]()

Returns a string that is the upper case version of the input string.

[Trace]()

Uses the vex gather function to send a ray and return with the reflected or refracted colors.


[Transform]()

Transforms a vector to or from an object’s transform space, or one of several other spaces, such as world or camera space.


[Transform Matrix]()


[Translate]()

Translates a 4×4 matrix 'amount' units along the x,y,z and possibly w axes.


[Transpose]()


[Trigonometric Functions]()

Performs a variety of trigonometric functions.


[Turbulent Noise]()

Can compute three types of 1D and 3D noise with the ability to compute turbulence with roughness and attenuation.


[Two Sided]()

Generates a two sided surface.


[Two Way Switch]()

Takes an integer input.


[USD Global Variables]

Provides outputs representing commonly used input variables for processing USD primitive attributes inside an Attribute VOP LOP.

[USD Preview Surface]()

USD Preview Surface shader

[USD Prim Var Reader]()

USD Prim Var Reader shader

[USD UV Texture]()

USD UV Texture shader

[UV Coords]()

Returns texture coordinates or geometric s and t, depending on what is defined.


[UV Noise]()

Disturbs the incoming parametric s and t coordinates using anti aliased noise generated from the Surface Position input.


[UV Planar Project]()

Computes UV co-ordinates projected along a single axis, derived from the position of an object, and generates a mask relative to the projection axis.


[UV Position]()


[UV Project]()

Assigns texture coordinates based on the specified projection type.


[UV Transform]()

Transforms texture coordinates by the inverse of the matrix consisting of the translation, rotation, and scale amounts.


[UV Tri-planar Project]()

Projects texture maps along X, Y, and Z axes and blends them together at the seams.


[Unified Noise]()

Presents a unified interface and uniform output range for all the noise types available in VEX.


[Unified Noise]()

Presents a unified interface and uniform output range for all the noise types available in VEX.


[Unified Noise Static]()

Presents a unified interface and uniform output range for all the noise types available in VEX.

[Unique Value Count of Attribute]()

[Unique Values of Attribute]()


[VOP Force Global]()

Provides outputs that represent all the global variables for the Force VOP network type.


[VOP Force Output Variables]()

Simple output variable for VOP Force Networks.


[Vector Cast]()

Converts between different vector types.


[Vector To Float]()

Unpacks a vector into its three components.


[Vector To Quaternion]()

Takes an angle/axis vector and constructs the quaternion representing the rotation about that axis.


[Vector To Vector4]()

Converts a vector to a vector4.


[Vector to Matrix3]()

Converts rows values to a 3×3 matrix value.


[Vector to Vector2]()

Converts a vector to a vector2 and also returns the third component of the vector.


[Vector2 To Float]()

Unpacks a vector2 into its two components.


[Vector2 To Vector]()

Converts a vector2 to a vector.


[Vector2 To Vector4]()

Converts a pair of vector2s into a vector4.


[Vector2 to Matrix2]()

Converts rows values to a 2×2 matrix value.


[Vector4 to Float]()

Unpacks a vector4 into its four components.


[Vector4 to Matrix]()

Converts rows values to a 4×4 matrix value.


[Vector4 to Vector]()

Converts a vector4 to a vector and also returns the fourth component of the vector4.


[Vector4 to Vector2]()

Converts a vector4 to a pair of vector2s..


[Veins]()

Generates an anti-aliased vein pattern that can be used in any VEX context.


[Vex Volume Procedural]()

This procedural will generate a volume from a CVEX shader.


[Visualize]()

Exports a vis_ prefixed attribute.

[Volume Density to Opacity]()

Computes the opacity of a uniform volume given a density.


[Volume Gradient]()

Calculates the gradient of a volume primitive stored in a disk file.


[Volume Index]()

Gets the value of a voxel from a volume primitive stored in a disk file.


[Volume Index To Pos]()

Calculates the position of a voxel in a volume primitive stored in a disk file.


[Volume Index Vector]()

Gets the vector value of a voxel from a volume primitive stored in a disk file.

[Volume Model]()

A shading model for volume rendering.


[Volume Pos To Index]()

Calculates the voxel closest to a voxel of a volume primitive stored in a disk file.


[Volume Resolution]()

Gets the resolution of a volume primitive stored in a disk file.


[Volume Sample]()

Samples the value of a volume primitive stored in a disk file.


[Volume Sample Vector]()

Samples the vector value of a volume primitive stored in a disk file.


[Volume VOP Global Parameters]()

Provides outputs that represent all the global variables for the Volume VOP network type.


[Volume VOP Output Variables]()

Simple output variable for Volume VOP Networks.


[Voronoi Noise]()

Computes 1D, 3D, and 4D Voronoi noise, which is similar to Worley noise but has additional control over jittering.


[Wave Vector]()

Computes the wave vector for a given index in a grid of specified size.


[Waves]()

Simulates rolling waves with choppiness of various frequencies, and outputs the positional and normal displacements as well as the amount of displacement.

[Wire Pattern]()

Returns float between 0 and 1 which defines a wire grid pattern useful for simulating screens or visualizing parametric or texture coordinates.


[Worley Noise]()

Computes 1D, 3D, and 4D Worley noise, which is synonymous with "cell noise".


[XYZ Distance]()

Finds closest position on a primitive in a given geometry file.


[Xor]()

Performs a logical "xor" operation between its inputs.

[agentaddclip]()

Add a clip into an agent’s definition.


[argsort]()

Returns the indices of a sorted version of an array.
