import bpy

from .ops.analyze import ColorplotAnalyze

class ColorplotSidepanel(bpy.types.Panel):
    bl_idname = "colorplot.sidepanel"
    bl_label = "Color Plot"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Color Plot"

    @classmethod
    def poll(cls, context):
        return (context.object is not None) and context.object.select_get() and ('colorplot_props' in context.object)
    
    def draw(self, context):
        layout = self.layout
        props = context.object.colorplot_props

        stage1 = layout.box()
        stage1.label(text = "(1) Analyze Image")
        stage1.template_ID_preview(props, "image", new="image.new", open="image.open")
        stage1.operator(ColorplotAnalyze.bl_idname)

        stage2 = layout.box()
        stage2.label(text = "(2) Plot stuff")
        stage2.prop(props, "scale", text = "Scale")