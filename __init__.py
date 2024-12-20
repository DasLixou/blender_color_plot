import bpy

from .props import ColorplotProperties, ColorplotValues
from .ops.add import ColorplotAdd, draw_add_menu_appendix
from .ops.analyze import ColorplotAnalyze
from .ops.clear import ColorplotClear
from .ops.generate import ColorplotGenerate
from .panel import ColorplotSidepanel

# TODO: https://blender.stackexchange.com/questions/9365/how-can-i-import-materials-from-another-blender-file-with-python

def register():
    bpy.utils.register_class(ColorplotProperties)
    bpy.utils.register_class(ColorplotValues)
    bpy.types.Object.colorplot_props = bpy.props.PointerProperty(type = ColorplotProperties)
    bpy.types.Object.colorplot_values = bpy.props.PointerProperty(type = ColorplotValues)
    bpy.utils.register_class(ColorplotAdd)
    bpy.utils.register_class(ColorplotAnalyze)
    bpy.utils.register_class(ColorplotClear)
    bpy.utils.register_class(ColorplotGenerate)
    bpy.types.VIEW3D_MT_add.append(draw_add_menu_appendix)
    bpy.utils.register_class(ColorplotSidepanel)
    print("*Lixou's Blender Color Plot* was initialized!")

def unregister():
    bpy.utils.unregister_class(ColorplotSidepanel)
    bpy.types.VIEW3D_MT_add.remove(draw_add_menu_appendix)
    bpy.utils.unregister_class(ColorplotGenerate)
    bpy.utils.unregister_class(ColorplotClear)
    bpy.utils.unregister_class(ColorplotAnalyze)
    bpy.utils.unregister_class(ColorplotAdd)
    bpy.utils.unregister_class(ColorplotValues)
    bpy.utils.unregister_class(ColorplotProperties)