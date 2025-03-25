import bpy
import mathutils

def execute_set_origin(context):
    obj = context.object
    if obj is None or obj.type != 'MESH':
        return
    set_origin_mode = context.scene.set_origin
    bpy.context.view_layer.objects.active = obj
    if set_origin_mode == 'GEO_TO_ORIGIN':
        bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN', center='BOUNDS')
    elif set_origin_mode == 'ORIGIN_TO_GEO':
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
    elif set_origin_mode == 'ORIGIN_TO_CURSOR':
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    elif set_origin_mode == 'CURSOR_TO_ORIGIN':
        bpy.ops.view3d.snap_cursor_to_selected()

def apply_pivot_center(context):
    obj = context.object
    if obj is None or obj.type != 'MESH':
        return
    set_origin_mode = context.scene.set_origin
    if set_origin_mode in ('ORIGIN_TO_CURSOR', 'GEO_TO_ORIGIN', 'CURSOR_TO_ORIGIN'):
        return
    bbox_corners = [mathutils.Vector(corner) for corner in obj.bound_box]
    min_x, max_x = min(v.x for v in bbox_corners), max(v.x for v in bbox_corners)
    min_y, max_y = min(v.y for v in bbox_corners), max(v.y for v in bbox_corners)
    min_z, max_z = min(v.z for v in bbox_corners), max(v.z for v in bbox_corners)
    new_x = min_x + (max_x - min_x) * context.scene.align_x
    new_y = min_y + (max_y - min_y) * context.scene.align_y
    new_z = min_z + (max_z - min_z) * context.scene.align_z
    new_origin = mathutils.Vector((new_x, new_y, new_z))
    offset = obj.matrix_world @ new_origin - obj.location
    obj.data.transform(mathutils.Matrix.Translation(-new_origin))
    obj.location += offset

class OT_AlignPivot(bpy.types.Operator):
    bl_idname = "object.apply_pivot"
    bl_label = "Apply Pivot Center"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        execute_set_origin(context)
        apply_pivot_center(context)
        return {'FINISHED'}