import bpy

def get_or_create_sphere_mesh():
    mesh = bpy.data.meshes.get("__colorplot_sphere")
    if mesh:
        return mesh
    bpy.ops.mesh.primitive_uv_sphere_add(radius = 1, location = (0, 0, 0))
    mesh = bpy.context.object.data
    mesh.name = "__colorplot_sphere"
    return mesh

class ColorplotGenerate(bpy.types.Operator):
    """TODO"""
    bl_idname = "colorplot.generate_op"
    bl_label = "Generate Geometry"

    def execute(self, context):
        values = context.object.colorplot_values.values[:]

        mesh = get_or_create_sphere_mesh()

        for x in range(0, 32):
            for y in range(0, 32):
                for z in range(0, 32):
                    val = values[x][y][z]
                    if val > 0.0:
                        print(f"{x} {y} {z}")
                        sphere = bpy.data.objects.new(name = "ColorPlotShit", object_data = mesh)
                        bpy.context.collection.objects.link(sphere)
                        sphere.location = (x, y, z)
                        radius = val * 1000.
                        sphere.scale = (radius, radius, radius)

        return {'FINISHED'}