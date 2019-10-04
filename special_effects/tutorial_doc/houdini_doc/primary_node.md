
[Add]()----Creates Points or Polygons, or adds points/polys to an input.

[Agent]()----Creates agent primitives.

[Agent Clip]()----Adds new clips to agent primitives.

[Agent Layer]()----Adds a new layer to agent primitives.

[Agent Unpack]()----Extracts geometry from agent primitives.

[Alembic]()----Loads the geometry from an Alembic scene archive (.abc) file into a geometry network.

[Alembic Group]()----Creates a geometry group for Alembic primitives.

[Alembic Primitive]()----Modifies intrinsic properties of Alembic primitives.

[Align]()----Aligns a group of primitives to each other or to an auxiliary input.

[Attribute Cast]()----Changes the size/precision Houdini uses to store an attribute.

[Attribute Composite]()----Composites vertex, point, primitive, and/or detail attributes between two or more selections.

[Attribute Copy]()----Copies attributes between groups of vertices, points, or primitives.

[Attribute Create]()----Adds or edits user defined attributes.

[Attribute from Volume]()----Copies information from a volume onto the point attributes of another piece of geometry, with optional remapping.

[Attribute Interpolate]()----Interpolates attributes within primitives or based on explicit weights.

[Attribute Mirror]()----Copies and flips attributes from one side of a plane to another.

[Attribute Promote]()----Promotes or demotes attributes from one geometry level to another.

[Attribute Rename]()----Renames or deletes point and primitive attributes.

[Attribute Reorient]()----Modifies point attributes based on differences between two models.

[Attribute String Edit]()----Edits string attribute values.

[Attribute Swap]()----Copies, moves, or swaps the contents of attributes.

[Attribute Transfer]()----Transfers vertex, point, primitive, and/or detail attributes between two models.

[Bake ODE]()----Converts primitives for ODE and Bullet solvers.

[Bake Volume]()----Computes lighting values within volume primitive

[Basis]()----Provides operations for moving knots within the parametric space of a NURBS curve or surface.

[Blast]()----Deletes primitives, points, edges or breakpoints.

[Blend Shapes]()----Computes a 3D metamorphosis between shapes with the same topology.

[Block Begin]()----The start of a looping block.

[Block Begin Compile]()----The start of a compile block.

[Block End]()----The end/output of a looping block.

[Block End Compile]()----The end/output of a compile block.

[Bone Capture]()----Supports Bone Deform by assigning capture weights to bones.

[Bone Capture Biharmonic]()----Supports Deform by assigning capture weights to points based on biharmonic functions on tetrahedral meshes.

[Bone Capture Lines]()----Supports Bone Capture Biharmonic by creating lines from bones with suitable attributes.

[Bone Capture Proximity]()----Supports Bone Deform by assigning capture weights to points based on distance to bones.

[Bone Deform]()----Uses capture attributes created from bones to deform geometry according to their movement.

[Bone Link]()----Creates default geometry for Bone objects.

[Boolean]()----Combines two polygonal objects with boolean operators, or finds the intersection lines between two polygonal objects.

[Bound]()----Creates a bounding box, sphere, or rectangle for the input geometry.

[Box]()----Creates a cube or six-sided rectangular box.

[Bulge]()----Deforms the points in the first input using one or more magnets from the second input.

[Cache]()----Records and caches its input geometry for faster playback.

[Cap]()----Closes open areas with flat or rounded coverings.

[Capture Attribute Pack]()----Converts array attributes into a single index-pair capture attribute.

[Capture Attribute Unpack]()----Converts a single index-pair capture attribute into per-point and detail array attributes.

[Capture Correct]()----Adjusts capture regions and capture weights.

[Capture Layer Paint]()----Lets you paint capture attributes directly onto geometry.

[Capture Mirror]()----Copies capture attributes from one half of a symmetric model to the other.

[Capture Override]()----Overrides the capture weights on individual points.

[Capture Region]()----Supports Capture and Deform operation by creating a volume within which points are captured to a bone.

[Carve]()----Slices, cuts or extracts points or cross-sections from a primitive.

[Circle]()----Creates open or closed arcs, circles and ellipses.

[Connectivity]()----Creates an attribute with a unique value for each set of connected primitives or points.

[Control]()----Creates simple geometry for use as control shapes.

[Copy Stamp]()----Creates multiple copies of the input geometry, or copies the geometry onto the points of the second input.

[Copy to Points]()----Copies the geometry in the first input onto the points of the second input.

[Delete]()----Deletes input geometry by group, entity number, bounding volume, primitive/point/edge normals, and/or degeneracy.

[Divide]()----Divides, smooths, and triangulates polygons.

[Dop Import]()----Imports and transforms geometry based on information extracted from a DOP simulation.

[Edit]()----Edits points, edges, or faces interactively.

[Facet]()----Controls the smoothness of faceting of a surface.

[Font]()----Creates 3D text from Type 1, TrueType and OpenType fonts.

[Group]()----Generates groups of points, primitives, edges, or vertices according to various criteria.

[Group Delete]()----Deletes groups of points, primitives, edges, or vertices according to patterns.

[Group Promote]()----Converts point, primitive, edge, or vertex groups into point, primitive, edge, or vertex groups.

[Invoke Compiled Block]()----Processes its inputs using the operation of a referenced compiled block.

[Merge]()----Merges geometry from its inputs.

[Name]()----Creates a "naming" attribute on points or primitives allowing you to refer to them easily, similar to groups.

[Normal]()----Computes surface normal attribute.

[Null]()----Does nothing.

[Output]()----Marks the output of a sub-network.

[OpenCL]()----Executes an OpenCL kernel on geometry.

[Pack]()----Packs geometry into an embedded primitive.

[Pack Points]()----Packs points into a tiled grid of packed primitives.

[Point]()----Manually adds or edits point attributes.

[Point Generate]()----Creates new points, optionally based on point positions in the input geometry.

[Point Relax]()----Moves points with overlapping radii away from each other, optionally on a surface.

[Poly Extrude]()----Extrudes polygonal faces and edges.

[PolyBevel]()----Creates straight, rounded, or custom fillets along edges and corners.

[Python]()----Runs a Python snippet to modify the incoming geometry.

[Ray]()----Projects one surface onto another.

[Rest Position]()----Sets the alignment of solid textures to the geometry so the texture stays put on the surface as it deforms.

[Rewire Vertices]()----Rewires vertices to different points specified by an attribute.

[Sequence Blend]()----Sequence Blend lets you do 3D Metamorphosis between shapes and Interpolate point position, colors…

[Sphere]()----Creates a sphere or ovoid surface.

[Split]()----Splits primitives or points into two streams.

[Switch]()----Switches between network branches based on an expression or keyframe animation.

[TimeShift]()----Cooks the input at a different time.

[Torus]()----Creates a torus (doughnut) shaped surface.

[Transform]()----The Transform operation transforms the source geometry in "object space" using a transformation matrix.

[Transform By Attribute]()----Transforms the input geometry by a point attribute.

[Tube]()----Creates open or closed tubes, cones, or pyramids.

[Unpack]()----Unpacks packed primitives.

[Unpack Points]()----Unpacks points from packed primitives.

[UV Texture]()----Assigns texture UV coordinates to geometry for use in texture and bump mapping.

[UV Transform]()----Transforms UV texture coordinates on the source geometry.

