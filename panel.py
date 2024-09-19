import bpy

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

        layout.prop(props, "scale", text = "Scale")