

Adaptive Prune

Removes elements while trying to maintain the overall appearance.


Add

Creates Points or Polygons, or adds points/polys to an input.


Agent

Creates agent primitives.


Agent Clip

Adds new clips to agent primitives.


Agent Clip

Adds new clips to agent primitives.


Agent Clip Properties

Defines how agents' animation clips should be played back.


Agent Clip Transition Graph

Creates geometry describing possible transitions between animation clips.


Agent Collision Layer

Creates a new agent layer that is suitable for collision detection.


Agent Configure Joints

Creates point attributes that specify the rotation limits of an agent’s joints.


Agent Constraint Network

Builds a constraint network to hold an agent’s limbs together.


Agent Definition Cache

Writes agent definition files to disk.


Agent Edit

Edits properties of agent primitives.


Agent Layer

Adds a new layer to agent primitives.


Agent Look At

Adjusts the head of an agent to look at a specific object or position.


Agent Look At

Adjusts the head of an agent to look at a specific object or position.


Agent Prep

Adds various common point attributes to agents for use by other crowd nodes.


Agent Prep

Adds various common point attributes to agents for use by other crowd nodes.


Agent Proxy

Provides simple proxy geometry for an agent.


Agent Relationship

Creates parent-child relationships between agents.


Agent Terrain Adaptation

Adapts agents' legs to conform to terrain and prevent the feet from sliding.


Agent Transform Group

Adds new transform groups to agent primitives.


Agent Unpack

Extracts geometry from agent primitives.


Agent Vellum Unpack

Extracts geometry from agent primitives for a Vellum simulation.


Alembic

Loads the geometry from an Alembic scene archive (.abc) file into a geometry network.


Alembic Group

Creates a geometry group for Alembic primitives.


Alembic Primitive

Modifies intrinsic properties of Alembic primitives.


Alembic ROP output driver


Align

Aligns a group of primitives to each other or to an auxiliary input.


Assemble

Cleans up a series of break operations and creates the resulting pieces.


Attribute Blur

Blurs out (or "relaxes") points in a mesh or a point cloud.


Attribute Cast

Changes the size/precision Houdini uses to store an attribute.


Attribute Composite

Composites vertex, point, primitive, and/or detail attributes between two or more selections.


Attribute Copy

Copies attributes between groups of vertices, points, or primitives.


Attribute Create

Adds or edits user defined attributes.


Attribute Delete

Deletes point and primitive attributes.


Attribute Expression

Allows simple VEX expressions to modify attributes.


Attribute Fade

Fades a point attribute in and out over time.


Attribute Interpolate

Interpolates attributes within primitives or based on explicit weights.


Attribute Mirror

Copies and flips attributes from one side of a plane to another.


Attribute Noise

Adds noise to attributes of the incoming geometry.


Attribute Promote

Promotes or demotes attributes from one geometry level to another.


Attribute Randomize

Generates random attribute values of various distributions.


Attribute Rename

Renames or deletes point and primitive attributes.


Attribute Reorient

Modifies point attributes based on differences between two models.


Attribute String Edit

Edits string attribute values.


Attribute Swap

Copies, moves, or swaps the contents of attributes.


Attribute Transfer

Transfers vertex, point, primitive, and/or detail attributes between two models.

Attribute Transfer By UV

Transfers attributes between two geometries based on UV proximity.


Attribute VOP

Runs a VOP network to modify geometry attributes.


Attribute Wrangle

Runs a VEX snippet to modify attribute values.


Attribute from Map

Samples texture map information to a point attribute.


Attribute from Volume

Copies information from a volume onto the point attributes of another piece of geometry, with optional remapping.


Bake ODE

Converts primitives for ODE and Bullet solvers.

Bake Volume

Computes lighting values within volume primitives


Basis

Provides operations for moving knots within the parametric space of a NURBS curve or surface.


Bend

Applies deformations such as bend, taper, squash/stretch, and twist.


Blast

Deletes primitives, points, edges or breakpoints.


Blend Shapes

Computes a 3D metamorphosis between shapes with the same topology.


Blend Shapes

Computes a 3D metamorphosis between shapes with the same topology.


Block Begin

The start of a looping block.


Block Begin Compile

The start of a compile block.


Block End

The end/output of a looping block.


Block End Compile

The end/output of a compile block.


Bone Capture

Supports Bone Deform by assigning capture weights to bones.


Bone Capture Biharmonic

Supports Deform by assigning capture weights to points based on biharmonic functions on tetrahedral meshes.


Bone Capture Lines

Supports Bone Capture Biharmonic by creating lines from bones with suitable attributes.


Bone Capture Proximity

Supports Bone Deform by assigning capture weights to points based on distance to bones.


Bone Deform

Uses capture attributes created from bones to deform geometry according to their movement.


Bone Link

Creates default geometry for Bone objects.


Boolean

