import bpy

class ColorplotAnalyze(bpy.types.Operator):
    """Analyze and store the appearance of different colors in the source"""
    bl_idname = "colorplot.analyze_op"
    bl_label = "Analyze Colors"

    def execute(self, context):
        return {'FINISHED'}