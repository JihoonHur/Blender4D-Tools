import bpy

class OT_ResetPivotValues(bpy.types.Operator):
    bl_idname = "object.reset_pivot_values"
    bl_label = "Reset Pivot Values"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        context.scene.align_x = 0.5
        context.scene.align_y = 0.5
        context.scene.align_z = 0.5
        return {'FINISHED'}