Combines two polygonal objects with boolean operators, or finds the intersection lines between two polygonal objects.


Boolean Fracture

Fractures the input geometry using cutting surfaces.


Bound

Creates a bounding box, sphere, or rectangle for the input geometry.


Box

Creates a cube or six-sided rectangular box.


Bulge

Deforms the points in the first input using one or more magnets from the second input.


Cache

Records and caches its input geometry for faster playback.


Cap

Closes open areas with flat or rounded coverings.


Capture Attribute Pack

Converts array attributes into a single index-pair capture attribute.


Capture Attribute Unpack

Converts a single index-pair capture attribute into per-point and detail array attributes.


Capture Correct

Adjusts capture regions and capture weights.


Capture Layer Paint

Lets you paint capture attributes directly onto geometry.


Capture Mirror

Copies capture attributes from one half of a symmetric model to the other.


Capture Override

Overrides the capture weights on individual points.


Capture Region

Supports Capture and Deform operation by creating a volume within which points are captured to a bone.


Carve

Slices, cuts or extracts points or cross-sections from a primitive.


Channel

Reads sample data from a chop and converts it into point positions and point attributes.


Circle

Creates open or closed arcs, circles and ellipses.


Clay

Lets you deform NURBS faces and NURBS surfaces by pulling points that lie directly on them.


Clean

Helps clean up dirty models.


Clip

Removes or groups geometry on one side of a plane, or creases geometry along a plane.


Cloth Capture

Captures low-res simulated cloth.


Cloth Deform

Deforms geometry captured by the Cloth Capture SOP.


Cloud

Creates a volume representation of source geometry.


Cloud Light

Fills a volume with a diffuse light.


Cloud Noise

Applies a cloud like noise to a Fog volume.


Cluster

Low-level machinery to cluster points based on their positions (or any vector attribute).


Cluster Points

Higher-level node to cluster points based on their positions (or any vector attribute).


Collision Source

Creates geometry and VDB volumes for use with DOPs collisions.


Color

Adds color attributes to geometry.


Comb

Adjust surface point normals by painting.


Connect Adjacent Pieces

Creates lines between nearby pieces.


Connectivity

Creates an attribute with a unique value for each set of connected primitives or points.


Control

Creates simple geometry for use as control shapes.


Convert

Converts geometry from one geometry type to another.


Convert HeightField

Converts a 2D height field to a 3D VDB volume, polygon surface, or polygon soup surface.


Convert Line

Converts the input geometry into line segments.


Convert Meta

Polygonizes metaball geometry.


Convert Tets

Generates the oriented surface of a tetrahedron mesh.


Convert VDB

Converts sparse volumes.


Convert VDB Points

Converts a Point Cloud into a VDB Points Primitive, or vice versa.


Convert Volume

Converts the iso-surface of a volume into a polygonal surface.


Convex Decomposition

Decomposes the input geometry into approximate convex segments.


Copy Stamp

Creates multiple copies of the input geometry, or copies the geometry onto the points of the second input.


Copy and Transform

Copies geometry and applies transformations to the copies.


Copy to Points

Copies the geometry in the first input onto the points of the second input.


Crease

Manually adds or removes a creaseweight attribute to/from polygon edges, for use with the Subdivide SOP.


Creep

Deforms and animates a piece of geometry across a surface.


Crowd Source

Populates a crowd of agent primitives.


Crowd Source

Creates crowd agents to be used with the crowd solver.


Curve

Creates polygonal, NURBS, or Bezier curves.


Curveclay

Deforms a spline surface by reshaping a curve on the surface.


Curvesect

Finds the intersections (or points of minimum distance) between two or more curves or faces.


DOP I/O

Imports fields from DOP simulations, saves them to disk, and loads them back again.


DOP Import Fields

Imports scalar and vector fields from a DOP simulation.


DOP Import Records

Imports option and record data from DOP simulations into points with point attributes.


DOP Network


Debris Source

Generates point emission sources for debris from separating fractured rigid body objects.


Deformation Wrangle

Runs a VEX snippet to deform geometry.


Delete

Deletes input geometry by group, entity number, bounding volume, primitive/point/edge normals, and/or degeneracy.


DeltaMush

Smooths out (or "relaxes") point deformations.


Detangle

Attempts to prevent collisions when deforming geometry.


Dissolve

Deletes edges from the input polygonal geometry merging polygons with shared edges.


Dissolve

Deletes points, primitives, and edges from the input geometry and repairs any holes left behind.


Divide

Divides, smooths, and triangulates polygons.


Dop Import

Imports and transforms geometry based on information extracted from a DOP simulation.


Draw Curve

Creates a curve based on user input in the viewport.


Draw Guides


Each

Culls the input geometry according to the specifications of the For Each SOP.


Edge Collapse

Collapses edges and faces to their centerpoints.


Edge Cusp

Sharpens edges by uniquing their points and recomputing point normals.


Edge Divide

