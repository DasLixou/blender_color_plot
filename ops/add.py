import bpy

from ..props import ColorplotProperties

class ColorplotAdd(bpy.types.Operator):
    """Add a 3d color plot to the scene"""
    bl_idname = "colorplot.add_op"
    bl_label = "Color Plot"

    def execute(self, context):
        o = bpy.data.objects.new("Color Plot", None)
        bpy.context.collection.objects.link(o)
        o.colorplot_props.scale = 10
        select_one_object(o)
        return {'FINISHED'}
    
def draw_add_menu_appendix(self, context):
    layout = self.layout
    layout.separator()
    layout.operator(ColorplotAdd.bl_idname, icon = "FORCE_LENNARDJONES")

def select_one_object(obj):
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)