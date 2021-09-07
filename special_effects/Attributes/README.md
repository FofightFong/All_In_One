# 属性变量

https://www.johnkunz.com/vex

###   Attribute Data Types

To manually specify the VEX datatype for an attribute, add a character representing the type before the @ sign.
```
string                  s@name
int                     i@name
float                   f@name
vector2   (2 floats)    u@name
vector    (3 floats)    v@name
vector4   (4 floats)    p@name
matrix2   (2×2 floats)  2@name
matrix3   (3×3 floats)  3@name
matrix    (4×4 floats)  4@name
```
### Global Variables

A list of variables available in wrangles. The type indicator isn't needed, but is included as a reminder.

f@Frame     //The current floating frame number, equivalent to the $FF Hscript variable
f@Time      //The current time in seconds, equivalent to the $T Hscript variable 
i@SimFrame  //The integer simulation timestep number ($SF), only present in DOP contexts.
f@SimTime   //The simulation time in seconds ($ST), only present in DOP contexts. 
f@TimeInc   //The timestep currently being used for simulation or playback.

// Available in Attribute Wrangle
v@P         //The position of the current element.
i@ptnum     //The point number attached to the currently processed element.
i@vtxnum    //The linear number of the currently processed vertex.
i@primnum   //The primitive number attached to the currently processed element.
i@elemnum   //The index number of the currently processed element.
i@numpt     //The total number of points in the geometry.
i@numvtx    //The number of vertices in the primitive of the currently processed element. 
i@numprim   //The total number of primitives in the geometry. 
i@numelem   //The total number of elements being processed.  

// Available in Volume Wrangle
v@P                     //The position of the current voxel.
f@density               //The value of the density field at the current voxel location. 
v@center                //The center of the current volume.
v@dPdx, v@dPdy, v@dPdz  //These vectors store the change in P that occurs in the x, y, and z voxel indices.
i@ix, i@iy, i@iz        //Voxel indices. For dense volumes (non-VDB) these range from 0 to resolution-1.
i@resx, i@resy, i@resz  //The resolution of the current volume.
Common Geometry Attributes
Frequently used attributes. Houdini knows to cast these to the appropriate VEX datatype.  Type indicator isn't needed, but included as a reminder.

v@P          // Point position.  Used this to lay out points in 3D space.
v@N          // Surface or curve normal.  Houdini will compute the normal if this attribute does not exist.
v@uv         // UV texture coordinates for this point/vertex.
v@Cd         // Diffuse color override.  The viewport uses this to color OpenGL geometry.
f@pscale     // Particle radius size.  Uniform scale.  Set display particles as 'Discs' to visualize.
v@v          // Point velocity.  The direction and speed of movement in units per second.
i@id         // A unique indexing number that remains the same throughout time.  Used to match elements between frames.
v@rest       // Used by procedural patterns and textures to stick on deforming and animated surfaces.
s@name       // A unique name identifying which primitives belong to which piece.  Also used to label volumes.
v@up         // Up vector.  The up direction for local space, typically (0, 1, 0).
v@scale      // Vector scale.  Allows directional scaling or stretching (in one direction).
p@orient     // The local orientation of the point (represented as a quaternion).
p@rot        // Additional rotation to be applied after orient, N, and up attributes.
f@width      // Thickness of curves.  Enable 'Shade Open Curves In Viewport' on the object node to visualize.
f@Alpha      // Alpha transparency override.  The viewport uses this to set the alpha of OpenGL geometry.
s@instance   // Path of an object node to be instanced at render time.
f@Pw         // Spline weight.  Mostly depreciated at this point.
DOP Particle Attributes
A particle system is first and foremost driven by attributes. Here are some of the attributes used.

f@age       // Time in seconds since the particle was born.
f@life      // Time in seconds the particle is allowed to live. When f@age>f@life, i@dead will be set to 1.
f@nage      // Normalized age, f@age divided by f@life.  Implicit attribute, you cannot write to this.
i@dead      // Whether a particle is living (0) or dead (1).  A dead particle is deleted in the Reaping stage.
i@id        // A unique id for the particle that remains the same throughout a single simulation.

