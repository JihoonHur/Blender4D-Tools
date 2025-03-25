import bpy

class PT_PivotPanel(bpy.types.Panel):
    bl_label = "Axis Center"
    bl_idname = "PT_pivot_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Cappuccino"

    def draw(self, context):
        layout = self.layout
        obj = context.object
        is_enabled = obj is not None and obj.type == 'MESH'
        layout.enabled = is_enabled

        row = layout.row()
        row.scale_y = 2
        row.operator("object.toggle_enable_axis", text="Enable Axis Control", icon="OBJECT_ORIGIN", depress=context.scene.enable_axis)

        layout.separator()

        is_axis_enabled = context.scene.enable_axis
        is_slider_enabled = context.scene.set_origin == 'ORIGIN_TO_GEO' and not is_axis_enabled

        col = layout.column()
        col.enabled = not is_axis_enabled
        col.prop(context.scene, "set_origin", text="Set Origin")

        if not is_axis_enabled:
            col = layout.column()
            col.enabled = is_slider_enabled
            col.prop(context.scene, "align_x", text="X", icon="AXIS_FRONT", slider=True)
            col.prop(context.scene, "align_y", text="Y", icon="AXIS_SIDE", slider=True)
            col.prop(context.scene, "align_z", text="Z", icon="AXIS_TOP", slider=True)

        layout.separator()

        row = layout.row(align=True)
        row.enabled = not is_axis_enabled
        row.operator("object.apply_pivot", text="Execute", icon="CHECKMARK")
        row.operator("object.reset_pivot_values", text="", icon="LOOP_BACK")