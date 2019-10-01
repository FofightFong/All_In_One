
[Acoustic]()

Design audio filters and sound materials for the spatial audio system.


[Agent]()

Imports an animation clip from an agent primitive.


[Area]()

Calculates the area under a channel’s graph, which is the same as calculating the integral of a channel, or integrating the channel.


[Attribute]()

Adds, removes or updates attributes of the input chop.


[Audio In]()

Receives audio input from the analog audio ports or the digital port.


[Band EQ]()

A 14-band equalizer which filters audio input channels in the same way that a conventional band equalizer uses a bank of sliders to filter fixed-frequency bands of sound.


[Beat]()

Manually tap the beat of a piece of music, and automatically generate a repeating ramp or pulse that continues to keep time with the music after the taps stop.


[Blend]()

Combines two or more chops in input 2, 3 and so on, by using a set of blending channels in input 1.


[BlendPose]()

Performs multi-dimensional, example-based interpolation of channels.


[Channel]()

Creates channels from the value of its parameters.


[Channel VOP]()

Contains a VOP network that can manipulate channel data.


[Channel Wrangle]()

Runs a VEX snippet to modify channel data.


[Composite]()

Layers (blends) the channels of one CHOP on the channels of another CHOP.


[Constant]()

Create up to forty new channels.


[Constraint Blend]()

Combines two or more chops by using a list of weights specified as parameters.


[Constraint Get Local Space]()

Returns an Object Local Transform.


[Constraint Get Parent Space]()

Returns an Object Parent Transform.


[Constraint Get World Space]()

Returns an Object World Transform.


[Constraint Lookat]()

Constrains rotation so it always points toward a target position.


[Constraint Object]()

Compares two objects and returns information on their relative positions and orientations.


[Constraint Object Offset]()

Compares two objects and returns information on their relative positions and orientations.


[Constraint Object Pretransform]()

Returns an Object Pretransform.


[Constraint Offset]()

Applies an transformation offset after evaluating a constraint.


[Constraint Parent]()

Reparent an object.


[Constraint Path]()

Position an object on a path and orient it to the path’s direction.


[Constraint Points]()

Position and Orient an object using point positions from a geometry.


[Constraint Sequence]()

Combines multiple chops by blending the inputs in sequence.


[Constraint Simple Blend]()

Combines two chops by using a single weight specified as a parameter.


[Constraint Surface]()

Position and Orient an object using the surface of a geometry.


[Constraint Transform]()

Takes translate, rotate, and/or scale channels and transforms them.


[Copy]()

Produces multiple copies of the second input along the timeline of the first input.


[Count]()

Counts the number of times a channel crosses a trigger or release threshold.


[Cycle]()

Creates cycles.


[Delay]()

Delays the input, and can be run in normal or time-sliced mode.


[Delete]()

Removes channels coming from its input.


[Device Transform]()

Turns data from device inputs into transform data


[Dynamics]()

Extracts any information from a DOP simulation that is accessible through the dopfield expression function.


[Envelope]()

Outputs the maximum amplitude in the vicinity of each sample of the input.


[Euler Rotation Filter]()

Fixes discontinuity of rotation data after cracking matrices


[Export]()

A convenient tool for exporting channels.


[Export Constraints]()

Export Constraints Network on any object


[Expression]()

Modify input channels by using expressions.


[Extend]()

Only sets the "extend conditions" of a chop, which determines what values you get when sampling the CHOP before or after its interval.


[Extract Bone Transforms]()

Extracts the current world or local space bone transforms from a geometry object.


[Extract Locomotion]()

Extracts locomotion from an animation clip.

[Extract Pose-Drivers]()

Creates channels from the specified derived transforms, node parameters and CHOP channels for pose-space deformation.


[FBX]()

Reads in channel data from an FBX file.


[Fan]()

Used for controlling other CHOPs.


[Feedback]()

Get the state of a chop as it was one frame or time slice ago.


[Fetch Channels]()

Imports channels from other CHOPs.


[Fetch Parameters]()

Imports channels from other OPs.


[File]()

Reads in channel and audio files for use by chops.


[Filter]()

Smooths or sharpens the input channels.


[Foot Plant]()

Computes when position channels are stationary.


[Foreach]()

Divides the input channels into groups, cooking the contained network for each group.


[Function]()

Provides more complicated math functions than found in the Math CHOP such as trigonometic functions, logarithmic functions, and exponential functions.


[Gamepad]()

Turns input values for the gamepad or joystick device into channel outputs.


[Geometry]()

Uses a geometry object to choose a sop from which the channels will be created.


[Gesture]()


[Handle]()

The "engine" which drives Inverse Kinematic solutions using the Handle object.


[Hold]()

Sample and hold the value of the first input.


[IKSolver]()

Solves inverse kinematics rotations for bone chains.


[Identity]()

Returns an identity transform.


[Image]()

Converts rows and/or columns of pixels in an image to CHOP channels.


[Interpolate]()

Treats its multiple-inputs as keyframes and interpolates between them.


[InverseKin]()

