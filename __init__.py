bl_info = {
    "name": "Cappuccino - Axis Center",
    "author": "a.k.a Luckycuky",
    "version": (1, 0, 0),
    "blender": (4, 4, 0),
    "location": "View3D > Sidebar > Cappuccino",
    "description": "Custom tools for object creation and pivot control",
    "category": "3D View"
}

import bpy
from . import properties, keymap
from .operators import toggle_axis, apply_pivot, reset_values
from .panel import ui_panel

classes = (
    toggle_axis.OT_ToggleEnableAxis,
    apply_pivot.OT_AlignPivot,
    reset_values.OT_ResetPivotValues,
    ui_panel.PT_PivotPanel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    properties.register()
    keymap.register()

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    properties.unregister()
    keymap.unregister()