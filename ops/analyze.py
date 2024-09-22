import bpy
import math
import colorsys
import numpy as np

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

class ColorplotAnalyze(bpy.types.Operator):
    """Analyze and store the appearance of different colors in the source"""
    bl_idname = "colorplot.analyze_op"
    bl_label = "Analyze Colors"

    def execute(self, context):
        props = context.object.colorplot_props
        values = np.zeros((32, 32, 32))

        if props.image:
            pixels = props.image.pixels[:] # This converts the pixels python object to a native tuple, which is massively faster
            channels = props.image.channels
            portion = len(pixels)
            if channels == 3:
                strength = 1.0 / portion
                for pixel in chunker(pixels, 3):
                    hsv = colorsys.rgb_to_hsv(pixel[0], pixel[1], pixel[2])
                    x = round(hsv[0] * 31.)
                    y = round(hsv[1] * 31.)
                    z = round(hsv[2] * 31.)
                    values[x][y][z] += strength
            elif channels == 4:
                for pixel in chunker(pixels, 4):
                    strength = pixel[3] if props.weaken_alpha else math.ceil(pixel[3])
                    strength = strength / portion
                    hsv = colorsys.rgb_to_hsv(pixel[0], pixel[1], pixel[2])
                    x = round(hsv[0] * 31.)
                    y = round(hsv[1] * 31.)
                    z = round(hsv[2] * 31.)
                    values[x][y][z] += strength
            else:
                self.report({'ERROR'}, "Analyze colors only works for images with 3 or 4 channels")
                
            context.object.colorplot_values.values[:] = values
        else:
            self.report({'ERROR'}, "No image given")

        return {'FINISHED'}