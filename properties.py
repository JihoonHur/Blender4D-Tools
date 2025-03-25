import bpy
from bpy.props import FloatProperty, BoolProperty, EnumProperty

def register():
    bpy.types.Scene.enable_axis = BoolProperty(name="Enable Axis", default=False)
    bpy.types.Scene.align_x = FloatProperty(name="X Align", default=0.5, min=0.0, max=1.0)
    bpy.types.Scene.align_y = FloatProperty(name="Y Align", default=0.5, min=0.0, max=1.0)
    bpy.types.Scene.align_z = FloatProperty(name="Z Align", default=0.5, min=0.0, max=1.0)
    bpy.types.Scene.set_origin = EnumProperty(
        name="Set Origin",
        description="Set Origin options",
        items=[
            ('ORIGIN_TO_GEO', "Origin to Geometry", "Move origin to the geometry axis"),
            ('GEO_TO_ORIGIN', "Geometry to Origin", "Move geometry to the origin"),
            ('ORIGIN_TO_CURSOR', "Origin to 3D Cursor", "Move origin to the 3D cursor"),
            ('CURSOR_TO_ORIGIN', "3D Cursor to Origin", "Move 3D cursor to the origin of selected object"),
        ],
        default='ORIGIN_TO_GEO'
    )

def unregister():
    del bpy.types.Scene.enable_axis
    del bpy.types.Scene.align_x
    del bpy.types.Scene.align_y
    del bpy.types.Scene.align_z
    del bpy.types.Scene.set_origin