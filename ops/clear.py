import bpy

from ..props import ColorplotProperties

class ColorplotClear(bpy.types.Operator):
    """Clears all previous spheres from a color plot"""
    bl_idname = "colorplot.clear_op"
    bl_label = "Clear"

    def execute(self, context):
        if context.object.colorplot_values.spheres:
            spheres = context.object.colorplot_values.spheres.objects[:]
            for sphere in spheres:
                try:
                    bpy.context.collection.objects.unlink(sphere)
                except:
                    pass
            context.object.colorplot_values.spheres = None
        return {'FINISHED'}