Inserts points on the edges of polygons and optionally connects them.


Edge Flip

Flips the direction of polygon edges.


Edge Fracture

Cuts geometry along edges using guiding curves.


Edge Transport

Copies and optionally modifies attribute values along edges networks and curves.


Edit

Edits points, edges, or faces interactively.


Ends

Closes, opens, or clamps end points.


Enumerate

Sets an attribute on selected points or primitives to sequential numbers.


Error

Generates a message, warning, or error, which can show up on a parent asset.


Exploded View

Pushes geometry out from the center to create an exploded view.

Exploded View

Pushes geometry out from the center to create an exploded view.


Extract Centroid

Computes the centroid of each piece of the geometry.


Extract Transform

Computes the best-fit transform between two pieces of geometry.


Extrude

Extrudes geometry along a normal.


Extrude Volume

Extrudes surface geometry into a volume.


FEM Visualization


FLIP Source

Creates a surface or density VDB for sourcing FLIP simulations.


Facet

Controls the smoothness of faceting of a surface.


Falloff

Adds smooth distance attributes to geometry.


Filament Advect

Evolves polygonal curves as vortex filaments.


File

Reads, writes, or caches geometry on disk.


File Cache

Writes and reads geometry sequences to disk.


File Merge

Reads and collates data from disk.


Fillet

Creates smooth bridging geometry between two curves or surfaces.


Filmbox FBX ROP output driver


Find Shortest Path

Finds the shortest paths from start points to end points, following the edges of a surface.


Fit

Fits a spline curve to points, or a spline surface to a mesh of points.


Fluid Compress

Compresses the output of fluid simulations to decrease size on disk


Font

Creates 3D text from Type 1, TrueType and OpenType fonts.


Force

Uses a metaball to attract or repel points or springs.


Fractal

Creates jagged mountain-like divisions of the input geometry.


Fur

Creates a set of hair-like curves across a surface.


Fuse

Merges points.


Fuse

Merges or splits (uniques) points.


Glue Cluster

Adds strength to a glue constraint network according to cluster values.


Grain Source

Generates particles to be used as sources in a particle-based grain simulation.


Graph Color

Assigns a unique integer attribute to non-touching components.


Grid

Creates planar geometry.


Groom Blend

Blends the guides and skin of two grooms.


Groom Fetch

Fetches groom data from grooming objects.


Groom Pack

Packs the components of a groom into a set of named Packed Primitives for the purpose of writing it to disk.


Groom Switch

Switches between all components of two groom streams.


Groom Unpack

Unpacks the components of a groom from a packed groom.


Group

Generates groups of points, primitives, edges, or vertices according to various criteria.


Group Combine

Combines point groups, primitive groups, or edge groups according to boolean operations.


Group Copy

Copies groups between two pieces of geometry, based on point/primitive numbers.


Group Delete

Deletes groups of points, primitives, edges, or vertices according to patterns.


Group Expression

Runs VEX expressions to modify group membership.


Group Paint

Sets group membership interactively by painting.


Group Promote

Converts point, primitive, edge, or vertex groups into point, primitive, edge, or vertex groups.


Group Range

Groups points and primitives by ranges.


Group Rename

Renames groups according to patterns.


Group Transfer

Transfers groups between two pieces of geometry, based on proximity.


Guide Advect

Advects guide points through a velocity volume.


Guide Collide With VDB

Resolves collisions of guide curves with VDB signed distance fields.


Guide Deform

Deforms geometry with an animated skin and optionally guide curves.


Guide Groom

Allows intuitive manipulation of guide curves in the viewport.


Guide Group

Creates standard primitive groups used by grooming tools.


Guide Initialize

Quickly give hair guides some initial direction.


Guide Mask

Creates masking attributes for other grooming operations.


Guide Partition

Creates and prepares parting lines for use with hair generation.


Guide Skin Attribute Lookup

Looks up skin geometry attributes under the root point of guide curves.


Guide Tangent Space

Constructs a coherent tangent space along a curve.

Guide Transfer

Transfer hair guides between geometries.


Hair Card Generate

Converts dense hair curves to a polygon card, keeping the style and shape of the groom.


Hair Clump

Clumps guide curves together.


Hair Generate

Generates hair on a surface or from points.


Hair Growth Field

Generates a velocity field based on stroke primitives.


HeightField

Generates an initial heightfield volume for use with terrain tools.


HeightField Blur

Blurs a terrain height field or mask.


HeightField Clip

Limits height values to a certain minimum and/or maximum.


HeightField Copy Layer

Creates a copy of a height field or mask.


HeightField Crop

Extracts a square of a certain width/length from a larger height volume, or resizes/moves the boundaries of the height field.


HeightField Cutout by Object

Creates a cutout on a terrain based on geometry.


HeightField Distort by Layer

Displaces a height field by another field.


HeightField Distort by Noise

