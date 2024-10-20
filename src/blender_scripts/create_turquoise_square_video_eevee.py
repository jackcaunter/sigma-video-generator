import bpy #type: ignore
import os

# Clear existing objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Set up the scene
scene = bpy.context.scene
scene.render.engine = 'BLENDER_EEVEE_NEXT'
scene.render.film_transparent = True
scene.render.resolution_x = 1080
scene.render.resolution_y = 1920
scene.render.fps = 30
scene.frame_end = 30  # 1 second at 30fps

# Enable motion blur
scene.render.use_motion_blur = True

# Create a plane and scale it
bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=False, location=(0, 0, 0))
plane = bpy.context.active_object
plane.scale = (0.5, 0.5, 1)  # Adjust scale as needed

# Add material to the plane
material = bpy.data.materials.new(name="Turquoise_Material")
material.use_nodes = True
plane.data.materials.append(material)

# Set material color to turquoise
nodes = material.node_tree.nodes
diffuse_node = nodes["Principled BSDF"]
diffuse_node.inputs["Base Color"].default_value = (0.25, 0.88, 0.82, 1)  # Turquoise color

# Set up camera
bpy.ops.object.camera_add(location=(0, 0, 5), rotation=(0, 0, 0))
camera = bpy.context.active_object
scene.camera = camera

# Set up lighting
bpy.ops.object.light_add(type='SUN', radius=1, location=(0, 0, 10))

# Set the output path
output_path = os.path.join(os.path.dirname(bpy.data.filepath), "output", "test_output_eevee.mp4")
scene.render.filepath = output_path
scene.render.image_settings.file_format = 'FFMPEG'
scene.render.ffmpeg.format = 'MPEG4'
scene.render.ffmpeg.codec = 'H264'

# Render the animation
bpy.ops.render.render(animation=True)

print(f"Video rendered and saved to: {output_path}")
