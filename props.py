import bpy

class ColorplotProperties(bpy.types.PropertyGroup):
    image: bpy.props.PointerProperty(type = bpy.types.Image)
    weaken_alpha: bpy.props.BoolProperty(description = "Whether or not to take alpha into account when analyzing colors")
    scale: bpy.props.FloatProperty()

class ColorplotValues(bpy.types.PropertyGroup):
    values: bpy.props.FloatVectorProperty(size = (32, 32, 32)) # TODO: can't be larger than 32, need tuples wrapped around when needing more resolution
    spheres: bpy.props.PointerProperty(type = bpy.types.Collection)
