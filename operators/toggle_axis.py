import bpy

def update_enable_axis(context):
    if context.scene.enable_axis:
        bpy.context.tool_settings.use_transform_pivot_point_align = True
        bpy.context.tool_settings.use_transform_data_origin = True
    else:
        bpy.context.tool_settings.use_transform_pivot_point_align = False
        bpy.context.tool_settings.use_transform_data_origin = False

class OT_ToggleEnableAxis(bpy.types.Operator):
    bl_idname = "object.toggle_enable_axis"
    bl_label = "Enable Axis Control"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        context.scene.enable_axis = not context.scene.enable_axis
        update_enable_axis(context)
        return {'FINISHED'}