Advects the input volume through a noise pattern to break up hard edges and add variety.


HeightField Draw Mask

Lets you draw shapes to create a mask for height field tools.


HeightField Erode

Calculates thermal and hydraulic erosion over time (frames) to create more realistic terrain.


HeightField Erode

Calculates thermal and hydraulic erosion over time (frames) to create more realistic terrain.


HeightField Erode Hydro

Simulates the erosion from one heightfield sliding over another for a short time.


HeightField Erode Precipitation

Distributes water along a heightfield. Offers controls for adjusting the intensity, variability, and location of rainfall.


HeightField Erode Thermal

Calculates the effect of thermal erosion on terrain for a short time.


HeightField File

Imports a 2D image map from a file or compositing node into a height field or mask.


HeightField Flow Field

Generates flow and flow direction layers according to the input height layer.


HeightField Isolate Layer

Copies another layer over the mask layer, and optionally flattens the height field.


HeightField Layer

Composites together two height fields.


HeightField Layer Clear

Sets all values in a heightfield layer to a fixed value.


HeightField Layer Property

Sets the border voxel policy on a height field volume.


HeightField Mask by Feature

Creates a mask based on different features of the height layer.


HeightField Mask by Object

Creates a mask based some other geometry.


HeightField Mask by Occlusion

Creates a mask where the input terrain is hollow/depressed, for example riverbeds and valleys.


HeightField Noise

Adds vertical noise to a height field, creating peaks and valleys.


HeightField Output

Exports height and/or mask layers to disk as an image.


HeightField Paint

Lets you paint values into a height or mask field using strokes.


HeightField Patch

Patches features from one heightfield to another.


HeightField Pattern

Adds displacement in the form of a ramps, steps, stripes, Voronoi cells, or other patterns.


HeightField Project

Projects 3D geometry into a height field.


HeightField Quick Shade

Applies a material that lets you plug in textures for different layers.


HeightField Remap

Remaps the values in a height field or mask layer.


HeightField Resample

Changes the resolution of a height field.


HeightField Scatter

Scatters points across the surface of a height field.


HeightField Scatter

Scatters points across the surface of a height field.


HeightField Slump

Simulates loose material sliding down inclines and piling at the bottom.


HeightField Terrace

Creates stepped plains from slopes in the terrain.


HeightField Tile Splice

Stitches height field tiles back together.


HeightField Tile Split

Splits a height field volume into rows and columns.


HeightField Transform

Height field specific scales and offsets.


HeightField Visualize

Visualizes elevations using a custom ramp material, and mask layers using tint colors.


Hole

Makes holes in surfaces.


Inflate

Deforms the points in the first input to make room for the inflation tool.


Instance

Instances Geometry on Points.


Intersection Analysis

Creates points with attributes at intersections between a triangle and/or curve mesh with itself, or with an optional second set of triangles and/or curves.


Intersection Stitch

Composes triangle surfaces and curves together into a single connected mesh.


Invoke Compiled Block

Processes its inputs using the operation of a referenced compiled block.


IsoOffset

Builds an offset surface from geometry.


IsoSurface

Generates an isometric surface from an implicit function.


Join

The Join op connects a sequence of faces or surfaces into a single primitive that inherits their attributes.


Knife

Divides, deletes, or groups geometry based on an interactively drawn line.


L-System

Creates fractal geometry from the recursive application of simple rules.


Lattice

Deforms geometry based on how you reshape control geometry.


Lidar Import

Reads a lidar file and imports a point cloud from its data.


Line

Creates polygon or NURBS lines from a position, direction, and distance.


MDD

Animates points using an MDD file.


Magnet

Deforms geometry by using another piece of geometry to attract or repel points.


Match Axis

Aligns the input geometry to a specific axis.


Match Size

Resizes and recenters the geometry according to reference geometry.


Match Topology

Reorders the primitive and point numbers of the input geometry to match some reference geometry.


Material

Assigns one or more materials to geometry.


Measure

Measures area, volume, or curvature of individual elements or larger pieces of a geometry and puts the results in attributes.


Measure

Measures volume, area, and perimeter of polygons and puts the results in attributes.


Merge

Merges geometry from its inputs.


MetaGroups

Defines groupings of metaballs so that separate groupings are treated as separate surfaces when merged.


Metaball

Creates metaballs and meta-superquadric surfaces.


Mirror

Duplicates and mirrors geometry across a mirror plane.


Mountain

Displaces points along their normals based on fractal noise.


Mountain

Displaces points along their normals based on fractal noise.


Muscle Capture

Supports Muscle Deform by assigning capture weights to points based on distance away from given primitives


Muscle Deform

Deforms a surface mesh representing skin to envelop or drape over geometry representing muscles


Name

Creates a "naming" attribute on points or primitives allowing you to refer to them easily, similar to groups.


Normal

Computes surface normal attribute.


Null

Does nothing.


Object Merge