i@stopped   // Whether a particle is moving (0) or stopped (1).
i@stuck     // Whether a particle is free (0) or stuck (1).
i@sliding   // Whether a particle is free (0) or sliding along a surface (1).
f@cling     // Force applied to sliding paritcles inwards (according to the collision's surface normal).
s@pospath   // The path to the object that the particle is colliding with.
i@posprim   // Which collision primitive in the path geometry whose position we wish to refer to.
v@posuv     // Parametric uv on the collision primitive.

i@hittotal  // The cumulative total of all hits for the particle (only incremented once per timestep).
i@has_pprevious // This is set to 1 if v@pprevious contains valid values.
v@pprevious // Stores the position of the particle on the previous frame.  Used for collision detection.
i@hitnum    // The number of times the particle collided in the last POP Collision Detect.
s@hitpath   // The path to the object that was hit. A path to a file on disk or an op: path.
i@hitprim   // The primitive hit. Could be -1 if it the collision detector couldn’t figure out which prim.
v@hituv     // The parametric UV space on the primitive.
v@hitpos    // Where the hit actually occurred.  Useful if the colliding object was moving.
v@hitnml    // The normal of the surface at the time of the collision.
v@hitv      // The velocity of the surface at the time of the collision.
f@hittime   // When the collision occurred, that could be within a frame.
f@hitimpulse// Records how much of an impulse was needed for the collision resolution.  varies with timestep.
f@bounce    // When particles bounce off another object, this controls how much energy they keep.
f@bounceforward // Controls how much energy they keep in the tangential direction.
f@friction  // When particles bounce, they are slowed down proportional to how hard they hit.
s@collisionignore   // Objects that match this pattern will not be collided.

f@force     // Forces on the particle for this frame.
f@mass      // Inertia of the particle.
v@spinshape // This is multiplied by f@pscale to determine the shape of the particle for rotational inertia.
f@drag      // How much the particle is effected by any wind effects.
f@dragexp   // Ranges from 1 to 2, default is set on the solver.  Used for both angular and linear drag.
v@dragshape // How much the particle is dragged in each of its local axes.
v@dragcenter// If specified, drag forces will also generate torques on the particle.
v@targetv   // The local wind speed. Thought of as the goal, or target, velocity for the particle.
f@airresist // How important it is to match the wind speed.  Thickness of the air.
f@speedmin  // Minumum speed, in units per second, that a particle can move.
f@speedmax  // Maximum speed, in units per second, that a particle can move.

p@orient    // Orientation of the particle.  Used for figuring out 'local' forces.
v@w         // Angular speed of the particle.  A vector giving the rotation axis.
v@torque    // The equivalent of force for spins. No inertial tensor (the equivalent of mass) is supported.
v@targetw   // The goal spin direction and speed for this particle.
f@spinresist// How important it is to match the targetw.
f@spinmin   // Minumum speed in radians per second that a particle can spin.
f@spinmax   // Maximum speed in radians per second that a particle can spin.
DOP Grains Attributes
Particles under control of POP Grains have the ispbd attribute set to 1. This causes them to not perform normal movement update in the POP Solver, as the actual motion update is done in this node.

i@ispbd     // A value of 1 causes the particle to behave as grains.
f@pscale    // Used to determine the radius of each particle.
f@repulsionweight   // How much the particle collision forces are weighted.
f@repulsionstiffness// How strongly particles are kept apart.  Higher values result in less bouncy repulsion.
f@attractionweight  // How much the particles will naturally stick together when close.
f@attractionstiffness   // How strongly nearby particles stick to each other.
v@targetP   // Particles are constrained to this location.
f@targetweight      // The weight of the v@targetP constraints.
f@targetstiffness   // The stiffness with which particles are fixed to their v@targetP attribute.

f@restlength// Particles connected by polylines will be forced to maintain this distance (prim attribute).
f@constraintweight  // Scale, on a per-particle basis of the constraint force.
f@constraintstiffness   // This controls the stiffness on a per-particle basis.
f@strain    // This primitive attribute records how much the constraint is stretched.
f@strength  // If f@strain exceeds this primitive attribute, the constraint will be removed.
DOP Packed RBD Attributes
The Bullet Solver uses several point attributes to store the properties of each piece of a packed object.

