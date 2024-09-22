import bpy

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

class ColorplotAnalyze(bpy.types.Operator):
    """Analyze and store the appearance of different colors in the source"""
    bl_idname = "colorplot.analyze_op"
    bl_label = "Analyze Colors"

    def execute(self, context):
        props = context.object.colorplot_props

        if props.image:
            count = 0
            pixels = props.image.pixels[:] # This converts the pixels python object to a native tuple, which is massively faster
            channels = props.image.channels
            for pixel in chunker(pixels, channels):
                count += 1
            print(count)

        return {'FINISHED'}