Merges geometry from multiple sources and allows you to define the manner in which they are grouped together and transformed.

Object_musclerig@musclerigstrokebuilder

Object_riggedmuscle@musclestrokebuilder

Assists the creation of a Muscle or Muscle Rig by allowing you to draw a stroke on a projection surface.


Ocean Evaluate

Deforms input geometry based on ocean "spectrum" volumes.


Ocean Evaluate

Deforms input geometry based on ocean "spectrum" volumes.


Ocean Foam

Generates particle-based foam


Ocean Source

Generates particles and volumes from ocean "spectrum" volumes for use in simulations


Ocean Source

Generates particles and volumes from ocean "spectrum" volumes for use in simulations


Ocean Spectrum

Generates volumes containing information for simulating ocean waves.


Ocean Waves

Instances individual waveforms onto input points and generated points.


OpenCL

Executes an OpenCL kernel on geometry.


Output

Marks the output of a sub-network.


Pack

Packs geometry into an embedded primitive.


Pack Points

Packs points into a tiled grid of packed primitives.


Packed Disk Edit

Editing Packed Disk Primitives.


Packed Edit

Editing Packed Primitives.


Paint

Lets you paint color or other attributes on geometry.


Paint Color Volume

Creates a color volume based on drawn curve


Paint Fog Volume

Creates a fog volume based on drawn curve


Paint SDF Volume

Creates an SDF volume based on drawn curve


Particle Fluid Surface

Generates a surface around the particles from a particle fluid simulation.


Particle Fluid Tank

Creates a set of regular points filling a tank.


Partition

Places points and primitives into groups based on a user-supplied rule.


Peak

Moves primitives, points, edges or breakpoints along their normals.


Planar Patch

Creates a planar polygonal patch.


Planar Patch from Curves

Fills in a 2d curve network with triangles.


Planar Pleat

Deforms flat geometry into a pleat.


Platonic Solids

Creates platonic solids of different types.


Point

Manually adds or edits point attributes.


Point Cloud Iso

Constructs an iso surface from its input points.


Point Deform

Deforms geometry on an arbitrary connected point mesh.


Point Generate

Creates new points, optionally based on point positions in the input geometry.


Point Jitter

Jitters points in random directions.


Point Relax

Moves points with overlapping radii away from each other, optionally on a surface.


Point Replicate

Generates a cloud of points around the input points.


Point Velocity

Computes and manipulates velocities for points of a geometry.


Points from Volume

Creates set of regular points filling a volume.


Poly Bridge

Creates flat or tube-shaped polygon surfaces between source and destination edge loops, with controls for the shape of the bridge.


Poly Expand 2D

Creates offset polygonal geometry for planar polygonal graphs.


Poly Extrude

Extrudes polygonal faces and edges.


PolyBevel

Creates straight, rounded, or custom fillets along edges and corners.


PolyBevel

Bevels points and edges.


PolyCut

Breaks curves where an attribute crosses a threshold.


PolyDoctor

Helps repair invalid polygonal geometry, such as for cloth simulation.


PolyExtrude

Extrudes polygonal faces and edges.


PolyFill

Fills holes with polygonal patches.


PolyFrame

Creates coordinate frame attributes for points and vertices.


PolyLoft

Creates new polygons using existing points.


PolyPatch

Creates a smooth polygonal patch from primitives.


PolyPath

Cleans up topology of polygon curves.


PolyReduce

Reduces the number of polygons in a model while retaining its shape. This node preserves features, attributes, textures, and quads during reduction.


PolySoup

Combines polygons into a single primitive that can be more efficient for many polygons


PolySpline

The PolySpline SOP fits a spline curve to a polygon or hull and outputs a polygonal approximation of that spline.


PolySplit

Divides an existing polygon into multiple new polygons.


PolySplit

Divides an existing polygon into multiple new polygons.


PolyStitch

Stitches polygonal surfaces together, attempting to remove cracks.


PolyWire

Constructs polygonal tubes around polylines, creating renderable geometry with smooth bends and intersections.


Pose-Space Deform

Interpolates between a set of pose-shapes based on the value of a set of drivers.


Pose-Space Deform Combine

Combine result of Pose-Space Deform with rest geometry.

Pose-Space Edit

Packs geometry edits for pose-space deformation.

Pose-Space Edit Configure

Creates common attributes used by the Pose-Space Edit SOP.


Primitive

Edits primitive, primitive attributes, and profile curves.


Primitive Split

Takes a primitive attribute and splits any points whose primitives differ by more than a specified tolerance at that attribute.


Profile

Extracts or manipulates profile curves.


Project

Creates profile curves on surfaces.


Pyro Source

Creates points for sourcing pyro and smoke simulations.


Python

Runs a Python snippet to modify the incoming geometry.


RBD Cluster

Combines fractured pieces or constraints into larger clusters.


RBD Constraint Properties

Creates attributes describing rigid body constraints.