i@active    // Specifies whether the object is able to react to other objects.
i@animated  // Specifies whether the transform should be updated from its SOP geometry at each timestep.
i@deforming // Specifies whether the collision shape should be rebuilt from its SOP geometry each timestep.

f@bounce    // The elasticity of the object.
i@bullet_add_impact // Impacts that occur during the sim will be recorded in the Impacts or Feedback data.
i@bullet_ignore     // Specifies whether the object should be completely ignored by the Bullet solver.
f@bullet_angular_sleep_threshold// The sleeping threshold for the object’s angular velocity.
f@bullet_linear_sleep_threshold // The sleeping threshold for the object’s linear velocity.
i@bullet_want_deactivate// Disables simulation of a non-moving object until the object moves again. 
i@computecom// Specifies whether the center of mass should be computed from the collision shape.
i@computemass   // Specifies whether the mass should be computedfrom the collision shape and density.
f@creationtime  // Stores the simulation time at which the object was created.
i@dead  // Specifies whether the object should be deleted during the next solve.
f@density   // The mass of an object is its volume times its density.
f@friction  // The coefficient of friction of the object.
f@inertialtensorstiffness   // Rotational stiffness.  A scale factor applied to the inertial tensor. 
i@inheritvelocity   // v and w point attributes from the SOP geometry will override the initial velocity.
f@mass  // The mass of the object.
s@name  // A unique name for the object. Used by Constraint Networks.
p@orient// The orientation of the object.
v@P     // The current position of the object’s center of mass.
v@pivot // The pivot that the orientation applies to. If i@computecom is non-zero, this is auto-computed.
v@v     // Linear velocity of the object.
v@w     // Angular velocity of the object, in radians per second.

i@bullet_adjust_geometry    // Shrinks the collision geometry.
i@bullet_autofit    // Use the bounds of the object for Box, Capsule, Cylinder, Sphere, or Plane.
f@bullet_collision_margin   // Padding distance between collision shapes.
s@bullet_georep     // Can be convexhull, concave, box, capsule, cylinder, compound, sphere, or plane.
i@bullet_groupconnected     // Create convex hull per set of connected primitives.
f@bullet_length     // The length of the Capsule or Cylinder collision shape in the Y direction.
v@bullet_primR  // Orientation of the Box, Capsule, Cylinder, or Plane collision shape.
v@bullet_primS  // Size of the Box collision shape.
v@bullet_primT  // Position of the Box, Sphere, Capsule, Cylinder, or Plane collision shape.
f@bullet_radius // Radius of the Sphere, Capsule, or Cylinder collision shape.
f@bullet_shrink_amount  // Specifies the amount of resizing done by Shrink Collision Geometry.

s@activationignore  // Won't be activated by collisions with any objects that match this pattern.
s@collisiongroup    // Specifies the name of a collision group that this object belongs to.
s@collisionignore   // The object will not collide against any objects that match this pattern.
f@min_activation_impulse// Minimum impulse that will cause the object to switch from inactive to active.

f@speedmin  // Minumum speed, in units per second, that a particle can move.
f@speedmax  // Maximum speed, in units per second, that a particle can move.
f@spinmin   // Minumum speed in radians per second that a particle can spin.
f@spinmax   // Maximum speed in radians per second that a particle can spin.
f@accelmax  // Limits the change in the object’s speed that is caused by enforcing constraints.
f@angaccelmax   // Limits the change in the object’s angular speed that is caused by enforcing constraints.

f@airresist // Specifies how important it is to match the target velocity (v@targetv).
f@drag      // How much the the v@targetv and f@airresist attributes effect the object.
f@dragexp   // Ranges from 1 to 2, default is set on the solver.  Used for both angular and linear drag.
v@force     // Specifies a force that will be applied to the center of mass of the object.
f@spinresist// Specifies how important it is to match the target angular velocity (v@targetw).
v@targetv   // Target velocity for the object. Used in combination with the f@airresist attribute.
v@targetw   // Target angular velocity for the object. Used in combination with the f@spinresist attribute.
v@torque    // Specifies a torque that will be applied to the object.

