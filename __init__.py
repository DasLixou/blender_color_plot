import bpy

from .props import ColorplotProperties
from .ops.add import ColorplotAdd, draw_add_menu_appendix
from .panel import ColorplotSidepanel

def register():
    bpy.utils.register_class(ColorplotProperties)
    bpy.types.Object.colorplot_props = bpy.props.PointerProperty(type = ColorplotProperties)
    bpy.utils.register_class(ColorplotAdd)
    bpy.types.VIEW3D_MT_add.append(draw_add_menu_appendix)
    bpy.utils.register_class(ColorplotSidepanel)
    print("*Lixou's Blender Color Plot* was initialized!")

def unregister():
    bpy.utils.unregister_class(ColorplotSidepanel)
    bpy.types.VIEW3D_MT_add.remove(draw_add_menu_appendix)
    bpy.utils.unregister_class(ColorplotAdd)
    bpy.utils.unregister_class(ColorplotProperties)