RBD Constraints From Curves

Creates rigid body constraint geometry from curves drawn in the viewport.


RBD Constraints From Lines

Creates rigid body constraint geometry from interactively drawn lines in the viewport.


RBD Constraints From Rules

Creates rigid body constraint geometry from a set of rules and conditions.


RBD Interior Detail

Creates additional detail on the interior surfaces of fractured geometry.


RBD Material Fracture

Fractures the input geometry based on a material type.


RBD Material Fracture

Fractures the input geometry based on a material type.


RBD Pack

Packs RBD geometry, constraints, and proxy geometry into a single geometry.


RBD Paint

Paints values onto geometry or constraints using strokes.


RBD Unpack

Unpacks an RBD setup into three outputs.


RMan Shader

Attaches RenderMan shaders to groups of faces.


ROP Geometry Output


Rails

Generates surfaces by stretching cross-sections between two guide rails.


Ray

Projects one surface onto another.


Refine

Increases the number of points/CVs in a curve or surface without changing its shape.


Reguide

Scatters new guides, interpolating the properties of existing guides.


Remesh

Recreates the shape of the input surface using "high-quality" (nearly equilateral) triangles.


Repack

Repacks geometry as an embedded primitive.


Resample

Resamples one or more curves or surfaces into even length segments.


Rest Position

Sets the alignment of solid textures to the geometry so the texture stays put on the surface as it deforms.


Retime

Retimes the time-dependent input geometry.


Reverse

Reverses or cycles the vertex order of faces.


Revolve

Revolves a curve around a center axis to sweep out a surface.


Rewire Vertices

Rewires vertices to different points specified by an attribute.


Ripple

Generates ripples by displacing points along the up direction specified.


Scatter

Scatters new points randomly across a surface or through a volume.


Script

Runs scripts when cooked.


Sculpt

Lets you interactively reshape a surface by brushing.


Sequence Blend

Morphs though a sequence of 3D shapes, interpolating geometry and attributes.


Sequence Blend

Sequence Blend lets you do 3D Metamorphosis between shapes and Interpolate point position, colors…


Shape Diff

Computes the post-deform or pre-deform difference of two geometries with similar topologies.


Shrinkwrap

Computes the convex hull of the input geometry and moves its polygons inwards along their normals.


Shrinkwrap

Takes the convex hull of input geometry and moves its polygons inwards along their normals.


Skin

Builds a skin surface between any number of shape curves.


Sky

Creates a sky filled with volumentric clouds


Smooth

Smooths out (or "relaxes") polygons, meshes and curves without increasing the number of points.


Smooth

Smooths out (or "relaxes") polygons, meshes and curves without increasing the number of points.


Soft Peak

Moves the selected point along its normal, with smooth rolloff to surrounding points.


Soft Transform

Moves the selected point, with smooth rolloff to surrounding points.


Solid Conform

Creates a tetrahedral mesh that conforms to a connected mesh as much as possible.


Solid Embed

Creates a simple tetrahedral mesh that covers a connected mesh.


Solid Fracture

Creates a partition of a tetrahedral mesh that can be used for finite-element fracturing.


Solver

Allows running a SOP network iteratively over some input geometry, with the output of the network from the previous frame serving as the input for the network at the current frame.


Sort

Reorders points and primitives in different ways, including randomly.


Sphere

Creates a sphere or ovoid surface.


Split

Splits primitives or points into two streams.


Spray Paint

Spray paints random points onto a surface.


Sprite

A SOP node that sets the sprite display for points.


Starburst

Insets points on polygonal faces.


Stash

Caches the input geometry in the node on command, and then uses it as the node’s output.


Stitch

Stretches two curves or surfaces to cover a smooth area.


Stroke

Low level tool for building interactive assets.


Subdivide

Subdivides polygons into smoother, higher-resolution polygons.


Subnetwork

The Subnet op is essentially a way of creating a macro to represent a collection of ops as a single op in the Network Editor.


Super Quad

Generates an isoquadric surface.


Surfsect

Trims or creates profile curves along the intersection lines between NURBS or bezier surfaces.


Sweep

Creates a surface by sweeping cross-sections along a backbone curve.


Switch

Switches between network branches based on an expression or keyframe animation.


TOP SOP

Sends input geometry to a TOP subnet and retrieves the output geometry.


Table Import

Reads a CSV file creating point per row.


Test Geometry: Crag

Creates a rock creature, which can be used as test geometry.


Test Geometry: Pig Head

Creates a pig head, which can be used as test geometry..


Test Geometry: Rubber Toy

Creates a rubber toy, which can be used as test geometry.


Test Geometry: Shader Ball

Creates a shader ball, which can be used to test shaders.


Test Geometry: Squab

Creates a squab, which can be used as test geometry.


Test Geometry: Tommy

Creates a soldier, which can be used as test geometry.


Test Simulation: Crowd Transition