i@bullet_autofit_valid  // Stores whether the solver has already computed collision shape attributes.
i@bullet_sleeping   // Tracks whether the object has been put to sleep by the solver.
f@deactivation_time // Amount of time the speed has been below the Linear Threshold or Angular Threshold.
i@found_overlap // Used by the solver to determine whether it has performed the overlap test.
i@id    // A unique identifier for the object.
i@nextid// Stores the i@id the solver will assign to the next new object.
DOP Constraint Network Attributes
You can create attributes on the geometry to customize each constraint’s behavior and type. If a primitive attribute with the same name as a constraint property (such as damping) is present, the attribute value will be multiplied with the value from the constraint sub-data.

s@constraint_name    // Specifies a piece of relationship data by name, such as 'Glue' or 'Spring'.
s@constraint_type    // Specifies whether the constraint affects 'position', 'rotation' or 'all' degrees of freedom.
f@restlength    // Specifies the desired length of the constraint.
f@width  // Width of each edge.
f@density   //  Density of each point.
p@orient// Initial orientation of each point. This value is stored as a quaternion.
v@v     // Initial velocity of each point.
v@w     // Initial angular velocity of each point measured in radians per second.
f@friction  // Friction of each point.
f@klinear   // Defines how strongly the wire resists stretching.
f@damplinear// Defines how strongly the wire resists oscillation due to stretching forces.
f@kangular  // Defines how strongly the wire resists bending.
f@dampangular   // Defines how strongly the wire resists oscillation due to bending forces.
f@targetstiffness   // Defines how strongly the wire resists deforming from the animated position.
f@targetdamping // Defines how strongly the wire resists oscillation due to stretch forces.
f@normaldrag// The component of drag in the directions normal to the wire.
f@tangentdrag   // The component of drag in the direction tangent to the wire.
i@nocollide // Collision detection for the edge is disabled (Only used if Collision Handling is SDF).
v@restP // Rest position of each point.
p@restorient// Rest orientation of each point.
i@gluetoanimation   // Causes a point’s position and orientation to be constrained to the input geometry.
i@pintoanimation    // Causes a point’s position to be constrained to the input geometry.
v@animationP// Target position of each point.
p@animationorient   // Target orientation of each point.
v@animationv// Target velocity of each point.
v@animationw// Target angular velocity of each point.
i@independentcollisionallowed   // Toggle external collisions (Only non-SDF Geometric Collision).
i@independentcollisionresolved  // Unresolved external collisions (Only non-SDF Geometric Collision).
i@codependentcollisionallowed   // Toggle soft body collisions (Only non-SDF Geometric Collision).
i@codependentcollisionresolved  // Unresolved toggle soft body collisions (Only non-SDF Geometric Collision).
i@selfcollisionallowed  // Toggle self collisions (Only non-SDF Geometric Collision).
i@selfcollisionresolved // Unresolved toggle self collisions (Only non-SDF Geometric Collision).
DOP FLIP Attributes
The FLIP Solver contains an embedded POP Solver, so all of POP Attributes listed above apply.

f@pscale// Particle scale
v@v     // Particle velocity
f@viscosity // The "thickness" of a fluid.
f@density   // The mass per unit volume.
f@temperature   // The temperature of the fluid.
f@vorticity // Measures the amount of circulation in the fluid.
f@divergence// Positive values cause particles to spread out, negative cause them to clump together.
v@rest  // Used to track the position of the fluid over time.
v@rest2 // Used for blending dual rest attributes, avoids stretching. 
f@droplet   // Identifies particles that separate from the main body of fluid.
f@underresolved // Particles that haven't fully resolved on the grid.
i@ballistic // Specifies particles which will be ignored by the fluid solve.
v@Lx    // Angular momentum X axis
v@Ly    // Angular momentum Y axis
v@Lz    // Angular momentum Z axis
DOP Vellum Attributes
Vellum geometry is also considered particles, so all of POP Attributes listed above apply.