Generates channels for bone objects based on a bone chain and an end affector.


[Invert]()

Returns an invert transform of the input.


[Jiggle]()

Creates a jiggling effect in the translate channels passed in.


[Keyboard]()

Turns key presses into channel output.


[Lag]()

Adds lag and overshoot to channels.


[Layer]()

Mix weighted layers of keyframed animation from multiple Channel CHOPs to a base Channel CHOP.


[Limit]()

Provides a variety of functions to limit and quantize the input channels.


[Logic]()

Converts channels of all its input chops into binary channels and combines them using a variety of logic operations.


[Lookup]()

Uses a channel in the first input to index into a lookup table in the second input, and output values from the lookup table.


[MIDI In]()

The MIDI In CHOP reads Note events, Controller events, Program Change events, and Timing events from both midi devices and files.


[MIDI Out]()

The MIDI Out CHOP sends MIDI events to any available MIDI devices.


[Math]()

Perform a variety of arithmetic operations on and between channels.


[Merge]()

Takes multiple inputs and merges them into the output.


[Mouse]()

Outputs X and Y screen values for the mouse device.


[Mouse 3D]()

Turns input values for the Connexion space mouse into channel outputs.


[Multiply]()

Post multiplies all the input transformations.


[Network]()

Similar to the Pipe In/Out CHOPs in Network mode.


[Noise]()

Makes an irregular wave that never repeats, with values approximately in the range -1 to +1.


[Null]()

Used as a place-holder and does not have a function of its own.


[Object]()

Compares two objects and returns information on their relative positions and orientations.


[ObjectChain]()

Creates channels representing the transforms for a chain of objects.


[Oscillator]()

Generates sounds in two ways.


[Output]()

Marks the output of a sub-network.


[Parametric EQ]()

Filters an audio clip, and then applies other audio effects.


[Particle]()

Produces translate and rotate channels to move Objects according to the positions of particles in a POP Network.


[Pass Filter]()
Filters audio input using one of four different filter types.


[Phoneme]()

Translates english text into a series of phonetic values.


[Pipe In]()

Pipes data from custom devices into a CHOP, without needing the Houdini Developers' Kit or knowledge of Houdini internals.


[Pipe Out]()

Transmit data out of Houdini to other processes.


[Pitch]()

Attempts to extract the fundamental pitch of a musical tone from the input audio.


[Pose]()

Store a transform pose for later use by evaluating the input.


[Pose Difference]()

Computes the difference between two poses.


[Pretransform]()

Takes translate, rotate, and/or scale channels and transforms them using the pretransform of the given object.


[Pulse]()

Generates pulses at regular intervals of one channel.


[ROP Channel Output]()


Record


[Rename]()

Renames channels.


[Reorder]()

Reorders the first input CHOP’s channels by numeric or alphabetic patterns.


[Resample]()

Resamples an input’s channels to a new rate and/or start/end interval.


[Sequence]()

Takes all its inputs and appends one chop after another.


[Shift]()

This time-shifts a CHOP, changing the start and end of the CHOP’s interval.


[Shuffle]()

Reorganizes a list of channels.


[Slope]()

Calculates the slope (or derivative) of the input channels.


[Spatial Audio]()

The rendering engine for producing 3D audio.


[Spectrum]()

Calculates the frequency spectrum of the input channels, or a portion of the channels.


[Spline]()

Edit the channel data by using direct manipulation of cubic or Bezier handles in the graph of the CHOP.


[Spring]()

Creates vibrations influenced by the input channels, as if a mass was attached to a spring.


[Stash]()

Caches the input motion in the node on command, and then uses it as the node’s output.

[Stash Pose]()

Stashes the bone transforms and pose-drivers for use by the Pose-Space Deform SOP and Pose-Space Edit SOP nodes.


[Stretch]()

Preserves the shape of channels and the sampling rate, but resamples the channels into a new interval.


[Subnetwork]()

Allows for the simplification of complex networks by collapsing several CHOPs into one.


[Switch]()

Control the flow of channels through a CHOPnet.


[Time Range]()

This converts an input node in Current Frame mode to a Time Range mode by re-cooking it multiple times.


[Time Shift]()

This time-shifts a CHOP, re-cooking the node using different time.


[Transform]()

Takes translate, rotate, and/or scale channels and transforms them.


[TransformChain]()

Combines a chain of translate, rotate, and/or scale channels.


[Trigger]()

Adds an audio-style attack/decay/sustain/release (ADSR) envelope to all trigger points in the input channels.


[Trim]()

Shortens or lengthens the input’s channels.


[VEX Waveform]()

This function is a sub-set of the waveform CHOP.


[Vector]()

Performs vector operations on a set or sets of channels.


[Voice Split]()

The Voice Split CHOP takes an audio track and separates "words" out into different channels.


[Voice Sync]()

The Voice Sync CHOP detects phonemes in an audio channel given some audio phoneme samples and pro…


[Warp]()

Time-warps the channels of the first input (the Pre-Warp Channels) using one warping channel in the second input.


[Wave]()

Creates a waveform that is repeated.