Provides a simple crowd simulation for testing transitions between animation clips.


Test Simulation: Ragdoll

Provides a simple Bullet simulation for testing the behavior of a ragdoll.


Tet Partition

Partitions a given tetrahedron mesh into groups of tets isolated by a given polygon mesh


Tetrahedralize

Performs variations of a Delaunay Tetrahedralization.


TimeShift

Cooks the input at a different time.

Toon Shader Attributes

Sets attributes used by the Toon Color Shader and Toon Outline Shader.


TopoBuild

Lets you interactively draw a reduced quad mesh automatically snapped to existing geometry.


Torus

Creates a torus (doughnut) shaped surface.


Trace

Traces curves from an image file.


Trail

Creates trails behind points.


Transform

The Transform operation transforms the source geometry in "object space" using a transformation matrix.


Transform Axis

Transforms the input geometry relative to a specific axis.


Transform By Attribute

Transforms the input geometry by a point attribute.


Transform Pieces

Transforms input geometry according to transformation attributes on template geometry.


Tri Bezier

Creates a triangular Bezier surface.


TriDivide

Refines triangular meshes using various metrics.


Triangulate 2D

Connects points to form well-shaped triangles.


Trim

Trims away parts of a spline surface defined by a profile curve or untrims previous trims.


Tube

Creates open or closed tubes, cones, or pyramids.


UV Autoseam

Generates an edge group representing suggested seams for flattening a polygon model in UV space.


UV Brush

Adjusts texture coordinates in the UV viewport by painting.


UV Edit

Lets you interactively move UVs in the texture view.


UV Flatten

Creates flattened pieces in texture space from 3D geometry.


UV Flatten

Creates flattened pieces in texture space from 3D geometry.


UV Fuse

Merges UVs.


UV Layout

Packs UV islands efficiently into a limited area.


UV Pelt

Relaxes UVs by pulling them out toward the edges of the texture area.


UV Project

Assigns UVs by projecting them onto the surface from a set direction.


UV Quick Shade

Applies an image file as a textured shader to a surface.


UV Texture

Assigns texture UV coordinates to geometry for use in texture and bump mapping.


UV Transform

Transforms UV texture coordinates on the source geometry.


UV Transform

Transforms UV texture coordinates on the source geometry.


UV Unwrap

Separates UVs into reasonably flat, non-overlapping groups.


Unix

Processes geometry using an external program.


Unpack

Unpacks packed primitives.


Unpack Points

Unpacks points from packed primitives.


VDB

Creates one or more empty/uniform VDB volume primitives.


VDB Activate

Activates voxel regions of a VDB for further processing.


VDB Activate SDF

Expand or contract signed distance fields stored on VDB volume primitives.


VDB Advect

Moves VDBs in the input geometry along a VDB velocity field.


VDB Advect Points

Moves points in the input geometry along a VDB velocity field.


VDB Analysis

Computes an analytic property of a VDB volumes, such as gradient or curvature.


VDB Clip

Clips VDB volume primitives using a bounding box or another VDB as a mask.


VDB Combine

Combines the values of two aligned VDB volumes in various ways.


VDB Diagnostics

Tests VDBs for Bad Values and Repairs.


VDB Fracture

Cuts level set VDB volume primitives into multiple pieces.


VDB LOD

Build an LOD Pyramid from a VDB.


VDB Morph SDF

Blends between source and target SDF VDBs.


VDB Occlusion Mask

Create a mask of the voxels in shadow from a camera for VDB primitives.


VDB Points Delete

Deletes points inside of VDB Points primitives.


VDB Points Group

Manipulates the Internal Groups of a VDB Points Primitive.


VDB Potential Flow

Computes the steady-state air flow around VDB obstacles.


VDB Project Non-Divergent

Removes divergence from a Vector VDB.


VDB Renormalize SDF

Fixes signed distance fields stored in VDB volume primitives.


VDB Resample

Re-samples a VDB volume primitive into a new orientation and/or voxel size.


VDB Reshape SDF

Reshapes signed distance fields in VDB volume primitives.


VDB Segment by Connectivity

Splits SDF VDBs into connected components.


VDB Smooth

Smooths out the values in a VDB volume primitive.


VDB Smooth SDF

Smooths out SDF values in a VDB volume primitive.


VDB Topology to SDF

Creates an SDF VDB based on the active set of another VDB.


VDB Vector Merge

Merges three scalar VDB into one vector VDB.


VDB Vector Split

Splits a vector VDB primitive into three scalar VDB primitives.


VDB Visualize Tree

Replaces a VDB volume with geometry that visualizes its structure.


VDB from Particle Fluid

Generates a signed distance field (SDF) VDB volume representing the surface of a set of particles from a particle fluid simulation.


VDB from Particles

Converts point clouds and/or point attributes into VDB volume primitives.


VDB from Polygons