i@isgrain     // A value of 1 causes the particle to behave as grains.  Distinguish between cloth and grains.
f@attractionweight  // How much the particles will naturally stick together when close, zero disables clumping.
f@friction // How much to scale the static friction.
f@dynamicfriction // How much to scale the dynamic friction.
f@inertia // Resistance of a particle to rotational hair or wire constraints. If this is zero, the particle will not rotate.
v@v // Point velocity.
p@w // (Hair or Wire) angular velocity.
p@orient // (Hair or Wire) orientations.
i@stopped // Control pins using @stopped rather than @mass (0=free, 1=no motion, 2=no rotation, 3=no rotate or move).
i@pintoanimation // If 1, the pinned points' position will be updated to match the target point of target path's geometry.
i@gluetoanimation // If 1, both the position and orientation will be updated
s@target_path // target path for any pins (when the Target parameter is set in Vellum Source)
i@target_pt // target point number for any pins (when the Target parameter is set in Vellum Source)
f@targetweight // Affect the strength of the pinned points using a 0..1 weighting value.
i@weld // Weld this point to a point number.  If there is an @id attribute, then to a point id.
i@branchweld // built by hair constraints when it is forced to split points for hair simulation.
i@collisionweld // generated on demand to provide a single weld to the detangle algorithm.
f@breakthreshold // The threshold for breaking welds and branch welds
s@breaktype // one of the following: 'stretchstress', 'bendstress', 'stretchdistance', 'stretchratio', or 'bendangle'.

// Collisions
f@pscale    // Used to determine the thickness of cloth or radius of each particle.
f@overlap_self // Stores how much of the original pscale is overlapped.
f@overlap_external // Stores how much of the original pscale is overlapped.
i@layer // Point attribute which indicates belonging to different layers of cloth. Higher numbers refer to higher layers.
i@disableself // A value of 0 means this point will use self collisions.
i@disableexternal // A value of 0 means this point will use external collisions.
s@collisionignore // Stores a pattern for the objects and collision groups to not collide with.
s@collisiongroup // Gives the collision group that this point belongs to.


// When a point is part of a Pressure constraint, these attributes hold values computed during constraint evaluation.
v@pressuregradient // a vector pointing outwards along the direction of greatest volume gain.
i[]@volumepts // contains array of the points needed to compute the volume attribute.
i@volume // compare against the Pressure constraint’s restlength

// Internal worker variables (Kept to avoid removing/adding attributes every frame)
v@pprevious // For 1st order integration, the previous frames position (beginning of timestep).
v@plast  // For 2nd order integration, the position from two frames earlier.
v@vprevious // For 1st order integration, the previous frames velocity (beginning of timestep).
v@vlast // For 2nd order integration, the velocity from two frames earlier.
p@orientprevious // For 1st order integration, the previous frames orientation (beginning of timestep).
p@orientlast // For 2nd order integration, the orientation from two frames earlier.
p@wprevious // For 1st order integration, the previous frames angular velocity (beginning of timestep).
p@wlast // For 2nd order integration, the angular velocity from two frames earlier.
f@dP // Constraint displacements.  Likely of last iteration.
f@dPw // Constraint weights.  Likely of last iteration.
s@patchname // Identifies each generated patch in a simulation so it can be updated/replaced.
DOP Vellum Constraint Attributes
There are many types of constraints, so the meaning of these variables is often dependent on the constraint type. They usually live on the primitive.

s@type // Type of the constraint.
    distance // Each edge in the display geometry is turned into a distance constraint maintaining that edge length.
    stitch // Stitch points within the same geometry together using distance constraints. The points do not need to actually be connected by geometry. This is useful for keeping jackets closed or preventing pockets from flapping
    branchstitch // 
    ptprim // 
    bend // Each pair of triangles (or implied triangles if input is quads or higher) creates a constraint maintaining the initial dihedral angle between the triangles.
    trianglebend // Each pair of triangles (or implied triangles if input is quads or higher) creates a constraint maintaining the initial dihedral angle between the triangles.
    angle
    tetvolume
    pressure // Each piece, as determined by the Define Pieces parameter, stores its original volume and a many-point constraint is built to maintain it. The enforcement is global, so squishing one place will expand another, like a balloon.
    attach, pin
    attachnormal
    pinorient
    bendtwist
    stretchshear
    tetfiber
    triarap
    tetarap*

f@dampingratio // 
f@stress // Estimate of work done by the constraint (updated by Vellum solver).
