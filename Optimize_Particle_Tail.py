import bpy
import bmesh
import random

def delete_random_triangles(obj, fraction_to_delete):
    # Switch to object mode if not already
    bpy.ops.object.mode_set(mode='OBJECT')

    # Create a bmesh object
    bm = bmesh.new()
    bm.from_mesh(obj.data)

    # Collect triangles
    triangles = [face for face in bm.faces if len(face.verts) == 3]

    # Calculate number of triangles to delete
    num_to_delete = int(len(triangles) * fraction_to_delete)

    # Randomly select triangles to delete
    to_delete = random.sample(triangles, num_to_delete)
    for face in to_delete:
        bm.faces.remove(face)

    # Remove isolated vertices
    bmesh.ops.delete(bm, geom=[v for v in bm.verts if not v.link_faces], context='VERTS')

    # Update the mesh
    bm.to_mesh(obj.data)
    bm.free()

# Example usage
# Replace 'YourObjectNameHere' with the name of your object
# and set your desired fraction of triangles to delete (e.g. 0.5 for 50%)
obj = bpy.data.objects['Tail']
fraction_to_delete = 0.3  # for example, delete 50% of the triangles
delete_random_triangles(obj, fraction_to_delete)
