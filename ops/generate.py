import bpy
import os

def get_or_create_sphere_mesh():
    mesh = bpy.data.meshes.get("__colorplot_sphere")
    if mesh:
        return mesh
    
    script_file = os.path.realpath(__file__)
    directory = os.path.dirname(os.path.dirname(script_file))
    with bpy.data.libraries.load(os.path.join(directory, "Library.blend")) as (data_from, data_to):
        data_to.materials = [mat for mat in data_from.materials if mat == "ColorplotHSVMaterial"]
    bpy.ops.mesh.primitive_uv_sphere_add(radius = 1, location = (0, 0, 0))
    mesh = bpy.context.object.data
    mesh.name = "__colorplot_sphere"
    mesh.materials.append(data_to.materials[0])
    return mesh

class ColorplotGenerate(bpy.types.Operator):
    """Generates spheres sized accordingly to the color presence. Automatically clears old spheres"""
    bl_idname = "colorplot.generate_op"
    bl_label = "Generate Geometry"

    def execute(self, context):
        values = context.object.colorplot_values.values[:]

        bpy.ops.colorplot.clear_op()

        mesh = get_or_create_sphere_mesh()
        spheres = bpy.data.collections.new("ColorPlotSpheres")
        sphere_blueprint = bpy.data.objects.new(name = "ColorPlotShit", object_data = mesh)

        for x in range(0, 32):
            for y in range(0, 32):
                for z in range(0, 32):
                    val = values[x][y][z]
                    if val > 0.00000000001:
                        print(f"{x} {y} {z}")
                        sphere = sphere_blueprint.copy()
                        bpy.context.collection.objects.link(sphere)
                        spheres.objects.link(sphere)
                        sphere.location = (x / 32, y / 32, z / 32)
                        radius = val * 20.
                        sphere.scale = (radius, radius, radius)
        
        context.object.colorplot_values.spheres = spheres

        return {'FINISHED'}