import bpy

class ColorplotProperties(bpy.types.PropertyGroup):
    scale: bpy.props.FloatProperty()
    image: bpy.props.PointerProperty(type = bpy.types.Image)