Converts polygonal surfaces and/or surface attributes into VDB volume primitives.


VDB to Spheres

Fills a VDB volume with adaptively-sized spheres.


Vellum Configure Grain

Configures geometry for Vellum Grain constraints.


Vellum Constraints

Configure constraints on geometry for the Vellum solvers.


Vellum Drape

Vellum solver setup to pre-roll fabric to drape over characters.


Vellum I/O

Packs Vellum simulations, saves them to disk, and loads them back again.


Vellum Pack

Packs Vellum geometry and constraints into a single geometry.


Vellum Post-Process

Applies common post-processing effects to the result of Vellum solves.


Vellum Rest Blend

Blends the current rest values of constraints with a rest state calculated from external geometry.


Vellum Solver

Runs a dynamic Vellum simulation.


Vellum Unpack

Unpacks a Vellum simulation into two outputs.

Verify BSDF

Verify that a bsdf conforms to the required interface.


Vertex

Manually adds or edits attributes on vertices (rather than on points).


Vertex Split

Takes a vertex attribute and splits any point whose vertices differ by more than a specified tolerance at that attribute.


Visibility

Shows/hides primitives in the 3D viewer and UV editor.


Visualize

Lets you attach visualizations to different nodes in a geometry network.


Volume

Creates a volume primitive.


Volume Analysis

Computes analytic properties of volumes.


Volume Arrival Time

Computes a speed-defined travel time from source points to voxels.


Volume Blur

Blurs the voxels of a volume.


Volume Bound

Bounds voxel data.


Volume Break

Cuts polygonal objects using a signed distance field volume.


Volume Compress

Re-compresses Volume Primitives.


Volume Convolve 3×3×3

Convolves a volume by a 3×3×3 kernel.


Volume FFT

Compute the Fast Fourier Transform of volumes.


Volume Feather

Feathers the edges of volumes.


Volume Merge

Flattens many volumes into one volume.


Volume Mix

Combines the scalar fields of volume primitives.

Volume Optical Flow

Translates the motion between two "image" volumes into displacement vectors.

Volume Patch

Fill in a region of a volume with features from another volume.


Volume Ramp

Remaps a volume according to a ramp.


Volume Rasterize

Rasterizes into a volume.


Volume Rasterize Attributes

Samples point attributes into VDBs.


Volume Rasterize Curve

Converts a curve into a volume.


Volume Rasterize Hair

Converts fur or hair to a volume for rendering.


Volume Rasterize Particles

Converts a point cloud into a volume.


Volume Rasterize Points

Converts a point cloud into a volume.


Volume Reduce

Reduces the values of a volume into a single number.


Volume Resample

Resamples the voxels of a volume to a new resolution.


Volume Resize

Resizes the bounds of a volume without changing voxels.


Volume SDF

Builds a Signed Distance Field from an isocontour of a volume.


Volume Slice

Extracts 2d slices from volumes.


Volume Splice

Splices overlapping volume primitives together.


Volume Stamp

Stamps volumes instanced on points into a single target volume.


Volume Surface

Adaptively surfaces a volume hierarchy with a regular triangle mesh.


Volume Trail

Computes a trail of points through a velocity volume.


Volume VOP

Runs CVEX on a set of volume primitives.


Volume Velocity

Computes a velocity volume.


Volume Velocity from Curves

Generates a volume velocity field using curve tangents.


Volume Velocity from Surface

Generates a velocity field within a surface geometry.


Volume Visualization

Adjusts attributes for multi-volume visualization.


Volume Wrangle

Runs a VEX snippet to modify voxel values in a volume.


Volume from Attribute

Sets the voxels of a volume from point attributes.


Voronoi Fracture

Fractures the input geometry by performing a Voronoi decomposition of space around the input cell points


Voronoi Fracture

Fractures the input geometry by performing a Voronoi decomposition of space around the input cell points


Voronoi Fracture Points

Given an object and points of impact on the object, this SOP generates a set of points that can be used as input to the Voronoi Fracture SOP to simulate fracturing the object from those impacts.


Voronoi Split

Cuts the geometry into small pieces according to a set of cuts defined by polylines.


Vortex Force Attributes

Creates the point attributes needed to create a Vortex Force DOP.


Whitewater Source

Generates volumes to be used as sources in a whitewater simulation.


Whitewater Source

Generates emission particles and volumes to be used as sources in a Whitewater simulation.


Winding Number

Computes generalized winding number of surface at query points.


Wire Blend

Morphs between curve shapes while maintaining curve length.


Wire Capture

Captures surfaces to a wire, allowing you to edit the wire to deform the surface.


Wire Deform

Deforms geometry captured to a curve via the Wire Capture node.


Wire Transfer

Transfers the shape of one curve to another.


Wireframe

Constructs polygonal tubes around polylines, creating renderable geometry.


glTF ROP output driver


posescope

Assigns channel paths and/or pickscripts to geometry.
